#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 154_mars-transformation.py
@time: 2023/8/29 0:19
@project: huawei-od-python
@desc: 154 火星改造、宜居星球改造计划
"""


def solve_method(grid):
    rows, cols = len(grid), len(grid[0])
    # 已经访问过的区域的位置
    visited = set()
    # 待处理的区域
    queue = []
    days = 0
    # 当前可居住区域的数量
    count = 0

    # 将所有初始的YES区域加入队列
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'YES':
                queue.append((i, j))
                visited.add((i, j))
                count += 1

    # 使用BFS扩展可居住区域
    while queue and len(visited) != rows * cols:
        days += 1
        size = len(queue)
        for _ in range(size):
            x, y = queue.pop(0)
            count -= 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 'NO' and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    count += 1

        if count == 0:
            break

    # 检查是否所有的NO区域都被转化成YES
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'NO' and (i, j) not in visited:
                return -1

    return days


if __name__ == '__main__':
    grid = [["YES", "YES", "NO"],
            ["NO", "NO", "NO"],
            ["YES", "NO", "NO"]]
    assert solve_method(grid) == 2

    grid = [["YES", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"]]
    assert solve_method(grid) == 6

    grid = [["NO", "NA"]]
    assert solve_method(grid) == -1

    grid = [["YES", "NO", "NO", "YES"],
            ["NO", "NO", "YES", "NO"],
            ["NO", "YES", "NA", "NA"],
            ["YES", "NO", "NA", "NO"]]
    assert solve_method(grid) == -1
