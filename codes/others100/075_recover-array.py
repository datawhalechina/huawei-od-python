#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 075_recover-array
@time:  24/8/2023 下午 5:04
@project:  huawei-od-python 
"""
from collections import Counter


# def solve_method(s, n):
#     length = len(s)
#     counter = sorted(dict(Counter(s)).items(), key=lambda x: x[1], reverse=True)
#     if length % n == 0:
#         k = length // n
#         if k == 1:
#             return int(sorted(list(s))[0])
#         elif k == 2:
#
#
#         pass
#     else:
#         k = length // n
#         s0 = '9' * k
#         diff = (len(s0) + 1) * n
