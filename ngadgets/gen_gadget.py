import os
import re
import sys
import pathlib


gadgets = ['58c3', '5fc3', '5ac3', '5ec3', '0f05']
rs_set = ['rdx', 'r11', 'rsi', 'rbx', 'rdi', 'r8', 'rcx']
exec_path = ''

def get_registers(log:str):
    f = open(log, 'r')
    base = 110
    nums = []
    for i in range(base, base + 12):
        nums.append('0x' + str(i))

    lines = f.readlines()
    mm = dict()
    for line in lines:
        if line.find('0xc3') != -1 and line.find(',[') != -1:
            dd = line.split()
            # print gadget line
            print(dd[2], ' '.join(dd[3:]))
        for num in nums:
            if line.find(num) != -1 and line[line.find(num) - 1] == ',':
                mm[num] = line[line.find('r') : line.find(num) - 1]
                break
    return mm

def excute_js(js:str, filename:str)->bool:
    f = open(filename + '.js', 'w')
    f.write(js)
    f.close()
    os.system(exec_path + ' --print-opt-code ' + filename + '.js > ' + filename + '.txt')
    f = open(filename + '.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        for jsc in gadgets:
            if line.find('lea') != -1 and line.find(jsc) != -1:
                words = line.split()
                if len(words) > 3 and words[2].find(jsc) != -1 and words[2].find(jsc) % 2 == 0:
                    print(words)
                    gadgets.remove(jsc)
                    os.system('cp '  + filename + '.js '  + jsc + '.js')

def generate_js(count:int):
    header = '''
var array = new Uint8Array();
function syscall_jsc('''

    for i in range(11):
        header += 'var' + str(i) + ', '
    header += 'var11){\n'
    base = 110
    middle1 = ''
    for i in range(count):
        var = 't' + str(i)
        middle1 += '\tvar ' + var + ' = var' + str(i) + ' & 0x' + str(base) + ';\n'
        base += 1
    
    jscs = []

    for i in range(count):
        for j in range(i, count):
            jsc = '\tvar s = t' + str(i) + ' * 2 + t' + str(j) + ' + 0xc3;\n    return  '
            jscs.append(jsc)

    middle2 = ''
    for i in range(count - 1):
        middle2 += 't' + str(i) + ' ' + '+ '
    middle2 += 't' + str(count-1) + ' | s;\n}\n'

    tail = '''
for(var i = 0; i < 0x10000; i++)
{
'''
    tail += '\tsyscall_jsc('
    for i in range(count - 1):
        tail += '0xc' + str(i) + ', '
    tail += '0xc' + str(count - 1) + ');'
    tail += '\n}\n'

    for i, jsc in enumerate(jscs):
        excute_js(header + middle1 + jsc + middle2 + tail, str(i))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('plese input the path of v8')
        exit()
    
    exec_path = sys.argv[1]
    p = pathlib.Path(exec_path)
    if not p.is_file():
        print('path of v8 error')
        exit()


    # for i in range(32):
    generate_js(12)
    print('done')
