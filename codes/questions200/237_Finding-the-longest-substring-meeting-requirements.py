#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 237_Finding-the-longest-substring-meeting-requirements.py
@time: 2023/7/30
@project: huawei-od-python
@desc: 237 寻找符合要求的最长子串
"""

def solve_method(c, s):
    l = 0
    result = 0
    d = {}

    for i in range(len(s)):
        temp = s[i]
        if temp == c:
            d.clear()
            l = i + 1
            continue

        # 记录当前字符的出现次数
        d[temp] = d.get(temp, 0) + 1

        # 当前字符出现次数超出2次, 找到第一个出现的位置的下一个位置作为起点l
        while d[temp] == 3:
            rmChar = s[l]
            l += 1
            d[rmChar] -= 1

        # 更新结果, 记录符合条件的子串长度的最大值
        result = max(result, i - l + 1)

    return result

if __name__ == '__main__':
    assert solve_method('D',"ABC123") == 6
    assert solve_method('D',"ABACD1231") == 4