# -*- coding: utf-8 -*-
def tencent1(n):
    flag = '1'
    p = 0
    tempList = [0,0]
    res = 1
    for i in range(len(n)):
        if n[i] == flag:
                tempList[p] += 1
        else:
            if flag == '0':
                flag = '1'
                p = 0
                res *= (tempList[0] * tempList[1] + 1)
            else:
                p = 1
                flag = '0'
            tempList[p] = 1
    if n[i] == '0':  #结尾是1的话，最后一组有效数据和res相乘过，是0的话没有，则需要此补偿
        res *= (tempList[0] * tempList[1] + 1)
    return res

if __name__ == '__main__':
    n = str(bin(int(input(), 10)))[2:]
    print(tencent1(n))