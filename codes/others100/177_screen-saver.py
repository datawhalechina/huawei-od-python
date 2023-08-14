#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 177_screen-saver.py
@time: 2023/8/8 23:33
@project: huawei-od-python
@desc: 177 经典屏保
"""


def solve_method(s):
    # 题目提供的默认常量
    screen_width = 800
    screen_length = 600
    logo_width = 50
    logo_length = 25
    
    x, y, t = list(map(int, s.split()))
    # 求总长度
    x+=t
    y+=t
    # 一来一回为一个周期，两倍的长度，注意去掉logo长度
    interval_x = 2*(screen_width-logo_width)
    interval_y = 2*(screen_length-logo_length)
    
    x %= interval_x
    y %= interval_y
    
    # 超过了一半，要反向
    if x>(screen_width-logo_width):
        x = interval_x-x
    if y>(screen_length-logo_length):
        y = interval_y-y
    return '{} {}'.format(x, y)


if __name__ == '__main__':
    assert solve_method("0 0 10") == '10 10'
    assert solve_method("500 570 10") == '510 570'
