#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 014_five-key-keyboard.py
@time: 2023/7/26 19:58
@project: huawei-od-python
@desc: 014 五键键盘
"""


def clear(result, select):
    if select != "":
        result = result.replace(select, "")
        select = ""
    return select, result


def solve_method(ops):
    result = ""
    select = ""
    copy = ""
    for op in ops:
        if op == 1:
            select, result = clear(result, select)
            result += "A"
        elif op == 2:
            if select != "":
                copy = select
        elif op == 3:
            if select != "":
                copy = select
                select = ""
                result = result.replace(select, "")
                select = ""
        elif op == 4:
            select, result = clear(result, select)
            result += copy
        elif op == 5:
            if result != "":
                select = result

    return len(result)


if __name__ == '__main__':
    assert solve_method([1, 1, 1]) == 3
    assert solve_method([1, 1, 5, 1, 5, 2, 4, 4]) == 2
