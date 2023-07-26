#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 007_tlv-code.py
@time: 2023/7/26 13:54
@project: huawei-od-python
@desc: 007 TLV编码
"""


def solve_method(tag, source):
    index = 0
    while index < len(source):
        cur_tag = source[index]
        # 小端序
        length = int(source[index + 2] + source[index + 1], 16)
        if tag == cur_tag:
            value = source[index + 3: index + 3 + length]
            return value

        index += 3 + length


if __name__ == '__main__':
    source = ["32", "01", "00", "AE", "90", "02", "00", "01", "02", "30", "03", "00",
              "AB", "32", "31", "31", "02", "00", "32", "33", "33", "01", "00", "CC"]
    assert solve_method("31", source) == ["32", "33"]
