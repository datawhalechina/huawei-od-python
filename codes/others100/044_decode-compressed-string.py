#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 044_decode-compressed-string.py
@time: 2023/7/27 14:04
@project: huawei-od-python
@desc: 044 压缩报文还原
"""


def solve_method(string):
    prev, current = "", ""
    stack = []
    num = 0
    for i in range(len(string)):
        if string[i].isdigit():
            num = num * 10 + int(string[i])
        elif string[i] == "[":
            stack.append(current)
            stack.append(num)
            current = ""
            num = 0
        elif string[i] == "]":
            curr_num = stack.pop()
            prev = stack.pop()
            current = prev + curr_num * current
        else:
            current += string[i]

    return current


if __name__ == '__main__':
    assert solve_method("3[k]2[mn]") == "kkkmnmn"
    assert solve_method("3[m2[c]]") == "mccmccmcc"
