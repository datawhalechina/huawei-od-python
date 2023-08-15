#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 175_simple-unzip.py
@time: 2023/8/8 21:27
@project: huawei-od-python
@desc: 175 简易压缩算法
"""


def solve_method(s):
    if s[-1].isdigit():
        return "!error"

    # 检查字符串是否合法，判断是否是数字和小写字母
    for i in s:
        if i.isdigit() or (i.isalpha() and i.islower()):
            continue
        else:
            return '!error'

    num_str = ""
    result = ""
    for ch in s:
        if ch.isdigit():
            # 如果为数字，则加入到数字字符串中
            num_str += ch
        elif num_str and ch.isalpha():
            # 如果为字母，并且数字字符串不为空
            if int(num_str) > 2:
                # 如果数字大于2，则进行解压操作，存入结果字符串中。
                result += ch * int(num_str)
                num_str = ""
            else:
                # 如果数字小于等于2，则返回错误
                return '!error'
        else:
            # 如果为字母，则存入结果字符串
            result += ch

    return result


if __name__ == '__main__':
    assert solve_method("4dff") == 'ddddff'
    assert solve_method("2dff") == '!error'
    assert solve_method("4d@A") == '!error'
