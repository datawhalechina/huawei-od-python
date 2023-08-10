#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 084_find-the-minimum-number.py
@time: 2023/8/9 20:55
@project: huawei-od-python
@desc: 084 找最小数
"""


def solve_method(num, n):
    nums = list(str(num))
    # 使用栈来存储数字
    stack = []
    # 表示需要移除的数字个数
    removed = 0

    for digit in nums:
        # 如果栈顶的数字大于当前数字且还有剩余的移除次数，则弹出栈顶数字
        while stack and removed < n and stack[-1] > digit:
            stack.pop()
            removed += 1
        stack.append(digit)

    # 如果还有剩余的数字需要移除
    while removed < n:
        stack.pop()
        removed += 1

    # 构建最终的结果
    return int("".join(stack))


if __name__ == '__main__':
    assert solve_method(2615371, 4) == 131
    assert solve_method(123456, 4) == 12
