#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 057_letter-elimination.py
@time: 2023/08/14 21:00
@project: huawei-od-python
@desc: 057 字母消消乐
"""


def solve_method(chars):
    # 仅保留字母
    lst = [c for c in chars if c.isalpha()]

    if len(lst) == 0:
        # 如果列表中没有字母，则是异常输入，返回0
        return 0

    i = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            # 当前字符与后一个字符相同时，则删除重复项
            del lst[i:i + 2]
            # 位置倒退一个
            i = max(0, i - 1)
        else:
            i += 1
    return len(lst)


if __name__ == '__main__':
    assert solve_method("gg") == 0
    assert solve_method("mMbccbc") == 3
