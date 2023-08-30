# !/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 047_rearrange-books.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 047 叠放书籍
"""


def solve_method(books):
    # 按照长度从大到小、宽度从大到小排序
    books.sort(key=lambda x: (x[0], x[1]), reverse=True)

    # 可叠放的书的个数
    count = 1
    # 前一本书
    prev = books[0]
    for book in books[1:]:
        # 如果当前书的长度和宽度都小于前一本书，则个数加1
        if prev[0] > book[0] and prev[1] > book[1]:
            count += 1
            prev = book

    return count


if __name__ == '__main__':
    assert solve_method([[20, 16], [15, 11], [10, 10], [9, 10]]) == 3
