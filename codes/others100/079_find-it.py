#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 080_find-word
@time:  2023/7/30 16:19
@project:  huawei-od-python
@desc: 079 找到它
"""


def solve_method(matrix, word):
    def dfs(row, col, k, visited):
        # 如果出界、字母已访问过、该位置的字母不是目标字母，则没有找到，继续遍历
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k] or [row, col] in visited:
            return False
        # 添加该字母的坐标存入已访问列表中
        visited.append([row, col])
        # 如果遍历到最后一个单词，则表示找到了单词
        if k == len(word) - 1:
            return True
        # 上下左右进行寻找目标单词的下一个字母
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = dfs(row + d1, col + d2, k + 1, visited)
            if res:
                return res

        return False

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                visited = []
                res = dfs(i, j, 0, visited)
                if res:
                    # 如果找到了，则返回单词首字母的坐标
                    return i + 1, j + 1
    return "NO"


if __name__ == '__main__':
    matrix = ["CPUCY",
              "EKLQH",
              "CHELL",
              "LROWO",
              "DGRBC"]
    assert solve_method(matrix, "HELLOWORLD") == (3, 2)

    matrix = ["CPUCh",
              "wolle",
              "orldo",
              "EKLQo",
              "PGRBC"]
    assert solve_method(matrix, "Helloworld") == "NO"
