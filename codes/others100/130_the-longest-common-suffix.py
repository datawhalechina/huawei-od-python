#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 130_the-longest-common-suffix.py
@time: 2023/7/18 20:11
@project: huawei-od-python
@desc: 130 最长公共后缀
"""


def solve_method(arr):
    pre = arr[0]
    for i in range(1, len(arr)):
        cur = arr[i]
        # 记录重复的字符位置
        j = 1
        # 从后往前对比两个字符串
        while j <= min(len(pre), len(cur)) and pre[-j] == cur[-j]:
            j += 1
        if j == 1:
            pre = "@Zero"
            break

        # 取出公共后缀
        pre = pre[-j + 1:]

    return pre


if __name__ == '__main__':
    assert solve_method(["abc", "bbc", "c"]) == "c"
    assert solve_method(["aa", "bb", "cc"]) == "@Zero"
