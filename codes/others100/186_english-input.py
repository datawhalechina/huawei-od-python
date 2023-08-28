#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 186_english-input.py
@time: 2023/8/27 1:29
@project: huawei-od-python
@desc: 186 英文输入法
"""
import re


def solve_method(line, pre):
    words = re.findall(r'\w+', line)
    word_set = set(words)

    result = []

    for word in word_set:
        if word.startswith(pre):
            result.append(word)
    if not result:
        result.append(pre)

    result.sort()
    return " ".join(result)


if __name__ == '__main__':
    assert solve_method("I love you", "He") == "He"

    line = """The furthest distance in the world,
              Is not between life and death,
              But when I stand in front or you,
              Yet you don't know that I love you. """
    assert solve_method(line, "f") == "front furthest"
