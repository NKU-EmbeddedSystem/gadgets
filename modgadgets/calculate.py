#!/usr/bin/env python
# coding=utf-8
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

def printb(vectors):
    for i in range(0x100):
        for vector in vectors:
            if i >= vector[0] and i <= vector[1]:
                print(hex(i)[2:], end='')
                break
        else:
            print(r'\textcolor{red}'+ '{' + hex(i)[2:] + '}', end='')

        if (i+1) % 0x10 == 0:
            print(r'\\')
        else:
            print(' & ', end='')

if __name__ == '__main__':
    res = calculate(0, 3, 5, 5)

    printb(res)
