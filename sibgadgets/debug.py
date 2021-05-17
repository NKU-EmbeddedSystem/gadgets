#!/usr/bin/env python
# coding=utf-8
def calculate(index, base):
    i = 0
    left = 0
    res = []
    while i < 0xff:
        if i & 7 == base or (i >> 3) & 7 == index:
            if left <= i - 1:
                res.append((bin(left), bin(i - 1)))
            left = i + 1
        i += 1
    
    return res

if __name__ == '__main__':
    print(calculate(5, 5))
