#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 221_the-road-to-work.py
@time: 2023/7/23
@project: huawei-od-python
@desc: 221 上班之路
"""
from collections import defaultdict

# DFS搜索函数
def dfs(i, j, ut, uc, last_dir, path):
    # 达到目标(公司) return True
    if matrix[i][j] == 'T':
        return True 

    # 使用DFS的方式，尝试四个方向 上、下、左、右，i是行，j是列
    for di, dj, dir in [(-1, 0, 1), (1, 0, 2), (0, -1, 3), (0, 1, 4)]:        
        # 计算下一个位置的新 行、列值
        newI, newJ = i + di, j + dj  
        
        # 检查边界以及是否已访问
        if 0 <= newI < N and 0 <= newJ < M:
            pos = newI * M + newJ # 计算新位置的值
            if pos in path:  
                continue
            
            flagT = 0
            # 检查转向次数，如果还有次数可以记录消耗次数
            if last_dir and last_dir != dir:
                if ut + 1 > T: continue
                flagT = 1
                
            flagC = 0
            # 检查清障次数，如果还有次数可以记录消耗次数
            if matrix[newI][newJ] == '*':
                if uc + 1 > C: continue
                flagC = 1
                
            # 添加坐标到访问记录
            path.add(pos)  
            
            # DFS递归，继续走看能否到达 ‘T’
            ut, uc = ut + flagT, uc + flagC
            if dfs(newI, newJ, ut, uc, dir, path):
                return True

            # 回溯移除坐标，减去未成功消耗的次数
            path.remove(pos)
            ut, uc = ut - flagT, uc - flagC
            
    return False

def solution(M , N, matrix):
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'S':                
                # 从起点(Jungle的家)开始DFS
                path = set()
                path.add(i * M + j)  # 使用 i * M + j 来表示具体位置
                return "YES" if dfs(i, j, 0, 0, 0, path) else  "NO"
            
    return "NO"

if __name__ == '__main__':
    # 输入参数，按照格式，分别代表 转弯次数、清障次数、地图 行、列
    T, C = map(int, input().split())  
    N, M = map(int, input().split())
    # 将地图内容读取成为矩阵列表
    matrix = [list(input()) for _ in range(N)]

    print(solution(M, N, matrix))