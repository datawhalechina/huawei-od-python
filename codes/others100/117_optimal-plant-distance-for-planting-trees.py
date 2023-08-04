#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 117_optimal-plant-distance-for-planting-trees.py
@time: 2023-07-28 16:32:22
@project: huawei-od-python
@desc: 117 最佳植树距离、种树问题
"""


def solve_method(holes, target):
    holes.sort()
    min_dist = 0
    max_dist = holes[-1] - holes[0]
    answer = -1

    while min_dist <= max_dist:
        mid = min_dist + (max_dist - min_dist) // 2
        # 第一个树种植的位置为第一个坑位
        count = 1
        previous = holes[0]
        for i in range(1, len(holes)):
            if holes[i] - previous >= mid:
                count += 1
                previous = holes[i]

                if count >= target:
                    answer = mid
                    min_dist = mid + 1
                    break

        if count < target:
            max_dist = mid - 1

    return answer


if __name__ == '__main__':
    assert solve_method([1, 3, 6, 7, 8, 11, 13], 3) == 6
    assert solve_method([1, 2, 6, 8, 14], 3) == 6
    assert solve_method([1, 7, 14], 2) == 13
