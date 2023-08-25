#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 074_total-fastest-detection-efficiency
@time:  2023/8/24 16:42
@project:  huawei-od-python
@desc: 074 总最快检测效率
"""


def solve_method(samplers, num_volunteer):
    profit = []
    for p in samplers:
        # 当有1个志愿者，增加20%
        # 每增加1个志愿者，效率提升10%，最多提升30%
        profit.extend([p * 0.2, p * 0.1, p * 0.1, p * 0.1])
    # 没有志愿者协助时，每个采样员的效率是80%
    samplers = [i * 0.8 for i in samplers]
    # 选取志愿者能提升效率最高的分配给采样员，计算总和
    return sum(samplers) + sum(sorted(profit, reverse=True)[:num_volunteer])


if __name__ == '__main__':
    samplers = [200, 200]
    assert solve_method(samplers, 2) == 400
