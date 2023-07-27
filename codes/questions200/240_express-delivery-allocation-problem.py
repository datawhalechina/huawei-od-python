#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 240_express-delivery-allocation-problem.py
@time: 2023/7/25
@project: huawei-od-python
@desc: 240 快递投放问题
"""
from collections import defaultdict


def solve_method(want, cant):
    # 初始化包裹道路信息的 字典 和 无法通行的道路字典
    want_map = defaultdict(set)
    cant_map = defaultdict(set)

    # 将 want 中 包裹道路信息，按照 [key = package] = "起点-终点"的格式记录在want_map字典里
    for arr in want:
        pkg, path1, path2 = arr
        path = path1 + "-" + path2
        want_map[path].add(pkg)

    # 将 cant 中 不可通行信息，按照 [key = "起点-终点"] = 包裹1，包裹2，... 的格式记录在cant_map字典里
    for arr in cant:
        path1, path2, *pkgs = arr
        path = path1 + "-" + path2
        cant_map[path].update(pkgs)

    res = []
    for path, want_pkg in want_map.items():
        # 遍历包裹道路信息，在不可通行信息中找 key = 道路
        cant_pkg = cant_map.get(path)

        if cant_pkg is None:
            continue

        # 将两个集合求交集，即不可通行信息中对应的包裹，记录到结果列表中
        cant_pkgs = cant_pkg.intersection(want_pkg)
        res.extend(list(cant_pkgs))

    if not res:
        return "none"

    # 按照包裹序列进行排序
    res.sort(key=lambda s: int(s[7:]))

    return res


if __name__ == '__main__':
    packages = [["package1", "A", "C"],
                ["package2", "A", "C"],
                ["package3", "B", "C"],
                ["package4", "A", "C"]]
    barries = [["A", "B", "package1"],
               ["A", "C", "package2"]]
    assert solve_method(packages, barries) == ["package2"]
