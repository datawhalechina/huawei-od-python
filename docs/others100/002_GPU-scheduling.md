# 002 GPU调度

## 题目描述
为了充分发挥GPU算力，需要尽可能多的将任务交给GPU执行，现在有一个任务数组，数组元素表示在这1s内新增的任务个数，且每秒都有新增任务。假设GPU最多一次执行n个任务，一次执行耗时1s，在保证GPU不空闲的情况下，最少需要多长时间执行完成。

## 输入描述

第一个参数表示GPU最多执行的任务个数，取值范围为1\~10000。

第二个参数表示任务数组的长度，取值范围为1\~10000。

第三个参数表示任务数组， 数字范围为1\~10000。

## 输出描述
执行完所有任务需要多少秒。

## 示例描述

### 示例一

**输入：**
```text
3
5
1 2 3 4 5
```

**输出：**
```text
6
```

**说明：**  
一次最多执行3个任务，最少耗时6s。

### 示例二

**输入：**
```text
4
5
5 4 1 1 1
```

**输出：**
```text
5
```

**说明：**  
一次最多执行4个任务，最少耗时5s。

## 解题思路

1. 初始化总运行时间`total_time`和等待时间`remaining_time`。
2. 遍历所有作业，计算等待时间。
3. 继续等待作业完成，每载入n个作业，总时间累加1。
4. 返回总运行时间。

## 解题代码

```python
def solve_method(n, jobs):
    # 初始化总运行时间和等待时间
    total_time, remaining_time = 0, 0
    for job in jobs:
        if job + remaining_time > n:
            # 计算等待时间
            remaining_time = job + remaining_time - n
        else:
            # 无需等待
            remaining_time = 0
        total_time += 1

    # 继续等待作业完成，每载入n个作业，总时间累加1
    while remaining_time > 0:
        remaining_time -= n
        total_time += 1

    return total_time


if __name__ == '__main__':
    assert solve_method(3, [1, 2, 3, 4, 5]) == 6
    assert solve_method(4, [5, 4, 1, 1, 1]) == 5
```

