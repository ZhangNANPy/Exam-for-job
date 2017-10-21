# -*- coding: utf-8 -*-
def fun(n):
    sum = 0
    while n > 0:
        sum += n*n - (n - 1)*(n - 1)
        n -= 4
    return sum

if __name__ == '__main__':
    print(fun(30))