# 018 任务调度、单核CPU任务调度

## 题目描述

现有一个CPU和一些任务需要处理，已提前获知每个任务的任务ID、优先级、所需执行时间和到达时间。

CPU同时只能运行一个任务，请编写一个任务调度程序，采用“可抢占优先权调度”调度算法进行任务调度，规则如下：

- 如果一个任务到来时，CPU是空闲的，则CPU可以运行该任务直到任务执行完毕。但是如果运行中有一个更高优先级的任务到来，则CPU必须暂停当前任务去运行这个优先级更高的任务。
- 如果一个任务到来时，CPU正在运行一个比它优先级更高的任务时，新到来的任务必须等待。
- 当CPU空闲时，如果还有任务在等待，CPU会从这些任务中选择一个优先级最高的任务执行，相同优先级的任务选择到达时间最早的任务。

## 输入描述

输入有若干行，每一行有四个数字（均小于10^8），分别为任务ID、任务优先级、执行时间和到达时间。

每个任务的任务ID不同，数字越大优先级越高，并且相同优先级的任务不会同时到达。

输入的任务已按照到达时间从小到大排序，并且保证在任何时间，处于等待的任务不超过10000个。

## 输出描述

按照任务执行结束的顺序，输出每个任务的结束时间，输出格式：任务ID 结束时间。

## 示例描述

### 示例一

**输入：**
```text
1 3 5 1
2 1 5 10
3 2 7 12
4 3 2 20
5 4 9 21
6 4 2 22
```

**输出：**
```text
1 6
3 19
5 30
6 32
4 33
2 35
```

## 解题思路

1. 对`tasks`重新生成，便于进入堆，每个元素的4个值分别是任务优先级、到达时间、执行时间和任务ID。
2. 遍历任务列表`tasks`：
    - 获取当前时刻的任务`current_task`。
    - 如果任务不为空，堆顶为优先级最高的任务，获取优先级最高的任务。
    - 如果CPU空闲时间，从等待列表中取出优先级最高的任务执行。
    - 执行任务，运行时间减1，如果执行完毕，则移出等待列表和任务列表，将任务id和当前时间添加到结果列表中。
    - 执行时间加1，继续遍历。
3. 返回结果列表。    

## 解题代码

```python
import heapq


def solve_method(tasks):
    """
    :param tasks: 任务列表：每个元素有4个值，分别是任务ID、任务优先级、执行时间和到达时间
    :return:
    """
    time = 0
    waiting_list = []
    result = []
    # 对tasks重新生成，便于进入堆，每个元素的4个值分别是任务优先级、到达时间、执行时间和任务ID
    for i, task in enumerate(tasks):
        task_id, priority, duration, arrival_time = task
        tasks[i] = [-priority, arrival_time, duration, task_id]

    while len(tasks) > 0:
        current_task = next((task for task in tasks if task[1] == time), None)

        if current_task is not None:
            # 堆顶为优先级最高的任务
            heapq.heappush(waiting_list, current_task)
            # 取出优先级最高的任务执行
            current_task = waiting_list[0]
        else:
            # 空闲时间，从等待列表中取出优先级最高的任务执行
            if len(waiting_list) != 0:
                current_task = waiting_list[0]

        if current_task is not None:
            current_task[2] -= 1
            if current_task[2] == 0:
                # 任务执行完毕
                result.append([current_task[3], time + 1])
                tasks.remove(current_task)
                # 从waiting_list堆中移除掉堆顶优先级最大的元素
                heapq.heappop(waiting_list)

        time += 1

    return result


if __name__ == '__main__':
    tasks = [[1, 3, 5, 1],
             [2, 1, 5, 10],
             [3, 2, 7, 12],
             [4, 3, 2, 20],
             [5, 4, 9, 21],
             [6, 4, 2, 22]]
    assert solve_method(tasks) == [[1, 6], [3, 19], [5, 30], [6, 32], [4, 33], [2, 35]]
```

