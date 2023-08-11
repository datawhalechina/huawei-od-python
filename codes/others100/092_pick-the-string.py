#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 092_pick-the-string.py
@time: 2023/8/11 16:12
@project: huawei-od-python
@desc: 092 挑选字符串
"""


def solve_method(a, b):
    count = 0
    while True:
        chars = list(b)
        # 设置遍历索引
        pos = 0
        for ch in chars:
            # 找到了字符串b中的一个字符
            index = a.find(ch, pos)
            if index != -1:
                # 如果找到了，那就用`_`替换掉
                a = a.replace(ch, "_", 1)
                # 把找到的位置设置给索引
                pos = index
            else:
                return count
        # 找到一个，累计加1
        count += 1


if __name__ == '__main__':
    assert solve_method("badc", "bac") == 1
    assert solve_method("badc", "abc") == 0
    assert solve_method("abacc", "abc") == 1
    assert solve_method("abcabc", "abc") == 2
