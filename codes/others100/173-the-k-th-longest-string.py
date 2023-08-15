#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 173-the-k-th-longest-string.py
@time: 2023/8/8 22:55
@project: huawei-od-python
@desc: 173 第k长子串
"""
from collections import defaultdict


def solve_method(s, k):
    # 字符频次字典，key为字符，value为连续字母的最大出现次数
    dic_len = defaultdict(int)

    pre_ch = s[0]
    word = []
    for ch in s:
        if ch == pre_ch:
            # 如果与前一个字母相同，则加入到单词列表中
            word.append(ch)
        else:
            # 如果与前一个字母不同，则更新前一个连续字符的最大出现次数
            dic_len[pre_ch] = max(dic_len[pre_ch], len(word))
            # 保存当前字符串
            pre_ch = ch
            # 更新单词列表
            word = [ch]

    if word and pre_ch:
        dic_len[pre_ch] = max(dic_len[pre_ch], len(word))

    # 将字符频次字典按照字符出现次数从大到小进行排序
    tuple_len = sorted(dic_len.items(), key=lambda x: -x[1])
    # 子串数小于k，找不到返回-1
    if k - 1 >= len(tuple_len):
        return -1
    else:
        return tuple_len[k - 1][1]


if __name__ == '__main__':
    assert solve_method("AABAAA", 2) == 1
    assert solve_method("AAAAHHHBBCDHHHH", 3) == 2
