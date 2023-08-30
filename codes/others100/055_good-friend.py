#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 055_good-friend.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 055 好朋友
"""


def solve_method(n, heights):
    result = []

    for i in range(n):
        pos = 0
        for j in range(i + 1, n):
            if heights[j] > heights[i]:
                # 将找到的第一个更大的数的位置存入列表中
                pos = j
                break

        result.append(pos)

    return result


if __name__ == "__main__":
    assert solve_method(2, [100, 95]) == [0, 0]
    assert solve_method(8, [123, 124, 125, 121, 119, 122, 126, 123]) == [1, 2, 6, 5, 5, 6, 0, 0]
