#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 203_consecutive-letter-length.py
@time: 2023/7/20 14:05
@project: huawei-od-python
@desc: 203 连续字母长度、求第K长的字符串长度
"""

from collections import defaultdict


def solve_method(strings, k):
    pre_char = strings[0]
    # 字符字典，key为字母，value为同一字母连续出现的最大次数
    ch_freq = defaultdict(int)

    count = 0
    for ch in strings:
        if pre_char == ch:
            count += 1
        else:
            if pre_char in ch_freq:
                ch_freq[pre_char] = max(ch_freq[pre_char], count)
            else:
                ch_freq[pre_char] = count
            pre_char = ch
            count = 1

    # 按照出现次数排序
    ch_list = sorted(ch_freq.values(), reverse=True)
    if k > len(ch_list):
        return -1
    else:
        # 取出第k个字母的连续出现的次数
        return ch_list[k - 1]


if __name__ == '__main__':
    assert solve_method("AAAAHHHBBCDHHHH", 3) == 2
    assert solve_method("AABAAA", 2) == 1
    assert solve_method("ABC", 4) == -1
