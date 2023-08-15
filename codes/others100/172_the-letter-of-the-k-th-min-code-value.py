#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 172_the-letter-of-the-k-th-min-code-value.py
@time: 2023/8/8 22:53
@project: huawei-od-python
@desc: 172 第k个最小码值的字母
"""


def solve_method(k, s):
    # 从小到大按照码值排序
    sort_alpha = sorted(s)
    n = len(s)

    # k超过整个s的长度，则取最后一个字符即码值最大的
    if n<=k-1:
        return s.index(sort_alpha[-1])
    else:
        return s.index(sort_alpha[k-1])

if __name__ == '__main__':
    assert solve_method(3, "AbCdeFG") == 5
    assert solve_method(4, "fAdDAkBbBq") == 6
