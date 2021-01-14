import os
import re
import sys
import pathlib
import random
import time


gadgets = ['58c3', '5fc3', '5ac3', '5ec3', '0f05']
exec_path = ''

def excute_js(js:str)->bool:
    f = open('test.js', 'w')
    f.write(js)
    f.close()
    os.system(exec_path + ' --always-opt --print-opt-code test.js | grep rip > test.txt')
    f = open('test.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        for jsc in gadgets:
            if line.find('rip') != -1 and line.find(jsc) != -1:
                words = line.split()
                if len(words) > 3 and words[2].find(jsc) != -1 and words[2].find(jsc) % 2 == 0:
                    print(words)
                    gadgets.remove(jsc)
                    os.system('cp test.js ' + jsc + '.js')
    return True

def generate_js(count:int):
    m = 0
    header = \
'''
const constant = 0xfff12345;
function payload3(x, v2) {
    x = x ^ 0x44444444444444;
	if (x < 0) {
		x = -x;
	}
	else {
		x = x + constant;
	}
'''
    ops = ['&', '*']
    middle = ''
    for i in range(count):
        middle += '    var g' + str(i) + ' = x ' + ops[i % len(ops)] + ' ' + str(random.randint(0, 0xffffffff)) + ';\n'

    op2s = ['+', '|']
    middle += '    return '
    for i in range(count):
        middle += 'g' + str(i) + op2s[i % len(op2s)]
    
    middle += 'constant;\n}'
    tail = \
'''
for (var i = 0; i < 0x1; i++) {
    payload3(i, i % 32);
}
'''
    return header + middle + tail;
        # excute_js(header + middle1 + jsc + middle2 + tail)
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


    # for i in range(24):
    #     generate_js(i)
    # print('done')
    for i in range(100000, 0xffffff):
    # i = 100000
        print(i)
        js = generate_js(i)
        excute_js(js)
        time.sleep(1)
    # print(js)
    # excute_js(js)