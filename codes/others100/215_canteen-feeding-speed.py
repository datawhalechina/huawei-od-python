#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 215_canteen-feeding-speed.py
@time: 2023/7/22 23:19
@project: huawei-od-python
@desc: 215 食堂供餐
"""


def solve_method(total, M, N, P):
    min_speed, max_speed = 0, total - M
    result = max_speed
    # 二分查找，速度范围为[min_speed, max_speed]
    while min_speed <= max_speed:
        mid = (min_speed + max_speed) // 2
        # 检查该速度是否能满足
        if check_speed(mid, M, N, P):
            # 如果能满足
            result = mid
            # 继续查找左侧
            max_speed = mid - 1
        else:
            # 如果不能，则继续查找右侧
            min_speed = mid + 1

    return result


def check_speed(speed, foods, N, P):
    for i in range(N):
        foods -= P[i]
        if foods < 0:
            return False
        foods += speed
    return True


if __name__ == '__main__':
    P = [10, 4, 5]
    assert solve_method(sum(P), 14, 3, P) == 3
