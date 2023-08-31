#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 020_open-day-activity.py
@time: 2023/8/22
@project: huawei-od-python
@desc: 020 开放日活动
"""


def solve_method(target_sum, bucket_balls):
    total = sum(bucket_balls)
    if total <= target_sum:
        # 整体小球总数未超过范围
        return []

    # 各桶中剩余的球列表
    remainder_balls = [0] * len(bucket_balls)
    # 各桶中取出的球列表
    drop_balls = [0] * len(bucket_balls)

    # 从大到小遍历容量值
    for i in range(target_sum, 0, -1):
        for k in range(len(bucket_balls)):
            # 进行取球尝试
            drop_balls[k] = bucket_balls[k] - i if bucket_balls[k] - i > 0 else 0
            remainder_balls[k] = i if bucket_balls[k] - i > 0 else bucket_balls[k]
        if sum(remainder_balls) <= target_sum:
            # 达到要求即可返回
            return drop_balls


if __name__ == '__main__':
    bucket_balls = [2, 3, 2, 5, 5, 1, 4]
    assert solve_method(14, bucket_balls) == [0, 1, 0, 3, 3, 0, 2]

    bucket_balls = [1, 2, 3]
    assert solve_method(3, bucket_balls) == [0, 1, 2]

    bucket_balls = [3, 2]
    assert solve_method(6, bucket_balls) == []
