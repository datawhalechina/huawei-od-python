#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 274_symmetric-string.py
@time: 2023/7/13 18:55
@project: huawei-od-python
@desc: 274 对称美学
"""


def get_color(n, k):
    if n == 1:
        return "R"
    elif n == 2:
        return "B" if k == 0 else "R"

    half_len = 2 ** (n - 1)
    if k >= half_len:
        # 在后半段，要查找的位置等于上一个字符串的相应位置
        prev_pos = k - half_len
        return get_color(n - 1, prev_pos)
    else:
        # 在前半段，要查找的位置等于上一个字符串的相应位置取反
        return "B" if get_color(n - 1, k) == "R" else "R"


def solve_method(T):
    color_map = {"R": "red", "B": "blue"}
    result = []
    for t in T:
        n, k = t[0], t[1]
        # 将R转换成red，将B转换成blue
        result.append(color_map[get_color(n, k)])

    return result


if __name__ == '__main__':
    T = [[1, 0],
         [2, 1],
         [3, 2],
         [4, 6],
         [5, 8]]
    assert solve_method(T) == ["red", "red", "blue", "blue", "blue"]
    T = [[64, 73709551616]]
    assert solve_method(T) == ["red"]
