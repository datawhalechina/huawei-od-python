#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 026_optimal-resource-allocation.py
@time: 2023/8/17 14:08
@project: huawei-od-python
@desc: 026 最优资源分配
"""


def solve_method(M, N, config):
    cores = [M] * N
    used = [1, 2, 8]
    for c in config:
        cur = used[ord(c) - ord('A')]
        # 资源分配规则：按芯片编号从小到大分配资源
        for i in range(N):
            # 当前芯片容量，满足用户配置
            if cores[i] >= cur:
                cores[i] -= cur
                break
    return ['1' * (M - core) + '0' * core for core in cores]


if __name__ == "__main__":
    # 8
    # 2
    # ACABA
    # M = int(input())
    # N = int(input())
    # config = input().strip()
    # for core in solve_method(M, N, config):
    #     print(core)
    assert solve_method(8, 2, "ACABA") == ["11111000", "11111111"]
    assert solve_method(8, 2, "ACBCB") == ["11111000", "11111111"]
