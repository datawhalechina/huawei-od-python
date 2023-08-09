#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 178_draw_machine.py
@time: 2023/8/8 23:39
@project: huawei-od-python
@desc: 178 绘图机器
"""


def solve_method(n, e, steps):
    # 转变成字典表，便于查找
    dict_steps = dict(steps)
    # 每一步的位移，初始为0
    offset = 0
    # 总面积
    area = 0

    # 遍历起点到终点的长度e，如果改点在steps中能找到且做了位移，则进行改变
    for i in range(e):
        # 位移
        if i in dict_steps:
            offset+=dict_steps[i]
        # 面积即位移大小，向终点走的每一步都要累加计算
        area+=abs(offset)
        
    return area


if __name__ == '__main__':
    assert solve_method(4, 10, [(1,1),(2,1),(3,1),(4,-2)]) == 12
    assert solve_method(2, 4, [(0,1),(2,-2)]) == 4
