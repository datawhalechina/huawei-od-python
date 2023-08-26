#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 199_height-sorting.py
@time: 2023/8/27 1:33
@project: huawei-od-python
@desc: 199 身高排序
"""

h, n = map(int, input().split())
highs = list(map(int, input().split()))
highs.sort(key=lambda x: (abs(x - h), x))
print(' '.join(map(str, highs)))
