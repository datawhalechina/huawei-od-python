#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 098_the-arrangement-of-numbers.py
@time: 2023/8/11 21:15
@project: huawei-od-python
@desc: 098 数字的排列
"""
from collections import deque


def solve_method(n):
    asc_order = True
    nums_list = deque()
    x = 1
    # 计算每一行的数字及数字的排序
    for i in range(1, n + 1):
        arr = [0] * i
        if asc_order:
            for j in range(i):
                arr[j] = x
                x += 1
        else:
            for j in range(i - 1, -1, -1):
                arr[j] = x
                x += 1
        nums_list.appendleft(arr)
        asc_order = not asc_order

    # 得到每一个数的展现样式，及每一行的字符串
    result = []
    head = ""
    for nums in nums_list:
        content = head
        num_strs = []
        for j in range(len(nums)):
            num = nums[j]
            num_str = str(num) + "*" * (4 - len(str(num)))
            num_strs.append(num_str)

        result.append(content + "    ".join(num_strs))
        head += "    "

    # 逆序输出结果
    return result[::-1]


if __name__ == '__main__':
    assert solve_method(2) == ["    1***", "3***    2***"]
