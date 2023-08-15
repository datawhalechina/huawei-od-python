#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 165_relative-open-syllable.py
@time: 2023/8/8 22:03
@project: huawei-od-python
@desc: 165 相对开音节
"""
import re


def solve_method(line):
    # 空格分隔和反转
    s_list = list(map(lambda x: x[::-1] if x.isalpha() else x, line.split()))
    count = 0
    p = re.compile(r"[^aeiou][aeiou][^aeiour]e")
    for string in s_list:
        # 必须全部是字母，才符合要求
        if len(string) >= 4 and all([True if ch.isalpha() else False for ch in string]):
            for i in range(len(string) - 3):
                # 使用正则表达式判断是否满足条件
                result = p.search(string[i:i + 4])
                if result:
                    count += 1

    return count


if __name__ == '__main__':
    assert solve_method("ekam a ekac") == 2
    assert solve_method("!ekam a ekekac") == 2
