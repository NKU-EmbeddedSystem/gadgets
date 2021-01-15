import os
import re
import sys
import pathlib
import random
import time


gadgets = ['58c3', '5fc3', '5ac3', '5ec3', '0f05']
# gadgets = ['5ec3']
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
array = new Uint8Array();
const constant = 0x1234;
function payload3(v1, v2) {
    array[0] = v1 ^ 0x11;
	if (v1 > 0){
		array[1] = 0x00;
'''

    ops = ['&', '*']
    middle = ''
    for i in range(count):
        # middle += '        g15 ' +  ops[i % len(ops)] + '= ' + hex(random.randint(0xa0000000, 0xffffffff)) + ';\n'
        middle += '        array[15] ' +  ops[i % len(ops)] + '= ' + "0x56" + ';\n'

    tail = \
'''
	}
	else{
		array[1] = 0x01;
	}
	array[16] = v1 * 0x77;
	array[2];
	if (v1 > 0)
		array[2] = 0x00;
	else
		array[2] = 0x01;
	array[17] = v1 * 0x88;
	array[18] = v1 * 0x99;
	array[19] = v1 * 0x12;
	array[20] = v1 * 0x23;
	array[21] = v1 * 0x34;
	return array[0] ^ array[1] ^  array[15] ^ array[16] ^ array[17] ^ array[18] ^ array[19] ^ array[20] ^ array[21];
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
    for i in range(2100, 10000):
        print(i)
        js = generate_js(i)
        excute_js(js)
        if len(gadgets) == 0:
            break
    # time.sleep(1)
    # print(js)
    # excute_js(js)