import os
import re
import sys
import pathlib

def generate_js(count:int):
    ops = ['&', '+', '*', '^']
    header = '''
var array = new Uint8Array();
function syscall_jsc(var1, var2, var3, var4){
    var a0 = var1 ^ 0x111;
    var a1 = var1 ^ 0x112;
    var a2 = var1 ^ 0x113;
'''

    base = 114
    middle = ''
    for i in range(count):
        var = 't' + str(i)
        middle += '\tvar ' + var + ' = var1 ' + ops[i % len(ops)] + ' 0x' + str(base) + ';\n'
        base += 1
    middle += '\tvar s = t' + str(count - 2) + ' + t' + str(count - 1) + ' * 2 + 0xc3;\n    return a0 | a1 + a2 | '

    op2s = ['+', '|']
    for i in range(count - 1):
        middle += 't' + str(i) + ' ' + op2s[i % len(op2s)] + ' '
    middle += 't' + str(count-1) + '\n}'

    tail = '''
for(var i = 0; i < 0x10000; i++)
{
    syscall_jsc(0xc35, 0xc22, 0xc32, 0xc55);
}
'''
    return header + middle + tail

def excute_js(js:str, gadget:str, path:str):
    f = open('test.js', 'w')
    f.write(js)
    f.close()
    os.system(path + ' --print-opt-code test.js > test.txt')

def search_word(word:str, lines:list):
    result = ''
    for line in lines:
        if line.find(word) != -1:
            result += line
    return result

def analyse(gadget:str, count:int):
    f = open('test.txt', 'r')
    lines = f.readlines()
    f.close()
    result = ''
    for i in range(111, 114 + count):
        result += search_word(',0x'+str(i), lines)
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('plese input the path of v8')
        exit()
    
    exec_path = sys.argv[1]
    p = pathlib.Path(exec_path)
    if not p.is_file():
        print('path of v8 error')
        exit()

    gadgets = ['58c3', '5fc3', '5ec3', '5ac3', '0f05'] 

    for i in range(32):
        f = open(str(i) + '.txt', 'w')
        test_js = generate_js(i)
        f2 = open(str(i) + '.js', 'w')
        f2.write(test_js)
        f2.close()
        excute_js(test_js, gadgets[0], exec_path)
        f.write(analyse(gadgets[0], i))
        f.close()
    print('done')