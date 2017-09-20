# -*- coding: utf-8 -*-
def myPow(a,b):
    #b = bin(b);
    #i = len(b) - 1
    res = 1
    base = a
    while b != 0:
        if b & 1 == 1:
            res *= base
        base *= base
        b = b >> 1
    return res

if __name__ == '__main__':
    (a, b, m) = input().split()
    print(myPow(int(a), int(b)) % int(m))