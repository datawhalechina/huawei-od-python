#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 019_finding-the-longest-substring-meeting-requirements.py
@time: 2023/7/30
@project: huawei-od-python
@desc: 019 寻找符合要求的最长子串
"""
from collections import Counter


def solve_method(ch, chars):
    chars_lst = chars.split(ch)

    result = []
    for sub_chars in chars_lst:
        counter = Counter(sub_chars)
        # 判断子串的任意字符最多出现2次
        if all([True if v <= 2 else False for k, v in counter.items()]):
            result.append(sub_chars)

    # 将满足条件的子串按照子串长度从大到小排序
    result.sort(key=lambda x: len(x), reverse=True)
    # 返回最长的子串
    return len(result[0]) if len(result) != 0 else 0


if __name__ == '__main__':
    assert solve_method('D', "ABC123") == 6
    assert solve_method('D', "ABACABD12321") == 5
