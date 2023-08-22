#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 238_Open-day-activity.py
@time: 2023/8/22
@project: huawei-od-python
@desc: 238 开放日活动
"""

def solve_method(target_sum, bucket_balls):
    total = sum(bucket_balls)
    if total <= target_sum:
        # 整体小球总数未超过范围
        return []
    
    tmp = [0] * len(bucket_balls)
    sub = [0] * len(bucket_balls)

    for i in range(target_sum, 0, -1):
        for k in range(len(bucket_balls)):
            # 进行取球尝试
            sub[k] = bucket_balls[k] - i if bucket_balls[k] - i > 0 else 0
            tmp[k] = i if bucket_balls[k] - i > 0 else bucket_balls[k]
        if sum(tmp) <= target_sum:
            # 达到要求即可返回
            return sub

if __name__ == '__main__':
    bucket_balls = [2,3,2,5,5,1,4]
    assert solve_method(14, bucket_balls) == [0, 1, 0, 3, 3, 0, 2]

    bucket_balls = [1, 2, 3]
    assert solve_method(3, bucket_balls) == [0, 1, 2]

    bucket_balls = [3, 2]
    assert solve_method(6, bucket_balls) == []