#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 018_print-file.py
@time: 2023/7/14 14:00
@project: huawei-od-python
@desc: 018 打印文件
"""
import heapq


def solve_method(print_list):
    result = []
    file_id = 1
    # 构造一个打印机序列，其中key是打印机编号，value是待打印的优先序列
    printers = {}
    for command in print_list:
        commands = command.split()
        if commands[0] == "IN":
            p = commands[1]
            num = int(commands[2])
            if p not in printers:
                printers[p] = []
            # 使用优先队列，由于优先序列是越小越优先，所以num要取负号
            heapq.heappush(printers[p], (-num, file_id))
            file_id += 1
        elif commands[0] == "OUT":
            p = commands[1]
            if p in printers and len(printers[p]) > 0:
                _, file_id = heapq.heappop(printers[p])
                result.append(file_id)
            else:
                result.append("NULL")

    return result


if __name__ == '__main__':
    print_list = [
        "IN 1 1",
        "IN 1 2",
        "IN 1 3",
        "IN 2 1",
        "OUT 1",
        "OUT 2",
        "OUT 2"
    ]
    assert solve_method(print_list) == [3, 4, "NULL"]

    print_list = [
        "IN 1 1",
        "IN 1 3",
        "IN 1 1",
        "IN 2 3",
        "OUT 1"
    ]
    assert solve_method(print_list) == [2]
