#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 151_caving.py
@time: 2023/8/29 0:17
@project: huawei-od-python
@desc: 151 洞穴探险
"""
import re


def solve_method(records):
    coordinates = re.findall(r'\((\d+),(\d+)\)', records)
    valid_coordinates = []
    for coordinate in coordinates:
        x, y = map(int, coordinate)
        if 0 < x < 1000 and 0 < y < 1000:
            valid_coordinates.append((x, y))
    if len(valid_coordinates) == 0:
        return "(0,0)"

    valid_coordinates.sort(key=lambda x: x[0] ** 2 + x[1] ** 2, reverse=True)
    return f"({valid_coordinates[0][0]},{valid_coordinates[0][1]})"


if __name__ == '__main__':
    records = "ferg(3,10)a13fdsf3(3,4)f2r3rfasf(5,10)"
    assert solve_method(records) == "(5,10)"

    records = "asfefaweawfawf(0,1)fe"
    assert solve_method(records) == "(0,0)"
