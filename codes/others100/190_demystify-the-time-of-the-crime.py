#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 190_demystify-the-time-of-the-crime.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 190 解密犯罪时间
"""


def solve_method(time):
    # 得到时间中出现过的数字
    nums = [int(c) for c in time if c != ":"]
    # 得到小时和分钟
    h, m = map(int, time.split(":"))
    lst = set()
    # 得到由这些数字组成的时间
    for i in nums:
        for j in nums:
            if i <= 5:
                lst.add(i * 10 + j)
    lst = list(sorted(lst))

    # 当前小时的时刻的最近分钟
    for i in lst:
        if i <= m:
            continue
        return format_time(h, i)

    # 当前时间的分钟数很大，则是后面小时的时刻
    if h != 23:
        for i in lst:
            if i <= h:
                continue
            if i <= 23:
                # 得到最近小时的时刻最小分钟数
                return format_time(i, lst[0])

    # 第二天的最近时刻的最小分钟数
    return format_time(lst[0], lst[0])


def format_time(h, m):
    return f"{h:02d}:{m:02d}"


if __name__ == "__main__":
    assert solve_method("20:12") == "20:20"
    assert solve_method("23:59") == "22:22"
    assert solve_method("20:59") == "22:00"
    assert solve_method("23:09") == "23:20"
