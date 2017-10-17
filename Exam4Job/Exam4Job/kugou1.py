# -*- coding: utf-8 -*-
n = int(input())
k = n % 8
res = int(n / 8)
if n >= 12:
    if k == 2 or k == 4 or k == 6:
        print(res + 1)
    elif k == 0:
        print(res)
    else:
        print(-1)
else:
    if n == 6 or n == 8:
        print(1)
    else:
        print(-1)