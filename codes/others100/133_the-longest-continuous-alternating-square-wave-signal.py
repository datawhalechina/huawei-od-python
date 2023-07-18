#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 133_the-longest-continuous-alternating-square-wave-signal.py
@time: 2023/7/18 22:02
@project: huawei-od-python
@desc: 133 最长连续交替方波信号
"""
import re


def solve_method(line):
    result = []
    # 设置正则表达式
    p = re.compile("0(10)+")
    pos = 0
    while pos < len(line):
        # 使用正则表达式查找
        m = p.search(line, pos)
        # 记录字符串位置
        pos = m.span()[1]
        # 保存子串
        result.append(m.group())
    # 按照子串长度从大到小排序
    result.sort(key=lambda x: len(x), reverse=True)
    # 如果存在，返回最大长度，如果不存在，返回-1
    return result[0] if len(result) != 0 else -1


if __name__ == '__main__':
    assert solve_method("0010101010110000101000010") == "010101010"
