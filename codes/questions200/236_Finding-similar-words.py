#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 236_Finding-similar-words.py
@time: 2023/8/19
@project: huawei-od-python
@desc: 236 寻找相似单词
"""

def is_similar(word1, word2):
    if len(word1) != len(word2):
        return False

    count = [0] * 52
    for c1, c2 in zip(word1, word2):
        if 'A' <= c1 <= 'Z':
            count[ord(c1) - ord('A')] += 1
        else:
            count[ord(c1) - ord('a') + 26] += 1

        if 'A' <= c2 <= 'Z':
            count[ord(c2) - ord('A')] -= 1
        else:
            count[ord(c2) - ord('a') + 26] -= 1

    for c in count:
        if c != 0:
            return False

    return True

def solve_method(words, target_word):
    result = []
    for word in words:
        if is_similar(word, target_word):
            result.append(word)

    return result

if __name__ == '__main__':
    words = ["abc", "dasd", "tad", "bca"]
    assert solve_method(words, "abc") == ["abc", "bca"]

    assert solve_method(words, "abd") == []