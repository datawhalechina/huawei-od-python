#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 177_screen-saver.py
@time: 2023/8/8 23:33
@project: huawei-od-python
@desc: 177 经典屏保
"""


def solve_method(x, y, t):
    screen_width, screen_length = 800, 600
    logo_width, logo_length = 50, 25

    x_dir = 1
    y_dir = 1
    for i in range(t):
        # 继续移动
        x += x_dir
        y += y_dir

        # 当达到边缘时，转向
        if x == 0 or x == screen_width - logo_width:
            x_dir *= -1
        if y == 0 or y == screen_length - logo_length:
            y_dir *= -1

    return x, y


if __name__ == '__main__':
    assert solve_method(0, 0, 10) == (10, 10)
    assert solve_method(500, 570, 10) == (510, 570)
