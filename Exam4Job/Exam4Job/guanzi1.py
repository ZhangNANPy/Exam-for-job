# -*- coding: utf-8 -*-
import itertools
a = set([i for i in range(1, 15)])
counter = 0
q = list(itertools.combinations(a, 7))
print(q)
for i in q:
    i = set(i)
    j = a - i
    i = sorted(list(i))
    j = sorted(list(j))
    flag = True
    for k in range(7):
        if i[k] > j[k]:
            flag = False
    if flag:
        counter += 1
print(counter)