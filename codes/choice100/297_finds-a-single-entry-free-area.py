#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 297_finds-a-single-entry-free-area.py
@time: 2023/8/1 14:52
@project: huawei-od-python
@desc: 297 查找单入口空闲区域
"""


def dfs(i, j, count, out):
    # 如果到了边界、遇到了X或已经在连通域中，则直接返回结果。
    if i < 0 or i >= m or j < 0 or j >= n \
            or areas[i][j] == "X" or (i, j) in checked:
        return count

    checked.add((i, j))
    # 当遇到入口时，则加入到结果列表中
    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
        out.append([i, j])

    count += 1
    # 继续对各个方向进行深度优先搜索
    for offsetX, offsetY in directions:
        newI = i + offsetX
        newJ = j + offsetY
        count = dfs(newI, newJ, count, out)

    return count


def solve_method(areas):
    global checked, m, n, directions
    m = len(areas)
    n = len(areas[0])
    checked = set()
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    ans = []

    for i in range(m):
        for j in range(n):
            if areas[i][j] == "O" and (i, j) not in checked:
                out = []
                count = dfs(i, j, 0, out)
                if len(out) == 1:
                    # 只能有一个入口
                    tmp = out[0][:]
                    ans.append((tmp[0], tmp[1], count))

    if len(ans) == 0:
        return "NULL"
    elif len(ans) == 1 or ans[0][2] > ans[1][2]:
        return ans[0]
    elif len(ans) > 1:
        # 如果有多个，取出最大单入口空闲区域
        ans.sort(key=lambda x: -x[2])
        return ans[0][2]


if __name__ == '__main__':
    areas = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "O", "O", "X"],
             ["X", "O", "X", "X"]]
    assert solve_method(areas) == (3, 1, 5)

    areas = [["X", "X", "X", "X", "X"],
             ["O", "O", "O", "O", "X"],
             ["X", "O", "O", "O", "X"],
             ["X", "O", "X", "X", "O"]]
    assert solve_method(areas) == (3, 4, 1)

    areas = [["X", "X", "X", "X"],
             ["X", "O", "O", "O"],
             ["X", "O", "O", "O"],
             ["X", "O", "O", "X"],
             ["X", "X", "X", "X"]]
    assert solve_method(areas) == "NULL"

    areas = [["X", "X", "X", "X"],
             ["X", "O", "O", "O"],
             ["X", "X", "X", "X"],
             ["X", "O", "O", "O"],
             ["X", "X", "X", "X"]]
    assert solve_method(areas) == 3
