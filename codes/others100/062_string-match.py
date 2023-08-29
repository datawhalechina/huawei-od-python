#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 062_string-match
@time:  2023/8/14 23:39
@project:  huawei-od-python
@desc: 062 字符匹配
"""


def solve_method(arr, pattern):
    def check(chars):
        i = 0
        chars = list(chars)
        prev = chars[0]
        while i < len(pattern):
            if len(chars) == 0:
                break
            if pattern[i] == ".":
                chars.pop(0)
                prev = "."
            elif pattern[i] == "*":
                # 如果连续相同字符，或者前一个字符是点号，则一直删除，直到不满足条件
                while len(chars) != 0 and (prev in [chars[0], "."]):
                    chars.pop(0)
            else:
                if chars[0] == pattern[i]:
                    # 如果是单个字符，则保存该字符作为后续字符匹配
                    prev = chars.pop(0)
                else:
                    return False
            i += 1

        if len(chars) == 0 and i == len(pattern):
            return True

        return False

    result = []
    for index, s in enumerate(arr):
        if check(s):
            result.append(index)
    return result


if __name__ == '__main__':
    arr = ["ab", "aab", "abacd"]
    assert solve_method(arr, ".*") == [0, 1, 2]

    arr = ["ab", "aab"]
    assert solve_method(arr, "a.b") == [1]

    arr = ["bab", "baaa"]
    assert solve_method(arr, "ba*") == [1]
