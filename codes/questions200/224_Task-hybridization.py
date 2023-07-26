#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 224_Task-hybridization.py
@time: 2023/7/25
@project: huawei-od-python
@desc: 224 任务混部
"""
import heapq

def solution(tasksInfo, taskNum):
    # 按任务的 开始时间 进行排序
    tasksInfo.sort(key = lambda task:task[0])

    # 初始化优先级队列
    priorityQ = []
    result = 0

    # 遍历每个任务
    for i in range(taskNum):
        # 当优先级队列中元素 小于 当前任务的开始时间，说明该任务占用的服务器可释放
        while priorityQ and priorityQ[0] <= tasksInfo[i][0]:
            heapq.heappop(priorityQ)

        # 将 当前要执行的任务 的 结束时间，丢入优先级队列
        for j in range(tasksInfo[i][2]):
            heapq.heappush(priorityQ, tasksInfo[i][1])

        # 记录优先级长度，即占用服务器的最大个数
        result = max(result, len(priorityQ))
    return result

if __name__ == '__main__':
    while(True):
        # 处理输入格式
        taskNum = int(input())
        tasksInfo = [list(map(int, input().split())) for _ in range(taskNum)]

        print(solution(tasksInfo, taskNum))

        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break