#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 075_recover-array
@time:  2023/8/24 17:04
@project:  huawei-od-python
@desc: 075 恢复数字序列
"""
from collections import Counter


def solve_method(s, n):
    counter = Counter(s)
    candidate = [val for val in range(n)]
    candidate_counter = Counter(''.join(map(str, candidate)))
    for new in range(n, 1001):
        if candidate_counter == counter:
            return candidate[0]
        else:
            prev = candidate.pop(0)
            candidate_counter -= Counter(str(prev))

            candidate.append(new)
            candidate_counter += Counter(str(new))
    return -1


if __name__ == '__main__':
    assert solve_method("19801211", 5) == 8
    assert solve_method("432111111111", 4) == 111
