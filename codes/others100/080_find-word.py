#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 080_find-word
@time:  2023/7/30 16:19
@project:  huawei-od-python
@desc: 080 找单词
"""


def solve_method(matrix, word):
    def dfs(row, col, k, visited, word):
        # 如果出界、字母已访问过、该位置的字母不是目标字母，则没有找到，继续遍历
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k] or [row, col] in visited:
            return []
        # 添加该字母的坐标存入已访问列表中
        visited.append([row, col])
        # 如果遍历到最后一个单词，则表示找到了单词，返回该字母的坐标
        if k == len(word) - 1:
            return [[row, col]]
        # 上下左右进行寻找目标单词的下一个字母
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = dfs(row + d1, col + d2, k + 1, visited, word)
            if res:
                return [[row, col]] + res
        return []

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                visited = []
                res = dfs(i, j, 0, visited, word)
                if res:
                    # 如果找到了，则返回单词的所有坐标
                    return [i for x in res for i in x]
    return "N"


if __name__ == '__main__':
    matrix = [["A", "C", "C", "F"],
              ["C", "D", "E", "D"],
              ["B", "E", "S", "S"],
              ["F", "E", "C", "A"]]
    assert solve_method(matrix, "ACCESS") == [0, 0, 0, 1, 0, 2, 1, 2, 2, 2, 2, 3]
