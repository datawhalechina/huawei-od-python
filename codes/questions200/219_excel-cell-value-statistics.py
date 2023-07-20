#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 219_excel-cell-value-statistics.py
@time: 2023/7/15
@project: huawei-od-python
@desc: 219 Excel 单元格数值统计
"""
import re

addSubPattern = re.compile(r'[\+\-]')
# ([A-Z])? 匹配一个可选的大写字母，用来表示列号
# ([0-9]+) 匹配一个或多个数字，用来表示行号
# (:) 匹配一个冒号，用来分隔起始和结束的单元格
# ([A-Z])?([0-9]+) 重复前面的模式，用来匹配结束的单元格
areaPattern = re.compile(r'([A-Z])?([0-9]+)(:)([A-Z])?([0-9]+)')

def getCellValue(cell,sheet):
    # 如果第一个符号不是A~Z，则为直接数，'A' > '9'
    if cell[0] >= 'A':
        return int(sheet[int(cell[1])-1][ord(cell[0])-ord('A')])
    else:
        return int(cell)

def evaluate(value, sheet):
    # 通过正则表达式找到 + / -
    addSubSig = addSubPattern.search(value)
    c1 = value

    # 如果有 + / - ，说明不是单独的 =cell
    if addSubSig:
        addSubSig = addSubSig.group()
        idx = value.index(addSubSig)
        c1 = value[:idx]
        c2 = value[idx+1:]
        # 获取单元格的值 或 将 字符串转化为数字
        c2 = getCellValue(c2,sheet)

    # 获取单元格的值 或 将 字符串转化为数字
    c1 = getCellValue(c1,sheet)
    
    # 计算表达式的值返回出去
    if addSubSig:
        if addSubSig == '+':
            return c1 + c2
        else:
            return c1 - c2
    else:
        return c1    
        
def solution(rows, cols, sheet, area):
    # 将表格中的"=xxx"表达式 计算为数值
    for r in range(rows):
        for c in range(int(cols)):
            if sheet[r][c].startswith('='):
                sheet[r][c] = evaluate(sheet[r][c][1:], sheet)
                
    # 正则匹配处理统计区域
    area = areaPattern.search(area)
    # 处理正则匹配拆出来的内容
    cs, rs, _, ce, re = area.groups()
    rs, re = int(rs)-1, int(re)-1
    cs, ce = ord(cs)-ord('A'), ord(ce)-ord('A')

    # 计算需要统计区域的值的和
    return sum(int(sheet[r][c]) for r in range(rs, re+1) for c in range(cs, ce+1))
    
if __name__ == '__main__':
    # 获取行、列数
    rows, cols = map(int, input().split())
    # 将输入的表格存储到sheet中
    sheet = [input().split() for _ in range(rows)] 
    # 获取需要统计和的起始和终点
    area = input()
    # 调用处理函数
    print(solution(rows, cols, sheet, area))