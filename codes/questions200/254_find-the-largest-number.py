#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 254_find-the-largest-number.py
@time: 2023/8/21 19:47
@project: huawei-od-python
@desc: 254 求最大数字
"""
from collections import defaultdict


def solve_method(nums):
    num_freq = defaultdict(int)
    for num in nums:
        num_freq[num] += 1

    # 从前向后依次删除元素，确保每个元素最多出现两次
    stack = []
    for num in nums:
        if stack and num_freq[stack[-1]] > 2 and stack[-1] < num:
            num_freq[stack[-1]] -= 1
            stack.pop()
        stack.append(num)

    # 从后向前依次删除元素，确保每个元素最多出现两次
    res = []
    while stack:
        if num_freq[stack[-1]] > 2:
            num_freq[stack[-1]] -= 1
            stack.pop()
        else:
            # 每次都将该数加入到最前面
            res.insert(0, stack.pop())
    return "".join(res)


if __name__ == "__main__":
    # 4533
    # input_str = input().strip()
    # nums = [c for c in input_str]
    # print(solve_method(nums))

    assert solve_method("34533") == "4533"
    assert solve_method("5445795045") == "5479504"
    assert solve_method("5554") == "554"
