#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 173_the_k_th_longest_string.py
@time: 2023/8/8 22:55
@project: huawei-od-python
@desc: 173 第k长子串
"""


def solve_method(k, s):
    dic_len = {}
    
    # 双指针，将同一元素最大长度存到dic_len字典中
    left = right = 0
    n = len(s)
    
    count=0
    while right<n:
        if s[left]!=s[right]:
            if s[left] in dic_len:
                dic_len[s[left]] = max(dic_len[s[left]], right-left)
            else:
                dic_len[s[left]] = right-left
            left = right
        right+=1
    if s[left] in dic_len:
        dic_len[s[left]] = max(dic_len[s[left]], right-left)
    else:
        dic_len[s[left]] = right-left

    # 将字典转化成元祖，按照长度从大到小进行排序
    tuple_len = sorted(dic_len.items(), key=lambda x:-x[1])
    # 记录总长度n
    n = len(tuple_len)
    
    # 子串数小于k，找不到返回-1
    if k-1>=n:
        return -1
    else:
        return tuple_len[k-1][1]


if __name__ == '__main__':
    assert solve_method(2, "AABAAA") == 1
    assert solve_method(3, "AAAAHHHBBCDHHHH") == 2
