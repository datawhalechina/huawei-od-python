#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 045_get-the-perfect-position.py
@time: 2023/8/3 14:11
@project: huawei-od-python
@desc: 045 获得完美走位
"""
import math
from collections import Counter


def check(changed_map):
    return all(map(lambda x: False if x > 0 else True, changed_map.values()))


def solve_method(ops):
    chars = {'A': 0, 'S': 0, 'W': 0, 'D': 0}
    length = len(ops)
    count = length // 4
    # 保留缺失的字符
    chars.update(dict(Counter(ops)))
    for k, v in chars.items():
        chars[k] = v - count

    result = math.inf
    for i in range(len(ops)):
        c1 = ops[i]
        res = 0
        changed = chars.copy()
        # 判断当前字符是否多出来
        if changed[c1] > 0:
            # 持续更换字符，统计更换次数
            for j in range(i, length):
                c2 = ops[j]
                changed[c2] -= 1
                res += 1
                # 检查所有的字符频数是否都为0
                if check(changed):
                    break
        if check(changed):
            result = min(result, res)

    return result


if __name__ == '__main__':
    assert solve_method("ASDW") == 0
    assert solve_method("AASW") == 1
    assert solve_method("AAAA") == 3
    assert solve_method("AAADDWWW") == 4
