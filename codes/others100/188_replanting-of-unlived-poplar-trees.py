#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 188_replanting-of-unlived-poplar-trees.py
@time: 2023/8/27 1:30
@project: huawei-od-python
@desc: 188 补活未成活胡杨树
"""

num_of_dice = int(input())
num_of_sides = int(input())
dice_strings = input().split()

rolls = [0] * num_of_dice
k = int(input())

for i in range(num_of_sides):
    rolls[int(dice_strings[i]) - 1] = 1

left = 0
right = 0
count = 0
result = 0

while right < num_of_dice:
    while right < num_of_dice and count <= k:
        if rolls[right] == 1:
            count += 1
        right += 1

        if count <= k:
            result = max(right - left, result)
    while left <= right and count > k:
        if rolls[left] == 1:
            count -= 1
        left += 1

print(result)
