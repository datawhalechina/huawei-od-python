#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 061_string-abstract
@time:  2023/8/13 17:45
@project:  huawei-od-python
@desc: 061 字符串摘要
"""


def solve_method(s):
    n = len(s)
    index = 0
    result = []
    s = s.lower()

    while index < n:
        if index == n - 1:
            result.append(s[index] + "0")
        if s[index] == s[index + 1]:
            # 如果是连续字符
            start, index = index, index + 1
            # 统计相同字符出现次数
            while index < n - 1 and s[index] == s[index + 1]:
                index += 1
            freq = index - start + 1
            result.append(s[start] + str(freq))
            index += 1
        else:
            # 如果是非连续字符
            freq = s.count(s[index], index + 1, n)
            result.append(s[index] + str(freq))
            index += 1
    # 将结果列表按照数字从大到小、字符按字典序排序
    result.sort(key=lambda x: (-int(x[1]), x[0]))
    return "".join(result)


if __name__ == '__main__':
    assert solve_method("aabbcc") == "a2b2c2"
    assert solve_method("bAaAcBb") == "a3b2b2c0"
