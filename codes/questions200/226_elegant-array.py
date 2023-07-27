#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 226_elegant-array.py
@time: 2023/7/27
@project: huawei-od-python
@desc: 226 优雅数组
"""

def solution(arr, n, k):
    res = 0

    # i是子数组起点
    for i in range(n):
        # 统计 arr元素出现次数 的字典容器
        count = {}

        # j是子数组终点
        for j in range(i, n):
            key = arr[j]
            # 增加具体元素的计数
            count[key] = count.get(key, 0) + 1
            # 出现了k次即记录满足要求的子数组个数
            if count[key] >= k:
                # 自j后的子数组均满足要求
                res += n - j
                break

    return res

if __name__ == '__main__':
    while(True):
        # 处理输入格式
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        print(solution(arr, n, k))

        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break