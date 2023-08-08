#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 165_relative_open_syllable.py
@time: 2023/8/8 22:03
@project: huawei-od-python
@desc: 165 相对开音节
"""


def solve_method(s):
    # 检查是否合法满足相对元音
    def check(ind, string):
        # 首先长度至少为4
        if ind>=3:
            # ind为e，我们取e前三个字符
            # 首先得是单词字母，其次满足：辅音+元音(aeiou)+辅音(r除外)+e
            substring = string[ind-3:ind]
            # print(substring)
            if substring.isalpha() and substring[0] not in 'aeiou' and substring[1] in 'aeiou' and substring[2] not in 'aeiour':
                return True
        return False
    # 空格切割和反转
    s_list = list(map(lambda x:x[::-1] if x.isalpha() else x, s.split()))
    # print(s_list)
    count = 0
    for string in s_list:
        # 只包含字母
        for ind, char in enumerate(string):
            if char=='e' and check(ind, string):
                count+=1
    return count


if __name__ == '__main__':
    assert solve_method("!ekam a ekekac") == 2
    assert solve_method("ekam a ekac") == 2
    assert solve_method("ekam a ekekac") == 3
