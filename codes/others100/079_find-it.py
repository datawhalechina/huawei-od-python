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
    def check(row, col, k, visited, word, matrix, m, n):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k] or [row, col] in visited:
            return False
        visited.append([row, col])
        if k == len(word) - 1:
            return True
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = check(row + d1, col + d2, k + 1, visited, word, matrix, m, n)
            if res:
                return res
        return False

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                visited = []
                res = check(i, j, 0, visited, word, matrix, m, n)
                if res:
                    return [i + 1, j + 1]
    return []


if __name__ == '__main__':
    M, N = input().strip().split(' ')
    word = input().strip()
    matrix = [list(input().strip()) for _ in range(int(N))]
    res = solve_method(matrix, word)
    if res:
        print(' '.join([str(res[0]), str(res[1])]))
    else:
        print('NO')
