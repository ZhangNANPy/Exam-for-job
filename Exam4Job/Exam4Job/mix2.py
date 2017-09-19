# -*- coding: utf-8 -*-

def YH(n):
    if n == 1:
        return 0
    i = 1
    while True:#控制行
        up = 1
        down = 1
        i += 1
        for j in range(1, int((i + 1) / 2 + 1)):
            up = up * (i - j + 1)
            down = down * j
            temp = int(up / down)
            if n == temp:
                return i
            elif n < temp:
                break

if __name__ == "__main__":
    n = int(input())
    print(YH(n))