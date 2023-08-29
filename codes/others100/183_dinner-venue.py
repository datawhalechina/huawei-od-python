#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 183_dinner-venue.py
@time: 2023/8/27 1:27
@project: huawei-od-python
@desc: 183 聚餐地点、快乐的周末
"""

from collections import deque


def solve_method(arr):
    m = len(arr)
    n = len(arr[0])
    # 起始地点
    start_spots = []
    # 聚会地点
    end_spots = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 2:
                start_spots.append((i, j))
            elif arr[i][j] == 3:
                end_spots.append((i, j))
    count = 0

    def bfs(row, col, end_spot):
        # 待遍历的地点
        queue = deque([(row, col)])
        # 已访问的地点
        visited = {(row, col)}
        while queue:
            r, c = queue.popleft()

            # 能到达聚会地点，返回True
            if (r, c) == end_spot:
                return True
            # 访问上下左右的地点
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # 如果超出边界，或者遇到障碍物，则继续遍历
                if not (0 <= nr < m and 0 <= nc < n) or arr[nr][nc] == 1:
                    continue
                if (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        # 当所有地点都访问过，当还是没有到达聚会地点，返回False
        return False

    for end_spot in end_spots:
        if all(bfs(start_spot[0], start_spot[1], end_spot) for start_spot in start_spots):
            count += 1

    return count


if __name__ == '__main__':
    arr = [[2, 1, 0, 3],
           [0, 1, 2, 1],
           [0, 3, 0, 0],
           [0, 0, 0, 0]]
    assert solve_method(arr) == 2
