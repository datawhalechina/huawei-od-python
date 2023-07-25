#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 241_searching-land-plot-establishment.py
@time: 2023/7/24
@project: huawei-od-python
@desc: 241 探索地块建立
"""

def solution(mat, n, m, threshold, c):
    ans = 0
    # 遍历矩阵中的每个元素
    for i in range(n - c + 1):
        for j in range(m - c + 1):
            sum = 0

            # 计算以该元素为起点的c*c个元素之和
            for k in range(c):
                for l in range(c):
                    sum += int(mat[i + k][j + l])
            
            # 判断是否超预期
            if sum >= threshold:
                ans += 1

    return ans

if __name__ == '__main__':
    while(True):
        # 处理输入格式
        n, m, c, k = map(int, input().split())
        matrix = [list(input().split()) for _ in range(n)]
        
        print(solution(matrix, n, m, k, c))

        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break