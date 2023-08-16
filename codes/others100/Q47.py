#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:Q47.py
@Date：2023/08/11 0:47
"""

import sys


class Book:
    def __init__(self, l, w):
        self.l = l  # 书的长度
        self.w = w  # 书的宽度

    def __lt__(self, other):
        # 定义小于运算符，用于排序。如果当前书的长度和宽度都大于或等于另一本书，则返回True。
        return self.l <= other.l and self.w <= other.w


def solve_method(input_str):
    # 去除输入字符串的首尾括号
    input_str = input_str.strip()[2:-2]
    # 使用列表推导式创建Book对象列表
    books = [Book(*map(int, book_str.split(","))) for book_str in input_str.split("],[")]
    # 按照长度和宽度的递减顺序对书进行排序
    books.sort(reverse=True)

    count = 0  # 计数符合条件的书的数量
    last = None  # 存储上一本符合条件的书
    for cur in books:
        # 如果当前书是第一本书，或者当前书的长度和宽度都小于上一本符合条件的书，则计数加1
        if last is None or (last.l > cur.l and last.w > cur.w):
            count += 1
            last = cur

    print(count)  # 打印符合条件的书的数量


if __name__ == '__main__':
    input_str = sys.stdin.readline()  # 从标准输入读取字符串
    solve_method(input_str)  # 调用解决方案方法
