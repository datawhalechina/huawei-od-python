#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 240_Express-delivery-allocation-problem.py
@time: 2023/7/25
@project: huawei-od-python
@desc: 240 快递投放问题
"""
from typing import List, Dict, Set, Tuple
from collections import defaultdict
import sys

def solution(want: List[List[str]], cant: List[List[str]]) -> str:
    # 初始化包裹道路信息的 字典 和 无法通行的道路字典
    want_map: Dict[str, Set[str]] = defaultdict(set)
    cant_map: Dict[str, Set[str]] = defaultdict(set)

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

    res: List[str] = []
    for path, want_pkg in want_map.items():
        # 遍历包裹道路信息，在不可通行信息中找 key = 道路
        cant_pkg = cant_map.get(path)

        if cant_pkg is None:
            continue

        # 如果不可通行信息中有对应的包裹，则该包裹不可送达，需记录在结果中
        for pkg in want_pkg:
            if pkg in cant_pkg:
                res.append(pkg)
    
    if not res:
        return "none"

    # 按照包裹序列进行排序
    res.sort(key=lambda s: int(s[7:]))

    return " ".join(res)

if __name__ == '__main__':
    while(True):
        # 处理输入格式
        m, n = map(int, input().split())
        packages = [input().split() for _ in range(m)]
        barries = [input().split() for _ in range(n)]

        print(solution(packages, barries))

        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break