#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 286_adjust-poker.py
@time: 2023/7/14 18:27
@project: huawei-od-python
@desc: 286 整理扑克牌
"""
import collections


def solve_method(poker_arr):
    counter = collections.Counter(poker_arr)
    # 按照频数降序、按照牌面降序排列
    sorted_pokers = sorted(counter.items(), key=lambda x: (-x[1], -x[0]))

    result = []
    # 拆牌队列
    split_pokers = []
    for i, (card_num, card_count) in enumerate(sorted_pokers):
        # 由于已经排好序，如果当前牌有3张，前一个大一点的牌也有3张，拆分当前牌为两张或一张
        if i > 0 and sorted_pokers[i - 1][1] == 3 and card_count == 3:
            # 添加到拆牌队列中
            split_pokers.append(card_num)
            card_count = 2
            # 将当前位置，重新赋值为2张
            sorted_pokers[i] = (card_num, 2)
        elif card_count == 1 and split_pokers:
            # 循环比较单张牌
            for k, split_num in enumerate(split_pokers):
                if split_num > card_num:
                    result.append(split_num)
                    split_pokers.pop(k)
                    break

        # 添加到整理好的结果列表中
        result.extend([card_num] * card_count)

    # 如果拆牌队列中还有牌，直接加入到结果列表队尾
    if split_pokers:
        result.extend(split_pokers)

    return result


if __name__ == '__main__':
    assert solve_method([1, 3, 3, 3, 2, 1, 5]) == [3, 3, 3, 1, 1, 5, 2]
    assert solve_method([4, 4, 2, 1, 2, 1, 3, 3, 3, 4]) == [4, 4, 4, 3, 3, 2, 2, 1, 1, 3]
    assert solve_method([4, 4, 4, 4, 3, 3, 4]) == [4, 4, 4, 4, 4, 3, 3]
