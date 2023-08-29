#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 063_escape-room-game
@time:  2023/8/17 10:48
@project:  huawei-od-python
@desc: 063 密室逃生游戏
"""


def solve_method(key, boxes) -> int:
    key_lst = list(key)
    for index, chars in enumerate(boxes):
        chars = [char.lower() for char in chars if char.isalpha()]
        chars.sort()
        if chars == key_lst:
            return index
    return -1


if __name__ == '__main__':
    assert solve_method("abc", ["s", "sdf134", "A2c4b"]) == 2
    assert solve_method("abc", ["s", "sdf134", "A2c4bd", "523[]"]) == -1
