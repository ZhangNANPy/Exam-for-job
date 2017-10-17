# -*- coding: utf-8 -*-
'''
输入一个字符串，字符串内全是0和1，
找出这个串最长的连续的0和1个数相等的子串。输出子串的长度。
例如输入“00000010001”，满足条件的子串是“01”，长度为2，输出2.
'''

def equalSubString(s):
    '''
    使用额外的空间，counter记录字符串中0和1个数的差，
    history记录差是否出现过，利用个数差相等找见子串。
    若个数差未出现过，则插入history中，否则和当前最长子串比较，
    考虑更新结果。
    '''
    counter = [0 for i in range(len(s) + 1)]
    history = {}
    res = 0
    for i in range(len(s)):
        if s[i] == '1':
            counter[i+1] = counter[i] + 1
        else:
            counter[i+1] = counter[i] - 1
        if counter[i+1] in history.keys():
            if i - history[counter[i+1]] > res:
                res = i - history[counter[i+1]]
        else:
            history[counter[i+1]] = i
    return res

if __name__ == '__main__':
    print(equalSubString(input()))