#!/usr/bin/env python
# encoding: utf-8
"""
@author: libihan
@file: 002_servers-that-can-make-up-a-network.py
@time: 2023/9/3 23:18
@project: huawei-od-python
@desc: 002 可以组成网络的服务器
"""
def solve_method(n, m, servers):
    max_count = 0
    for i in range(n):
        for j in range(m):
            max_count = max(max_count, dfs(i, j, n, m, servers, 0))
    return max_count

def dfs(i, j, n, m, servers, count):
    if i < 0 or i >= n or j < 0 or j >= m or servers[i][j] == 0:
        return count
    count += 1
    # 避免重复计算
    servers[i][j] = 0
    count = dfs(i + 1, j, n, m, servers, count)
    count = dfs(i - 1, j, n, m, servers, count)
    count = dfs(i, j + 1, n, m, servers, count)
    count = dfs(i, j - 1, n, m, servers, count)
    return count

if __name__ == '__main__':
    # n, m = map(int, input().split())
    # servers = []
    # for _ in range(n):
    #     servers.append(list(map(int, input().split())))

    servers1 = [[1, 0],
               [1, 1]]
    assert solve_method(2, 2, servers1) == 3
    servers2 = [[1, 1],
               [1, 0]]
    assert solve_method(2, 2, servers2) == 3