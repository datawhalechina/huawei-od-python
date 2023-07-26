# 224 任务混部

## 题目描述

公司创新实验室正在研究如何最小化资源成本，最大化资源利用率，请你设计算法帮他们解决一个任务混部问题：有`taskNum`项任务，每个任务有开始时间（`startTime`），结束时间（`endTime`），并行度（`parallelism`）三个属性，并行度是指这个任务运行时将会占用的服务器数量，一个服务器在每个时刻可以被任意任务使用但最多被一个任务占用，任务运行完会立即释放（结束时刻不占用）。任务混部问题是指给定一批任务，让这批任务由同一批服务器承载运行，请你计算完成这批任务混部最少需要多少服务器，从而最大化控制资源成本。

## 输入描述

第一行输入为`taskNum`，表示有`taskNum`项任务接下来`taskNum`行，每行三个整数，表示每个任务的开始时间(`startTime`)，结束时间(`endTime`)，并行度(`parallelism`)

## 输出描述

一个整数，表示最少需要的服务器数量

## 示例描述

### 示例一

**输入**
```
3
2 3 1
6 9 2
0 5 1
```

**输出**
```
2
```

**说明**
一共有三个任务，第一个任务在时间区间`[2，3)`运行，占用1个服务器，第二个任务在时间区间`[6,9)`运行，占用2个服务器，第二个任务在时间区间`[0,5)`运行，占用1个服务器，需要最多服务器的时间区间为`[2，3)`和`[6,9)`，需要2个服务器。

### 示例二

**输入**
```
2
3 9 2
4 7 3
```

**输出**
```
5
```

**说明**
一共有两个任务，第一个任务在时间区间`[3，9)`运行，占用2个服务器，第二个任务在时间区间`[4,7)`运行，占用3个服务器，需要最多服务器的时间区间为`[4，7)`，需要5个服务器。

## 备注
`1 <= taskNum <= 100000`
`0 <= startTime < endTime <= 50000`

## 解题思路

**一种解题步骤**
1. 用优先级队列元素来代表占用服务器，记录的元素为释放服务器的时间。
2. 将所有任务按照开始顺序，投入优先级队列，并行度即当前任务所需要的服务器数量。
3. 如果当前优先级队列中记录的释放时间，小于当前任务的开始时间，则释放该服务器。
4. 每次投入一个任务后，比较最少需要的服务器数量，记录最大值即为所求。

## 解题代码
``` python
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
```