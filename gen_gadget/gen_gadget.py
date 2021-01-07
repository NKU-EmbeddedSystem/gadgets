import os
import re
import sys
import pathlib


gadgets = ['5ec3', '5ac3']
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
            if line.find(jsc) != -1:
                words = line.split(' ')
                while '' in words: words.remove('')
                # print(words)
                if len(words) > 3 and words[2].find(jsc) != -1 and words[2].find(jsc) % 2 == 0:
                    print(words[2])
                    os.system('cp test.js ' + jsc + str(dd[gadgets.index(jsc)]) + '.js')
                    dd[gadgets.index(jsc)] += 1
                    return True
    return False

def search_word(word:str, lines:list):
    result = ''
    for line in lines:
        if line.find(word) != -1:
            result += line
    return result

def analyse(count:int):
    f = open('test.txt', 'r')
    lines = f.readlines()
    f.close()
    result = ''
    for i in range(111, 114 + count):
        result += search_word(',0x'+str(i), lines)
    return result

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
    middle1 = ''
    for i in range(count):
        var = 't' + str(i)
        middle1 += '\tvar ' + var + ' = var1 ' + ops[i % len(ops)] + ' 0x' + str(base) + ';\n'
        base += 1
    
    jscs = []
    for i in range(count):
        for j in range(count):
            if i == j:
                continue
            jsc = '\tvar s = t' + str(i) + ' + t' + str(j) + ' * 2 + 0xc3;\n    return a0 | a1 + a2 | '
            jscs.append(jsc)

    middle2 = ''
    op2s = ['+', '|']
    for i in range(count - 1):
        middle2 += 't' + str(i) + ' ' + '+ '
    middle2 += 't' + str(count-1) + ' | s;\n}'

    tail = '''
for(var i = 0; i < 0x10000; i++)
{
    syscall_jsc(0xc35, 0xc22, 0xc32, 0xc55);
}
'''
    for jsc in jscs:
        excute_js(header + middle1 + jsc + middle2 + tail)
    # return header + middle1 + jsc + middle2 + tail


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
        # excute_js(test_js)
        # f.write(analyse(i))
        # f.close()
    print('done')