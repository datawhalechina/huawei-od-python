#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 003_convert-IPv4-addresses-to-integers.py
@time: 2023/7/26 10:07
@project: huawei-od-python
@desc: 003 IPv4地址转换成整数
"""


def check_ip(ip):
    is_valid = False
    if "#" in ip:
        ip_strings = ip.split("#")
        length = len(ip_strings)
        if length == 4 \
                and 1 <= int(ip_strings[0]) <= 128 \
                and 0 <= int(ip_strings[1]) <= 255 \
                and 0 <= int(ip_strings[2]) <= 255 \
                and 0 <= int(ip_strings[3]) <= 255:
            is_valid = True

    return is_valid


def solve_method(ip):
    if check_ip(ip):
        ip_strings = ip.split("#")
        num = 0
        for ip_string in ip_strings:
            num += int(ip_string)
            num = num << 8

        num = num >> 8
        return num
    else:
        return "invalid IP"


if __name__ == '__main__':
    assert solve_method("100#101#1#5") == 1684340997
    assert solve_method("1#2#3") == "invalid IP"
