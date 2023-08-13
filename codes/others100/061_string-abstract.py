#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 061_string-abstract
@time:  13/8/2023 下午 5:45
@project:  huawei-od-python 
"""
import re

pattern = r"[^a-zA-Z]+"


def solve_method(s):
    n = len(s)
    index = 0
    item_list = []
    s = re.sub(pattern, '', s)
    s = s.lower()

    def count(s, c, start, end):
        ans = 0
        for i in range(start, end):
            if s[i] == c:
                ans += 1
        return ans

    while index < n:
        if index == n - 1:
            item_list.append(f'{s[index]}0')
        if s[index] == s[index + 1]:
            start, index = index, index + 1
            while index < n - 1 and s[index] == s[index + 1]:
                index += 1
            freq = index - start + 1
            item_list.append(f'{s[start]}{freq}')
            index += 1
        else:
            freq = count(s, s[index], index + 1, n)
            item_list.append(f'{s[index]}{freq}')
            index += 1
    item_list.sort(key=lambda x: (-int(x[1]), ord(x[0])))
    return ''.join(item_list)


if __name__ == '__main__':
    s = input()
    res = solve_method(s)
    print(res)
