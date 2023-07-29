#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhangChao
@file: 041_reverse-wordsv2.py
@time: 2023/7/29 18:27
@project: huawei-od-python
@desc: 041 单词反转2
"""


def solve_method(line, start, end):
    words = line.strip().split(" ")
    if start > end or start > len(line) -1 or end <0:
        return line.strip()
    # 提取区域内的字符串并反转
    sub_words = words[start:end + 1]
    sub_words.reverse()
    # 合并字符串数组并输出
    if end + 1 < len(words):
        result = words[:start] + sub_words + words[end + 1:]
    else:
        result = words[:start] + sub_words

    return " ".join(result)


if __name__ == '__main__':
    assert solve_method("I am a developer.", 0, 3) == "developer. a am I"
    assert solve_method("hello world!", 0, 3) == "world! hello"
    assert solve_method("I am a developer", 1, 2) == "I a am developer"
    assert solve_method("hello world", -1, 1) == "hello world"
