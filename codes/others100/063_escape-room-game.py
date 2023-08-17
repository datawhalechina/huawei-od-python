#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 063_escape-room-game
@time:  17/8/2023 上午 10:48
@project:  huawei-od-python 
"""
from typing import List
import re


def solve_method(key: str, boxes: List[str]) -> int:
    pattern = r'[^a-zA-Z]+'
    boxes = [''.join(sorted(re.sub(pattern, '', s).lower())) for s in boxes]
    for index, s in enumerate(boxes):
        if s == key:
            return index
    return -1


if __name__ == '__main__':
    key = input().strip()
    boxes = input().strip().split(',')
    res = solve_method(key, boxes)
    print(res)
