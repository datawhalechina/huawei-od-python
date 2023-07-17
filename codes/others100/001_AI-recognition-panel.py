#!/usr/bin/env python
# encoding: utf-8
"""
@author: Spridra
@file: 265_AI-Processor-Combination.py
@time: 2023/7/17 09:02
@project: huawei-od-python
@desc: 001 AI识别面板
"""


def solve_method(lights):
    lights_list = []
    for light in lights:
        id = light[0]
        x1 = light[1]
        y1 = light[2]
        x2 = light[3]
        y2 = light[4]
        # id, x坐标的平均值, y坐标的平均值, 灯高半径
        lights_list.append([id, (x1 + x2) // 2, (y1 + y2) // 2, (y2 - y1) // 2])

    # 将灯按行粗排
    lights_list.sort(key=lambda x: x[2])

    result = []

    # 设置每一行的起始索引
    row_start_index = 0
    # 先使用第1行第1个作为基准灯
    for i in range(1, len(lights_list)):
        # 高低偏差超过灯高度的一半
        if lights_list[i][2] - lights_list[row_start_index][2] > lights_list[row_start_index][3]:
            # 把之前的灯按x坐标排序，并存入结果列表中
            lights_list[row_start_index:i] = sorted(lights_list[row_start_index:i], key=lambda x: x[1])
            result.extend([light[0] for light in lights_list[row_start_index:i]])
            # 记录新一行对应的灯位置
            row_start_index = i

    # 把该行剩余的灯全部加入到结果列表中
    lights_list[row_start_index:] = sorted(lights_list[row_start_index:], key=lambda x: x[1])
    result.extend([light[0] for light in lights_list[row_start_index:]])

    return result


if __name__ == '__main__':
    lights = [
        [1, 0, 0, 2, 2],
        [2, 6, 1, 8, 3],
        [3, 3, 2, 5, 4],
        [5, 5, 4, 7, 6],
        [4, 0, 4, 2, 6]
    ]

    assert solve_method(lights) == [1, 2, 3, 4, 5]

