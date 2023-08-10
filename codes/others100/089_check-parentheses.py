#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 089_check-parentheses.py
@time: 2023/8/10 16:33
@project: huawei-od-python
@desc: 089 括号检查
"""


def solve_method(string):
    string = list(string)
    depth = 0
    stack = []

    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in string:
        if char in ["(", "[", "{"]:
            stack.append(char)
            depth = max(depth, len(stack))
        elif char in [")", "]", "}"]:
            if len(stack) == 0:
                return 0
            if stack[-1] == pares.get(char):
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return depth
    else:
        return 0


if __name__ == '__main__':
    assert solve_method("[]") == 1
    assert solve_method("([]{()})") == 3
    assert solve_method("(]") == 0
    assert solve_method("([)]") == 0
    assert solve_method(")(") == 0
