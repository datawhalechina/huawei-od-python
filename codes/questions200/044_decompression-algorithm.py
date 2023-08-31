#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 044_decompression-algorithm.py
@time: 2023/8/22 19:11
@project: huawei-od-python
@desc: 044 解压缩算法
"""


def solve_method(chars):
    chars += "#"
    stack = []
    num, temp = 0, ""
    for c in chars:
        if c.isdigit():
            num = num * 10 + int(c)
            continue
        if num != 0:
            # 数字统计结束，进行计算
            # 此时栈肯定非空，且栈顶元素为字母或}
            if stack[-1].isalpha():
                stack[-1] = stack[-1] * num
            elif stack[-1] == "}":
                # 弹出}
                stack.pop()
                while stack[-1] != "{":
                    temp = stack.pop() + temp
                # 弹出{，并保存解压后的字符串
                stack[-1] = temp * num
            num, temp = 0, ""
        stack.append(c)

    return "".join(stack[:-1])


if __name__ == "__main__":
    # {A3B1{C}3}3
    # string = input().strip()
    # print(solve_method(string))

    assert solve_method("{A3B1{C}3}3") == "AAABCCCAAABCCCAAABCCC"
    assert solve_method("A3") == "AAA"
    assert solve_method("{AD11B1{CF}3}3") == "ADDDDDDDDDDDBCFCFCFADDDDDDDDDDDBCFCFCFADDDDDDDDDDDBCFCFCF"
