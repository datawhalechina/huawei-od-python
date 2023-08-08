#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 037_identify-poker.py
@time: 2023/8/8 11:09
@project: huawei-od-python
@desc: 037 判断牌型
"""

from collections import Counter


# 同花
def check_tonghua(colors):
    # 判断花色是否一致
    return len(set(colors)) == 1


# 顺子
def check_shunzi(cards, nums):
    if "".join(nums) == "2345A":
        return True
    # 检查是否构成顺子
    for i in range(1, len(nums)):
        if cards[nums[i - 1]] + 1 != cards[nums[i]]:
            return False

    return True


# 四条
def check_four(nums):
    num_count = Counter(nums)
    return 4 in num_count.values()


# 葫芦
def check_hulu(nums):
    num_count = Counter(nums)

    # 检查是否存在三张相同牌值的牌和两张相同牌值的牌
    values = num_count.values()
    return len(values) == 2 and (2 in values or 3 in values)


# 三条
def check_three(nums):
    num_count = Counter(nums)
    # 判断是否有三张相同牌值得牌
    return 3 in num_count.values()


def solve_method(pokers):
    cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
             "A": 14}
    nums = []
    colors = []
    for poker in pokers:
        nums.append(poker[0])
        colors.append(poker[1])

    nums = sorted(nums, key=lambda x: cards[str(x)])
    shunzi_checked = check_shunzi(cards, nums)
    tonghua_checked = check_tonghua(colors)
    if shunzi_checked and tonghua_checked:
        return 1
    elif check_four(nums):
        return 2
    elif check_hulu(nums):
        return 3
    elif tonghua_checked:
        return 4
    elif shunzi_checked:
        return 5
    elif check_three(nums):
        return 6
    else:
        return 7


if __name__ == '__main__':
    pokers = [["4", "H"],
              ["5", "S"],
              ["6", "C"],
              ["7", "D"],
              ["8", "D"]]
    assert solve_method(pokers) == 5

    pokers = [["9", "S"],
              ["5", "S"],
              ["6", "S"],
              ["7", "S"],
              ["8", "S"]]
    assert solve_method(pokers) == 1
