#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 272_decrypt-string.py
@time: 2023/7/13 11:10
@project: huawei-od-python
@desc: 272 字符串解密加扰字符串
"""


def solve_method(string1, string2):
    # 获取有效子串
    avail_strings = get_available_strings(string1)

    # 参考字符串的长度
    string2_len = len(set(string2))

    result = ""
    for ava_str in avail_strings:
        if len(ava_str) > 0:
            # 有效子串的长度
            ava_str_len = len(set(ava_str))

            # 如果有效子串的长度小于参考字符串的长度
            if ava_str_len <= string2_len:
                result_len = len(set(result))
                # 如果满足条件
                if ava_str_len > result_len:
                    result = ava_str
                # 如果长度相等，取字典序大的那个
                elif ava_str_len == result_len and ava_str > result:
                    result = ava_str

    return result if len(result) > 0 else "Not Found"


def get_available_strings(string1):
    scrambled_sub = "1234567890abcdef"

    avail_strings = []
    tmp_string = ""
    for c in string1:
        if c not in scrambled_sub:
            tmp_string += c
        else:
            if tmp_string != "":
                avail_strings.append(tmp_string)
                tmp_string = ""

    if tmp_string != "":
        avail_strings.append(tmp_string)

    return avail_strings


if __name__ == '__main__':
    assert solve_method("123admyffc79pt", "ssyy") == "pt"
    assert solve_method("123admyffc79ptaagghi2222smeersst88mnrt", "ssyyfgh") == "mnrt"
    assert solve_method("abcmnq", "rt") == "Not Found"

