#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 220_The-number-of-Linux-distributions.py
@time: 2023/7/15
@project: huawei-od-python
@desc: 220 Linux发行版的数量
"""
matrix = []

# DFS搜索函数
def dfs(i, count, visited):
    # 标记节点i已访问
    visited[i] = 1
    # 记录遍历的结点数
    count[0] += 1   
    
    for j in range(N):
        # 对邻接矩阵中相连结点做DFS
        if matrix[i][j] == 1 and visited[j] == 0:
            dfs(j, count, visited)
            
def solution():
    # 初始化访问数组    
    visited = [0] * N  
    res = 0
    
    for i in range(N): 
        # 发现新连通分量进行DFS 
        if visited[i] == 0:
            count = [0]
            dfs(i, count, visited)
            # 记录最大结点数
            res = max(res, count[0])
            
    return res

if __name__ == '__main__':
    while True:
        # 读入数据        
        N = int(input())
        for _ in range(N):
            matrix.append(list(map(int, input().split())))
        
        # 调用函数
        print(solution())
        
        # 判断是否退出
        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break