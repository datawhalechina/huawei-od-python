#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 155_martian_compute.py
@time: 2023/8/29 14:20
@project: huawei-od-python
@desc: 155 火星文计算
"""
import re


def sharp(x, y):
    return 4 * x + 3 * y + 2


def dollar(x, y):
    return 2 * x + y + 3


def solve_method(line):
    # 将数字和操作符存储在列表中
    chars = re.findall(r"(\d+)|([#$])", line)
    chars = [match[0] or match[1] for match in chars]
    chars = [int(x) if x.isdigit() else x for x in chars]

    while len(chars) != 1:
        pos = chars.index("#") if "#" in chars else -1
        if pos != -1:
            # 优先计算#操作
            tmp = sharp(chars[pos - 1], chars[pos + 1])
            chars[pos - 1:pos + 2] = [tmp]
        else:
            pos = chars.index("$") if "$" in chars else -1
            if pos != -1:
                # 再计算$操作
                tmp = dollar(chars[pos - 1], chars[pos + 1])
                chars[pos - 1:pos + 2] = [tmp]

    return chars[0]


if __name__ == '__main__':
    assert solve_method("7#6$5#12") == 157
