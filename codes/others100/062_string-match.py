#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 062_string-match
@time:  14/8/2023 下午 11:39
@project:  huawei-od-python 
"""


def match_string(nums, pattern):
    def dfs(index1, index2, s, pattern, m, n):
        if index1 == m and index2 == n:
            return True
        elif index1 == m or index2 == n:
            return False
        if pattern[index2] == '.' or s[index1] == pattern[index2]:
            return dfs(index1 + 1, index2 + 1, s, pattern, m, n)
        elif pattern[index2] == '*':
            return dfs(index1 + 1, index2, s, pattern, m, n) or dfs(index1 + 1, index2 + 1, s, pattern, m, n)
        else:
            return False

    n = len(pattern)
    ans = []
    for i, s in enumerate(nums):
        m = len(s)
        if dfs(0, 0, s, pattern, m, n):
            ans.append(str(i))
    return ' '.join(ans)


if __name__ == '__main__':
    nums = input().strip().split(' ')
    pattern = input().strip()
    res = match_string(nums, pattern)
    print(res)
