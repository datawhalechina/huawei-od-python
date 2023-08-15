#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 172_the-letter-of-the-k-th-min-code-value.py
@time: 2023/8/8 22:53
@project: huawei-od-python
@desc: 172 第k个最小码值的字母
"""


def solve_method(s, k):
    # 从小到大按照码值排序
    sorted_chars = sorted(s)

    # k超过整个s的长度，则取最后一个字符即码值最大的
    c = sorted_chars[-1] if k >= len(sorted_chars) else sorted_chars[k - 1]
    return s.index(c)


if __name__ == '__main__':
    assert solve_method("AbCdeFG", 3) == 5
    assert solve_method("fAdDAkBbBq", 4) == 6
