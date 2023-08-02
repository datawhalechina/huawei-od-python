#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 303_port-merging.py
@time: 2023/8/2 10:11
@project: huawei-od-python
@desc: 303 端口合并
"""


def merge(ports):
    for i in range(len(ports)):
        for j in range(i + 1, len(ports)):
            seti = set(ports[i])
            setj = set(ports[j])
            merge_set = seti.union(setj)
            if len(merge_set) <= len(seti) + len(setj) - 2:
                ports[i] = list(merge_set)
                ports.pop(j)
                return True
    return False


def solve_method(ports):
    while merge(ports):
        pass

    return [sorted(list(set(p))) for p in ports]


if __name__ == '__main__':
    ports = [[4], [2, 3, 2], [1, 2], [5]]
    assert solve_method(ports) == [[4], [2, 3], [1, 2], [5]]
    ports = [[2, 3, 1], [4, 3, 2], [5]]
    assert solve_method(ports) == [[1, 2, 3, 4], [5]]
    ports = [[10], [4, 2, 1], [9], [3, 6, 9, 2], [6, 3, 4], [8]]
    assert solve_method(ports) == [[10], [1, 2, 3, 4, 6, 9], [9], [8]]
