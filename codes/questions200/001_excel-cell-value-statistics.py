#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 001_excel-cell-value-statistics.py
@time: 2023/7/15
@project: huawei-od-python
@desc: 001 Excel 单元格数值统计
"""
import re

add_sub_pattern = re.compile(r'[\\+\-]')
# ([A-Z])? 匹配一个可选的大写字母，用来表示列号
# ([0-9]+) 匹配一个或多个数字，用来表示行号
# (:) 匹配一个冒号，用来分隔起始和结束的单元格
# ([A-Z])?([0-9]+) 重复前面的模式，用来匹配结束的单元格
area_pattern = re.compile(r'([A-Z])?([0-9]+)(:)([A-Z])?([0-9]+)')


def get_cell_value(cell, sheet):
    # 如果第一个符号不是A~Z，则为直接数，'A' > '9'
    if cell[0] >= 'A':
        return int(sheet[int(cell[1]) - 1][ord(cell[0]) - ord('A')])
    else:
        return int(cell)


def evaluate(value, sheet):
    # 通过正则表达式找到 + / -
    add_sub_sig = add_sub_pattern.search(value)
    c1 = value
    c2 = 0
    # 如果有 + / - ，说明不是单独的 =cell
    if add_sub_sig:
        add_sub_sig = add_sub_sig.group()
        idx = value.index(add_sub_sig)
        c1 = value[:idx]
        c2 = value[idx + 1:]
        # 获取单元格的值 或 将字符串转化为数字
        c2 = get_cell_value(c2, sheet)

    # 获取单元格的值 或 将 字符串转化为数字
    c1 = get_cell_value(c1, sheet)

    # 计算表达式的值返回出去
    if add_sub_sig:
        if add_sub_sig == '+':
            return c1 + c2
        else:
            return c1 - c2
    else:
        return c1


def solve_method(rows, cols, sheet, area):
    # 将表格中的"=xxx"表达式 计算为数值
    for r in range(rows):
        for c in range(int(cols)):
            if sheet[r][c].startswith('='):
                sheet[r][c] = evaluate(sheet[r][c][1:], sheet)

    # 正则匹配处理统计区域
    area = area_pattern.search(area)
    # 处理正则匹配拆出来的内容
    c_start, r_start, _, c_end, r_end = area.groups()
    r_start, r_end = int(r_start) - 1, int(r_end) - 1
    c_start, c_end = ord(c_start) - ord('A'), ord(c_end) - ord('A')

    # 计算需要统计区域的值的和
    return sum(int(sheet[r][c]) for r in range(r_start, r_end + 1) for c in range(c_start, c_end + 1))


if __name__ == '__main__':
    sheet = [["10", "12", "=C5"],
             ["15", "5", "6"],
             ["7", "8", "=3+C2"],
             ["6", "=B2-A1", "=C2"],
             ["7", "5", "3"]]
    assert solve_method(5, 3, sheet, "B2:C4") == 29

    sheet = [["1", "=A1+C1", "3"]]
    assert solve_method(1, 3, sheet, "A1:C1") == 8
