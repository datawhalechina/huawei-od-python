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


def is_same_dict(d1, d2):
    for key in d1:
        if key not in d2 or d1[key] != d2[key]:
            return False
    for key in d2:
        if key not in d1 or d1[key] != d2[key]:
            return False
    return True


def solve_method(s, n):
    counter = dict(Counter(s))
    candidate = [val for val in range(n)]
    candidate_counter = dict(Counter(''.join(map(str, candidate))))
    for new in range(n, 1001):
        if is_same_dict(candidate_counter, counter):
            return candidate[0]
        else:
            prev = candidate.pop(0)
            for key in str(prev):
                candidate_counter[key] -= 1
                if candidate_counter[key] == 0:
                    candidate_counter.pop(key)

            candidate.append(new)
            for key in str(new):
                if key not in candidate_counter:
                    candidate_counter[key] = 1
                else:
                    candidate_counter[key] += 1
    return -1


if __name__ == '__main__':
    s, n = input().strip().split(' ')
    n = int(n)
    res = solve_method(s, n)
    print(res)
