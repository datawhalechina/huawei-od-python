#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 191_calculate-the-nearest-number.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 191 计算最接近的数
"""

def find_median(nums):
    sorted_nums = sorted(nums)
    N = len(sorted_nums)
    return sorted_nums[N // 2]


def main():
    input_str = input().replace("[", "").replace("]", "").replace("", "")
    number_strings = input_str.split(",")

    N = len(number_strings) - 1
    nums = [int(x) for x in number_strings[:N]]
    K = int(number_strings[N])

    mid = find_median(nums)
    min_distance = float('inf')
    index = -1
    for i in range(N - K + 1):
        count = nums[i]

        for j in range(i + 1,i+K):
            count -= nums[j]

        distance = abs(count - mid)

        if distance < min_distance:
            min_distance = distance
            index = i
    print(index)


main()
