#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 025_push-and-pop.py
@time: 2023/8/7 14:46
@project: huawei-od-python
@desc: 025 入栈出栈
"""


def solve_method(nums):
    stack = []

    for num in nums:
        # 标识是否重新入栈新元素
        changed = False
        if stack:
            i = n = len(stack) - 1

            while i > -1:
                # 当满足条件时，出栈相应元素，入栈新元素
                if sum(stack[i:n + 1]) == num:
                    del stack[i:n + 1]
                    stack.insert(i, num * 2)
                    changed = True
                    break
                i -= 1
        if not changed:
            stack.append(num)

    return stack[::-1]


if __name__ == '__main__':
    nums = [5, 10, 20, 50, 85, 1]
    assert solve_method(nums) == [1, 170]

    nums = [6, 7, 8, 13, 9]
    assert solve_method(nums) == [9, 13, 8, 7, 6]

    nums = [1, 2, 5, 7, 9, 1, 2, 2]
    assert solve_method(nums) == [4, 1, 9, 14, 1]
