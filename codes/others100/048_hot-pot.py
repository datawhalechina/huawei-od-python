#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 048_hot-pot.py
@time: 2023/7/27 14:56
@project: huawei-od-python
@desc: 048 吃火锅
"""


def solve_method(dishes, m):
    dish_cooked_time = []
    for dish in dishes:
        dish_cooked_time.append(dish[0] + dish[1])
    # 得到每个菜可以吃的时刻
    dish_cooked_time.sort()

    # 上一个吃到菜的时刻
    pre_time = dish_cooked_time[0]
    count = 1
    for i in range(1, len(dishes)):
        # 如果等待的时间能吃到这次的菜
        if dish_cooked_time[i] >= pre_time + m:
            # 记录吃到菜的时刻
            pre_time = dish_cooked_time[i]
            # 累计次数
            count += 1

    return count


if __name__ == '__main__':
    dishes = [[1, 2],
              [2, 1]]
    assert solve_method(dishes, 1) == 1

    dishes = [[1, 2],
              [1, 3],
              [2, 3]]
    assert solve_method(dishes, 1) == 3
