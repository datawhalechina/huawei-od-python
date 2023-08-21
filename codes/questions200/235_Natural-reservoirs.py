#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 235_Natural-reservoirs.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 235 天然蓄水池
"""

def solve_method(s):
    # 分别从左右两端向中间遍历，如果左端较低，则移动左端，如果右端较低，则移动右端
    left, right = 0, len(s) - 1
    max_area = 0
    max_i, max_j = 0, len(s) - 1

    while left < right - 1:
        area = 0
        for i in range(left + 1, right):
            area += min(s[left], s[right]) - s[i]
        if area >= max_area:
            max_area = area
            max_i, max_j = left, right
        
        if s[left] < s[right]:
            left += 1
        else:
            right -= 1

    if max_area == 0:
        return 0
    else:
        return (max_i, max_j, max_area)

if __name__ == '__main__':
    s = [3,1,2]
    assert solve_method(s) == (0, 2, 1)

    s = [3,2,1]
    assert solve_method(s) == 0

    s = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solve_method(s) == (1, 6, 15)

    s = [1, 9, 6, 2, 5, 4, 9, 3, 7]
    assert solve_method(s) == (1, 6, 19)