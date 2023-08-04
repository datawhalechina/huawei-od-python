#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 107_integer-code.py
@time: 2023-07-26 14:01:22
@project: huawei-od-python
@desc: 107 整数编码
"""


def solve_method(num):
    # 得到二进制
    binary = bin(num)[2:]
    length = len(binary)
    result = ""
    # 从后向前，每7位遍历一次
    for i in range(length, 0, -7):
        start = max(i - 7, 0)
        bin_7bit = binary[start:i]
        # 位数不够7位左侧补0
        bin_7bit = bin_7bit.zfill(7)
        # 置1表示后面还有更多的字节，置0表示当前字节为最后一个字节
        bin_7bit = "0" + bin_7bit if i - 7 <= 0 else "1" + bin_7bit
        # 将二进制转成十六进制，并转成大写字母，然后位数不够2位，左边补0
        hex_7bit = hex(int(bin_7bit, 2)).upper()[2:].zfill(2)
        result += hex_7bit

    return result


if __name__ == "__main__":
    assert solve_method(0) == '00'
    assert solve_method(100) == '64'
    assert solve_method(1000) == 'E807'
