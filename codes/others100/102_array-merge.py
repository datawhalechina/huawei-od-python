#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 102_array-merge.py
@time: 2023/7/25 15:56
@project: huawei-od-python
@desc: 102 数组合并
"""


def solve_method(k, arr):
    result = []
    index = 0
    while len(arr) > 0:
        num_list = arr[index]
        for i in range(k):
            if len(num_list) == 0:
                arr.pop(index)
                # 将位置指向前一个
                index -= 1
                break
            result.append(num_list.pop(0))
        # 由于前面删除了一行，index需要加1，继续回到这一行的位置
        index += 1
        if index >= len(arr):
            index = 0
    return result


if __name__ == '__main__':
    arr = [[2, 5, 6, 7, 9, 5, 7],
           [1, 7, 4, 3, 4]]
    assert solve_method(3, arr) == [2, 5, 6, 1, 7, 4, 7, 9, 5, 3, 4, 7]

    arr = [[1, 2, 3, 4, 5, 6],
           [1, 2, 3],
           [1, 2, 3, 4]]
    assert solve_method(4, arr) == [1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 5, 6]
