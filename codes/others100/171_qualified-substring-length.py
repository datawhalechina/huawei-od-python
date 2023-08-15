#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 171_qualified-substring-length.py
@time: 2023/8/8 22:48
@project: huawei-od-python
@desc: 171 符合条件的子串长度
"""


def solve_method(s1, s2, v):
    diff_list = []
    n = len(s1)
    for ch1, ch2 in zip(s1, s2):
        diff_list.append(abs(ord(ch1) - ord(ch2)))
    # 两个指针
    left = right = 0
    # 记录累加和
    accu = 0
    # 记录最大长度
    max_len = 0
    while right < n:
        accu += diff_list[right]
        # 累加和accu超过了v，左端点右移，accu减去相应的值
        while accu > v:
            accu -= diff_list[left]
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len


if __name__ == '__main__':
    assert solve_method("xxcdefgx", "cdefghic", 5) == 2
