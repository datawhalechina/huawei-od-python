#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 009_gomoku-fans.py
@time: 2023/9/1 15:05
@project: huawei-od-python
@desc: 009 五子棋迷
"""


def solve_method(curr_piece, pieces):
    result = []

    def get_left_count(index):
        left = index - 1
        count = 0
        while left > -1 and pieces[left] == curr_piece:
            count += 1
            left -= 1

        return count

    def get_right_count(index):
        right = index + 1
        count = 0
        while right < len(pieces) and pieces[right] == curr_piece:
            count += 1
            right += 1

        return count

    for i, piece in enumerate(pieces):
        if piece != 0:
            continue

        left_count = get_left_count(i)
        right_count = get_right_count(i)
        total_count = left_count + right_count
        if total_count <= 5:
            result.append([i, total_count])

    # 按照长度从大到小，与中间的距离从小到大排序
    result.sort(key=lambda x: (-x[1], abs(x[0] - len(pieces) // 2)))

    return result[0][0]


if __name__ == '__main__':
    pieces = [-1, 0, 1, 1, 1, 0, 1, 0, 1, -1, 1]
    assert solve_method(1, pieces) == 5

    pieces = [-1, 0, 1, 1, 1, 0, 1, 0, 1, -1, 1]
    assert solve_method(-1, pieces) == 1

    pieces = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    assert solve_method(1, pieces) == 5
