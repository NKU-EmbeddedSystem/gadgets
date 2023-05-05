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
def calculate(mod1, mod2, reg, rm):
    i = 0
    left = 0
    res = []
    while i < 0xff:
        if i & 7 == reg or (i >> 3) & 7 == rm or (i >> 6) == mod1 or (i >> 6) == mod2:
            if left <= i - 1:
                res.append((left, i - 1))
            left = i + 1
        i += 1
    
    return res

def printb(mods, sibs, vexs):
    for i in range(0x100):
        for mod in mods:
            if i >= vector[0] and i <= vector[1]:
                print(r'\cellcolor{mod} ', end='')
                break

        if i in one_byte_instructions:
            print(r'\textcolor{red}'+ '{' + myhex(i) + '}', end='')
        else:
            print(myhex(i), end='')

        if (i+1) % 0x10 == 0:
            print(r'\\')
        else:
            print(' & ', end='')

if __name__ == '__main__':
    fill_instructions()
    res = calculate(0, 3, 5, 5)
    printb(res)
