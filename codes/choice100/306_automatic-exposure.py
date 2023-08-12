#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 306_automatic-exposure.py
@time: 2023/8/2 23:47
@project: huawei-od-python
@desc: 306 自动曝光
"""


def solve_method(img):
    avg = sum(img) // len(img)
    diff = avg - 128
    new_img = img.copy()

    k = 0
    if diff > 0:
        # 如果差值大于0，则k是负数
        while avg > 127:
            k -= 1
            avg = get_new_image_avg(new_img, k)
    if diff < 0:
        # 如果差值小于0，则k是正数
        while avg < 128:
            k += 1
            avg = get_new_image_avg(new_img, k)
    return k


def get_new_image_avg(new_img, k):
    new_img = [min(max(0, x + k), 255) for x in new_img]
    return sum(new_img) // len(new_img)


if __name__ == '__main__':
    assert solve_method([0, 0, 0, 0]) == 128
    assert solve_method([129, 130, 129, 130]) == -2
