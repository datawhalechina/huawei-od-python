#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 006_the-MELON-conundrum.py
@time: 2023/9/1 8:54
@project: huawei-od-python
@desc: 006 MELON的难题
"""


def remove_elements(arr, sub_arr):
    result_array = arr.copy()

    for elem in sub_arr:
        if elem in result_array:
            result_array.remove(elem)

    return result_array


def solve_method(n, nums):
    total = sum(nums)
    if total % 2 != 0:
        return -1

    target_sum = total // 2
    sub_lst = []
    result = []

    def backtrack(index, curr_sum):
        if curr_sum == target_sum:
            # 得到另一个子序列
            other_lst = remove_elements(nums, sub_lst[:])
            # 如果另一个子序列之和也等于数组之和的一半，则存入结果列表中
            if target_sum == sum(other_lst) and sub_lst[:] not in result:
                result.append(sub_lst[:])
                return
        if curr_sum > target_sum or index >= n:
            return

        for i in range(index, n):
            sub_lst.append(nums[i])
            backtrack(i + 1, curr_sum + nums[i])
            sub_lst.pop()

    nums.sort()
    backtrack(0, 0)

    if not result:
        return -1

    return min(len(x) for x in result)


if __name__ == '__main__':
    assert solve_method(4, [1, 1, 2, 2]) == 2
    assert solve_method(10, [1, 1, 1, 1, 1, 9, 8, 3, 7, 10]) == 3
    assert solve_method(4, [1, 5, 5, 8]) == -1
