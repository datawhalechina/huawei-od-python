#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 164_max_number_of_consecutive_occurrences_of_the_same_char.py
@time: 2023/8/8 22:00
@project: huawei-od-python
@desc: 164 相同字符连续出现的最大次数
"""


def solve_method(s):
    # 双指针
    left = right = 0
    # 求最大值则初始化一个负无穷，当然也可以为0
    max_v = -float('inf')

    # 双指针模板
    count = 0
    while right<len(s):
        # 遇到相同字符指针右移，次数+1
        if s[left]==s[right]:
            count+=1
            right+=1
        # 遇到不相同字符，统计left字符的count
        # 更新最大值，随后left移到新字符上，count归零
        else:
            max_v = max(max_v, right-left)
            left=right
            count=0
    # 循环外结尾的字符还要更新一次，因为退出时没有进入while内的更新部分
    max_v = max(max_v, right-left)
    return max_v


if __name__ == '__main__':
    assert solve_method("aaabbc") == 3
    assert solve_method("aaabbccccc") == 5
    assert solve_method("aaabbcccccbbbbbbaaaaa") == 6
