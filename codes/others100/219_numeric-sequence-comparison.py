#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 219_numeric-sequence-comparison.py
@time: 2023/9/4 11:12
@project: huawei-od-python
@desc: 005 数字序列比大小
"""


def solve_method(A, B):
    # 对列表A和B按照从小到大排序
    A.sort()
    B.sort()

    result = 0
    # 遍历列表 A 中的元素
    for i in range(len(A)):
        numA = A[i]
        # 判断当前元素 numA 与列表 B 的第一个元素的大小关系
        if numA < B[0]:
            # 让当前元素与列表B的最大元素比较，输1分。
            result -= 1
            B.pop()
        else:
            # 如果大于，则赢1分，如果相等，则不加分
            result += 1 if numA > B[0] else 0
            B.pop(0)

    return result


if __name__ == '__main__':
    assert solve_method([4, 8, 10], [3, 6, 4]) == 3
