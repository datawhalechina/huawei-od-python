#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 058_letter-combination.py
@time: 2023/08/14 21:00
@project: huawei-od-python
@desc: 058 字母组合
"""

import itertools

# 定义数字到字母的映射
digits_mapping = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"],
    ["p", "q", "r"],
    ["s", "t"],
    ["u", "v"],
    ["w", "x"],
    ["y", "z"]
]


def solve_method(nums, block_words):
    nums = list(nums)
    words = [set(digits_mapping[int(num)]) for num in nums]
    # 得到各列表之间的笛卡尔积
    result = list(itertools.product(*words))

    result = ["".join(x) for x in result if block_words not in "".join(x)]
    result.sort()
    return result


if __name__ == "__main__":
    assert solve_method("78", "ux") == ["uw", "vw", "vx"]
    assert solve_method("78", "x") == ["uw", "vw"]
