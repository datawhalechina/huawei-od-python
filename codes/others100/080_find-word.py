#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 080_find-word
@time:  30/7/2023 下午 4:19
@project:  huawei-od-python 
"""


def solve_method(matrix, word):
    def check(row, col, k, word, matrix, m, n):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k]:
            return []
        if k == len(word) - 1:
            return [[row, col]]
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = check(row + d1, col + d2, k + 1, word, matrix, m, n)
            if res:
                return [[row, col]] + res
        return []

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                res = check(i, j, 0, word, matrix, m, n)
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
