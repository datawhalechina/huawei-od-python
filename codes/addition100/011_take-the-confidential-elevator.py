#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 011_take-the-confidential-elevator.py
@time: 2023/9/1 16:55
@project: huawei-od-python
@desc: 011 乘坐保密电梯
"""


def solve_method(m, steps):
    result = []

    def backtracking(curr_floor, curr_direction, curr_sequence, sequence):
        seq = sequence.copy()

        if len(seq) == 0:
            # 当所有序列都已经操作完毕
            if curr_floor <= m:
                # 当到达的楼层小于等于目标楼层
                result.append((curr_sequence.copy(), curr_floor))
            return

        for i in range(len(seq)):
            curr_sequence.append(seq[i])
            next_floor = curr_floor + seq[i] if curr_direction else curr_floor - seq[i]
            # 操作方向相反
            next_direction = not curr_direction
            num = seq.pop(i)
            backtracking(next_floor, next_direction, curr_sequence, seq)
            # 回溯
            seq.insert(i, num)
            curr_sequence.remove(seq[i])

    backtracking(0, True, [], steps)

    # 按照楼层从大到小、操作数字从大到小排序
    result.sort(key=lambda x: (-x[1], -x[0][0]))
    return result[0][0]


if __name__ == '__main__':
    assert solve_method(5, [1, 2, 6]) == [6, 2, 1]
