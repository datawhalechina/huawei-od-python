#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 223_Cloud-SMS-platform-promotional-activity.py
@time: 2023/7/24
@project: huawei-od-python
@desc: 223 Excel 云短信平台优惠活动
"""
max_g = 0

def solution(mesCount, n, lst, index):
    global max_g

    # 预算已耗光，计算当前总条数，并记录最大值
    if n == 0:
        count = sum(lst)
        max_g = max(max_g, count)
    else:
        for i in range(index, len(mesCount)):
            x = int(mesCount[i])
            lst.append(x)
            solution(mesCount, n - (i + 1), lst, i + 1) # 继续遍历所有可能性
            lst.pop()

if __name__ == '__main__':
    while(True):
        # 处理输入格式
        M = int(input())
        P = input().split()

        solution(P, M, [], 0)

        print(max_g)

        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break