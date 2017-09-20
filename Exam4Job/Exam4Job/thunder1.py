# -*- coding: utf-8 -*-
import re
def solve(eq, var = 'x'):
    eq1 = eq.replace('=', "-(")+")"
    c = eval(eq1, {var: 1j})
    return -c.real / c.imag

def pre(s):
    l = list(s)
    i = 1
    while i < len(l):
        if (l[i-1].isdigit() and l[i] == 'x') or (l[i-1].isdigit() and l[i] == '('):
            l.insert(i, '*')
            i+=1
        i += 1
    return "".join(l)

if __name__ == '__main__':
    s = input()
    print(solve(pre(s)))#2x+5-3+x=6+x-2