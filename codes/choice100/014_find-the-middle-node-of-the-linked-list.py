#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 014_find-the-middle-node-of-the-linked-list.py
@time: 2023/7/13 20:55
@project: huawei-od-python
@desc: 014 寻找链表的中间结点
"""


def solve_method(head, link):
    if len(link) == 0:
        return -1

    data = []
    next_node = head
    # 遍历链表
    while next_node in link:
        # 获取下一个结点
        node = link[next_node]
        # 将下一个结点的数据加入到列表中
        data.append(node[0])
        next_node = node[1]

    # 获取中间结点的数据
    return data[len(data) // 2]


if __name__ == '__main__':
    head = "00100"
    n = 4
    link = {"00000": [4, -1],
            "00100": [1, "12309"],
            "33218": [3, "00000"],
            "12309": [2, "33218"]}
    assert solve_method(head, link) == 3

    head = "10000"
    n = 3
    link = {"76892": [7, "12309"],
            "12309": [5, -1],
            "10000": [1, "76892"]}
    assert solve_method(head, link)
