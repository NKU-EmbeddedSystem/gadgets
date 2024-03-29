#!/usr/bin/env python
# coding=utf-8
one_byte_instructions = set([0x60, 0x61,0x98,0xa4,0xa5,0xd7,0xf4,0xcc,0xce,0xcf,0xc9,0xc3,0xcb,0xf5,0xf8,0xf9,0xfa,0xfb,0xfc,0xfd,0x9e,0x9f,0xd6])

def fill_instructions():
    for i in range(8):
        one_byte_instructions.add(0x40 + i)
        one_byte_instructions.add(0x48 + i)
        one_byte_instructions.add(0x50 + i)
        one_byte_instructions.add(0x58 + i)
        one_byte_instructions.add(0x90 + i)

def myhex(num):
    res = hex(num).upper()[2:]
    if len(res) == 1:
        res = '0' + res
    return res

def calculate(index, base):
    i = 0
    left = 0
    res = []
    while i < 0xff:
        if i & 7 == base or (i >> 3) & 7 == index:
            if left <= i - 1:
                res.append((left, i - 1))
            left = i + 1
        i += 1
    
    return res

def printb(vectors):
    count = 0
    for i in range(0x100):
        flag = 0
        if i in one_byte_instructions:
            print(r'\cellcolor{green} ', end='')
            flag = 1
        for vector in vectors:
            if i >= vector[0] and i <= vector[1]:
                if flag == 1:
                    count += 1
                    flag = 0
                print(r'\textcolor{red}'+ '{' +myhex(i) + '}', end='')
                break
        else:
            print(myhex(i), end='')

        if (i+1) % 0x10 == 0:
            print(r'\\')
        else:
            print(' & ', end='')

    print(count / len(one_byte_instructions))

if __name__ == '__main__':
    fill_instructions()
    res = calculate(5, 5)
    print(len(res) / 256)
    printb(res)
