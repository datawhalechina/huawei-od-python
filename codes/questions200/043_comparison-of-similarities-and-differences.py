#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 043_comparison-of-similarities-and-differences.py
@time: 2023/8/22 18:46
@project: huawei-od-python
@desc: 043 统计差异值大于相似值二元组个数
"""


def solve_method(n, nums):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = nums[i] ^ nums[j]
            simi = nums[i] & nums[j]
            if diff > simi:
                count += 1
    return count


if __name__ == "__main__":
    # 4
    # 4 3 5 2
    # n = int(input().strip())
    # nums = list(map(int, input().strip().split()))
    # print(solve_method(n, nums))

    assert solve_method(4, [4, 3, 5, 2]) == 4
    assert solve_method(5, [3, 5, 2, 8, 4]) == 8
