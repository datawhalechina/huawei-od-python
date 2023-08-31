#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jack Lee C.S.
@file: 028_maximum-number-of-substrings-extracted.py
@time: 2023/07/12 10:59
@project: huawei-od-python
@desc: 028 最多提取子串数目
"""


def solve_method(A: str, B: str) -> int:
    result = 0
    # 标记A的字母是否被使用
    exist = [True for _ in range(len(A))]
    # 是否已经找到了一个字符串B
    flag = True
    while flag:
        flag = False
        ib = 0
        for ia in range(len(A)):

            if exist[ia]:
                # 如果A中的字母没有被使用，与B中的字母匹配
                if A[ia] == B[ib]:
                    ib += 1
                    # 标记A中的字母已经被使用
                    exist[ia] = False
                ia += 1

            if ib == len(B):
                # 如果找到了一个字符串B，统计次数
                result += 1
                flag = True
                break
    return result


if __name__ == '__main__':
    assert solve_method("badc", "bac") == 1
    assert solve_method("badc", "abc") == 0
    assert solve_method("aabbcxd", "abcd") == 1
    assert solve_method("ababcecfdc", "abc") == 2
    assert solve_method("aaa", "a") == 3
