#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 012_determine-the-string-subsequence.py
@time: 2023/9/1 18:11
@project: huawei-od-python
@desc: 065 判断字符串子序列
"""


def solve_method(target, source):
    t_pos = len(target) - 1
    s_pos = len(source) - 1

    # 由于获取下标较大的位置，则从后向前遍历
    while t_pos >= 0 and s_pos >= 0:
        if target[t_pos] == source[s_pos]:
            t_pos -= 1
            if t_pos < 0:
                # 当遍历得到第一个子序列，则可以返回当前下标
                return s_pos

        s_pos -= 1

    return -1


if __name__ == '__main__':
    assert solve_method("abc", "abcaybec") == 3
