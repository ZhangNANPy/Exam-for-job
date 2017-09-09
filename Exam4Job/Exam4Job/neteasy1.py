# -*- coding: utf-8 -*-
#魔法币

n = 10

def magicCoin(n):
    re = []
    if n == 1:
        re.append(1)
    elif n == 2:
        re.append(2)
    while n > 2:
        if n % 2 == 0:
            n = (n-2)/2
            re.append(2)
        else:
            n = (n-1)/2
            re.append(1)
    re.append(int(n))
    re.reverse()
    return re

if __name__ == "__main__":
    print(''.join([str(i) for i in magicCoin(n)]))