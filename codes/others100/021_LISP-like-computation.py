#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 021_LISP-like-computation.py
@time: 2023/8/7 10:43
@project: huawei-od-python
@desc: 021 仿LISP运算
"""
import math


def solve_method(ops):
    # 用于存储操作数和操作符的栈
    stack = list()
    res = 0
    num_str, op_word = "", ""

    for ch in ops:
        if ch == "(":
            # 如果是左括号，直接压入栈中
            stack.append(ch)
        elif ch.isalpha():
            op_word += ch
        elif ch.isnumeric() or ch in ["-", "."]:
            num_str += ch
        elif ch.isspace() or ch == ")":
            if num_str != "":
                stack.append(int(num_str))
                num_str = ""
            if op_word != "":
                stack.append(op_word)
                op_word = ""

        if ch == ")":
            # 如果是右括号，取出栈顶的两个数和操作符进行计算，并将结果压入栈中
            num2 = stack.pop()
            num1 = stack.pop()
            op = stack.pop()
            stack.pop()

            if op == "add":
                res = num1 + num2
            elif op == "sub":
                res = num1 - num2
            elif op == "mul":
                res = num1 * num2
            elif op == "div":
                if num2 == 0:
                    # 如果除法操作的除数为0，返回error
                    return "error"
                res = math.floor(num1 / num2)

            # 将计算结果压入栈中
            stack.append(res)

    return stack[0]


if __name__ == '__main__':
    assert solve_method("(div 12 (sub 45 45))") == "error"
    assert solve_method("(add 1 (div -7 3))") == -2
