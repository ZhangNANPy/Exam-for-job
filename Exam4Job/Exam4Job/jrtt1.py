# -*- coding: utf-8 -*-

(n, m, c) = map(int, list(input().split()))
col = []
for i in range(n):
    temp = [int(j) for j in input().split()]
    if temp[0] == 0:
        col.append(set())
    else:
        col.append(set(temp[1:]))

def ring(n, m, c, cl):
    us = set(cl[0])
    re = 0
    for i in range(1, m):
        re += len(us & cl[i])
        us = us | cl[i]
    for i in range(1, n):
        us = us - cl[i - 1]
        re += len(us & cl[(i + m - 1) % n])
        us = us | cl[(i + m - 1) % n]
    return re

if __name__ == '__main__':
    print(ring(n,m,c,col))