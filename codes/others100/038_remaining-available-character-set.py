#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 038_remaining-available-character-set.py
@time: 2023/8/8 13:36
@project: huawei-od-python
@desc: 038 剩余可用字符集
"""


def solve_method(line):
    total, used = line.split("@")

    def to_counter(chars):
        chars = chars.split(",")
        chars_map = {}
        for char in chars:
            char = char.split(":")
            chars_map[char[0]] = int(char[1])
        return chars_map

    total_map = to_counter(total)
    if used:
        used_map = to_counter(used)
        for k in used_map.keys():
            diff = total_map[k] - used_map[k]
            if diff > 0:
                total_map[k] = diff
            else:
                total_map.pop(k)

    return ",".join([k + ":" + str(v) for k, v in total_map.items()])


if __name__ == '__main__':
    assert solve_method("a:3,b:5,c:2@a:1,b:2") == "a:2,b:3,c:2"
    assert solve_method("a:3,b:5,c:2@") == "a:3,b:5,c:2"
