#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 042_words-chain.py
@time: 2023/7/27 11:06
@project: huawei-od-python
@desc: 042 单词接龙
"""


def solve_method(words, k):
    result = words[k]
    words.pop(k)
    words = sorted(words, key=lambda x: (-len(x), x))
    index = 0
    while words and index < len(words):
        # 判断是否为前一个单词的尾字母
        if words[index].startswith(result[-1]):
            result += words[index]
            words.pop(index)
            # 遍历的时候，确保从第一个单词开始遍历
            index = 0
        else:
            # 继续遍历
            index += 1
    return result


if __name__ == '__main__':
    words = ["word", "dd", "da", "dc", "dword", "d"]
    assert solve_method(words, 0) == "worddwordda"

    words = ["word", "dd", "da", "dc", "dword", "d"]
    assert solve_method(words, 4) == "dwordda"
