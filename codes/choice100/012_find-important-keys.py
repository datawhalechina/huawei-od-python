#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 012_find-important-keys.py
@time: 2023/7/13 19:55
@project: huawei-od-python
@desc: 012 寻找关键钥匙
"""


def solve_method(key, line):
    boxes = line.split()
    processed_boxes = []
    for box in boxes:
        # 得到箱子的有效密码串
        box_keys = [char.lower() for char in box if char.isalpha()]
        if len(box_keys) > 0:
            # 对字符串排序
            box_keys.sort()
            processed_boxes.append("".join(box_keys))
    try:
        # 返回对应箱子编号
        return processed_boxes.index(key) + 1
    except ValueError:
        # 如果不存在，则返回-1
        return -1


if __name__ == '__main__':
    assert solve_method("abc", "s,sdf123  A2c4b") == 2
    assert solve_method("abc", "s,sdf123 A2c4bd 523[]") == -1
