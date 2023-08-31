#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 045_calculate-network-signal.py
@time: 2023/8/22 19:11
@project: huawei-od-python
@desc: 045 计算网络信号
"""


class Block:
    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value


def solve_method(nums, dest):
    source = [0, 0]
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] > 0:
                source = [i, j]

    blocks = [Block(source[0], source[1], nums[source[0]][source[1]])]
    visited = [[0] * len(nums[0]) for _ in range(len(nums))]
    while len(blocks) > 0:
        block = blocks.pop(0)
        diffuse(nums, blocks, visited, block.i, block.j, block.value)
    return nums[dest[0]][dest[1]]


def diffuse(nums, blocks, visited, i, j, value):
    for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= i + x < len(nums) and 0 <= j + y < len(nums[0]) and visited[i + x][j + y] == 0:
            visited[i + x][j + y] = 1
            if nums[i + x][j + y] == 0:
                nums[i + x][j + y] = value - 1
            if nums[i + x][j + y] > 1:
                blocks.append(Block(i + x, j + y, nums[i + x][j + y]))


if __name__ == "__main__":
    # 6 5
    # 0 0 0 -1 0 0 0 0 0 0 0 0 -1 4 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0
    # 1 4
    # m, n = map(int, input().strip().split())
    # array = list(map(int, input().strip().split()))
    # nums = [array[i:i + n] for i in range(0, len(array), n)]

    # 目的单元格
    # dest = list(map(int, input().strip().split()))
    # print(solve_method(nums, dest))

    grid = [[0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, -1, 4, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0]]

    assert solve_method(grid, [1, 4]) == 2

    grid = [[0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, -1, 4, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0]]
    assert solve_method(grid, [2, 1]) == 0
