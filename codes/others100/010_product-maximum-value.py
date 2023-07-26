#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 010_product-maximum-value.py
@time: 2023/7/26 17:09
@project: huawei-od-python
@desc: 010 乘积最大值
"""


def solve_method(strings):
    max_value = 0
    for i in range(len(strings)):
        for j in range(i, len(strings)):
            set_a = set(strings[i])
            set_b = set(strings[j])
            # 判断set集合合并的长度是否等于各集合的长度和，如果等于，则表示没有相同字符
            if len(set_a.union(set_b)) == len(set_a) + len(set_b):
                max_value = max(max_value, len(set_a) * len(set_b))

    return max_value


if __name__ == '__main__':
    assert solve_method(["iwdvpbn", "hk", "iuop", "iikd", "kadgpf"]) == 14
