# encoding: utf-8
"""
@author: Yalin Feng
@file: 142_dictionary-reference.py
@time: 2023/8/8 2:00
@project: huawei-od-python
@desc: 142 查字典
"""

from typing import List


def solve_method(prefix: str, length: int, words: List[str]):
    # 空列表results，存储与前缀相匹配的单词
    results = []

    for word in words:
        # 判断字符串的前缀是否与给定的前缀相同,如果相同，将该字符串添加到results列表中
        if word.startswith(prefix):
            results.append(word)

    return results if results else -1


if __name__ == '__main__':
    assert solve_method("b", 3, ["a", "b", "c"]) == ["b"]
    assert solve_method("abc", 4, ["a", "ab", "abc", "abcd"]) == ["abc", "abcd"]
    assert solve_method("a", 3, ["b", "c", "d"]) == -1
