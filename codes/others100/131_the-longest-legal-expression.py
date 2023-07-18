#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 131_the-longest-legal-expression.py
@time: 2023/7/18 21:02
@project: huawei-od-python
@desc: 131 最长合法表达式
"""
import re


def check_valid(expression):
    p = re.compile("^([0-9]+([+\\-*/][0-9]+)+)$")
    return p.match(expression)


def solve_method(line):
    SAMPLE_OPS = "0123456789+-*/"

    nums = []
    for i in range(len(line)):
        if line[i].isdigit():
            start = i
            # 确定满足简单数学表达式的连续字符
            while i + 1 < len(line) and line[i + 1] in SAMPLE_OPS:
                i += 1

            expression = line[start: i + 1]
            # 验证字符串是否为合法数学表达式
            if check_valid(expression):
                nums.append(expression)

    # 按照表达式长度进行排序
    nums.sort(key=lambda x: len(x), reverse=True)
    if nums:
        # 计算表达式的值
        return eval(nums[0])
    else:
        return 0


if __name__ == '__main__':
    assert solve_method("1-2abcd") == -1
