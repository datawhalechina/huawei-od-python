#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 001_divide-the-string.py
@time: 2023/9/3 23:18
@project: huawei-od-python
@desc: 001 划分字符串
"""
def solve_method(s):
    n = len(s)
    i, j = 1, n - 2
    summ = sum(ord(c) for c in s)
    summ1 = ord(s[0])
    summ3 = ord(s[n - 1])
    while i < j:
        summ2 = summ - summ1 - summ3 - ord(s[i]) - ord(s[j])
        if summ1 == summ2 == summ3:
            return f"{i},{j}"
        if summ1 > summ3:
            summ3 += ord(s[j])
            j -= 1
        elif summ1 < summ3:
            summ1 += ord(s[i])
            i += 1
        else:
            summ1 += ord(s[i])
            summ3 += ord(s[j])
            i += 1
            j -= 1
    return "0,0"

if __name__ == '__main__':
    assert solve_method("acdbbbca") == "2,5"
    assert solve_method("abcabc") == "0,0"