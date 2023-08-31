#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 008_find-duplicate-codes.py
@time: 2023/7/12 20:24
@project: huawei-od-python
@desc: 008 找出重复代码（最长公共子序列）
"""


def solve_method(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    end = 0
    max_length = 0
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # 获取最大长度
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end = i - 1
    # 返回最长公共子串
    return text1[end - max_length + 1: end + 1]


if __name__ == '__main__':
    assert solve_method("hello123world", "hello123abc4") == "hello123"
    assert solve_method("private_void_method", "public_void_method") == "_void_method"
    assert solve_method("hiworld", "hiweb") == "hiw"
