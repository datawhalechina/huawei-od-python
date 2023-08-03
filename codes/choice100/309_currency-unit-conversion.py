#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 309_currency-unit-conversion.py
@time: 2023/8/3 15:33
@project: huawei-od-python
@desc: 309 货币单位换算
"""
import re


def solve_method(amounts):
    exchange = {
        "CNY": 100,
        "JPY": 100 / 1825 * 100,
        "HKD": 100 / 123 * 100,
        "EUR": 100 / 14 * 100,
        "GBP": 100 / 12 * 100,
        "fen": 1,
        "cents": 100 / 123,
        "sen": 100 / 1825,
        "eurocents": 100 / 14,
        "pence": 100 / 12
    }

    ans = 0

    s = "".join(amounts)
    nums = re.findall(r"\d+", s)
    units = re.findall(r"[a-zA-Z]+", s)
    for num, unit in zip(nums, units):
        ans += int(num) * exchange[unit]

    return int(ans)


if __name__ == '__main__':
    amounts = ["100CNY"]
    assert solve_method(amounts) == 10000
    amounts = ["3000fen"]
    assert solve_method(amounts) == 3000
    amounts = ["123HKD"]
    assert solve_method(amounts) == 10000
    amounts = ["20CNY53fen", "53HKD87cents"]
    assert solve_method(amounts) == 6432
