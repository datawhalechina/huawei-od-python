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
    def check(row, col, k, visited, word, matrix, m, n):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k] or [row, col] in visited:
            return []
        visited.append([row, col])
        if k == len(word) - 1:
            return [[row, col]]
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = check(row + d1, col + d2, k + 1, visited, word, matrix, m, n)
            if res:
                return [[row, col]] + res
        return []

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                visited = []
                res = check(i, j, 0, visited, word, matrix, m, n)
                if res:
                    return res
    return []


if __name__ == '__main__':
    N = int(input().strip())
    matrix = [input().strip().split(',') for _ in range(N)]
    word = input().strip()
    res = solve_method(matrix, word)
    if res:
        print(','.join([','.join([str(item[0]), str(item[1])]) for item in res]))
    else:
        print('N')
