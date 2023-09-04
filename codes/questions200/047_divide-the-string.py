#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 047_divide-the-string.py
@time: 2023/9/3 23:18
@project: huawei-od-python
@desc: 047 划分字符串
"""


def solve_method(s):
    n = len(s)
    left, right = 1, n - 2
    sum_total = sum(ord(c) for c in s)
    sum_left = ord(s[0])
    sum_right = ord(s[n - 1])
    while left < right:
        sum_middle = sum_total - sum_left - sum_right - ord(s[left]) - ord(s[right])
        if sum_left == sum_middle == sum_right:
            return f"{left},{right}"
        if sum_left > sum_right:
            sum_right += ord(s[right])
            right -= 1
        elif sum_left < sum_right:
            sum_left += ord(s[left])
            left += 1
        else:
            sum_left += ord(s[left])
            sum_right += ord(s[right])
            left += 1
            right -= 1
    return "0,0"


if __name__ == '__main__':
    assert solve_method("acdbbbca") == "2,5"
    assert solve_method("abcabc") == "0,0"
