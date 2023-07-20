# 127 最短耗时

## 题目描述

给定一个正整型数组，表示待系统执行的任务列表，数组的每一个元素代表一个任务，元素的值表示该任务的类型。请计算执行完所有任务所需的最短时间。

任务执行规则如下：
1. 任务可以按任意顺序执行，且每个任务执行消耗时间均为1个时间单位。
2. 两个同类型的任务之间必须有长度为`N`个单位的冷却时间，比如`N`为2时，在时间`K`执行了类型3的任务，那么`K+1`和`K+2`两个时间不能执行类型3的任务。
3. 系统在任何一个单位时间内都可以执行一个任务，或者等待状态。

**说明：** 数组最大长度为1000，数组元素的值最大为1000。

## 输入描述

第1行记录一个用`,`分割的数组，数组长度不超过1000，数组元素的值不超过1000。

第2行记录任务冷却时间，`N`为正整数，其中，N <= 100。

## 输出描述

输出为执行完所有任务所需的最短时间。

## 示例描述

### 示例一

**输入：**
```text
2,2,2,3
2
```

**输出：**
```text
6
```

**说明：**
任务调度可以为[2,_,_,2,3,2]，故最短耗时为6。

## 解题思路

1. 计算任务频次，记作字典`task_count`，其中`key`为任务类型，`value`为任务次数。
2. 记录最大任务数，表示`max_count`；最大任务数的任务类型，表示`max_task_type`。
3. 计算出现次数最多的任务的耗时`result`，可表示为`(max_count - 1) * (N + 1) + 1`，其中`N`为冷却时间。有`max_count`个冷却耗时。
4. 遍历任务频次：
    - 插入其他任务，过滤掉最大任务数的任务类型。
    - 如果还有冷却耗时的次数，将其他任务插入进去，减去冷却时间。
    - 如果没有冷却耗时的次数，直接加入任务耗时（1个单位时间）。
5. 返回计算之后的任务耗时，为最短耗时。

## 解题代码

```python
from collections import defaultdict


def solve_method(tasks, N):
    # 计算任务频次
    task_count = defaultdict(int)
    for task in tasks:
        task_count[task] += 1
    # 记录最大任务数
    max_count = max(task_count.values())
    # 得到最大任务数的任务类型
    max_task_type = [key for key, value in task_count.items() if value == max_count][0]

    # 计算出现次数最多的任务的耗时
    result = (max_count - 1) * (N + 1) + 1
    # 计算冷却时间占用的次数
    free_pos = max_count - 1
    for task_type, count in task_count.items():
        # 插入其他任务
        if task_type != max_task_type:
            # 如果还有空位数，插入进去，减去冷却时间
            for _ in range(count):
                if free_pos > 0:
                    free_pos -= 1
                    result = result - N + 1
                else:
                    # 继续插入其他
                    result += 1

    return max(result, len(tasks))


if __name__ == '__main__':
    assert solve_method([2, 2, 2, 3], 2) == 6
    assert solve_method([2, 2, 2, 3, 3, 1], 2) == 6
    assert solve_method([2, 2, 2, 3, 3, 3], 2) == 6
    assert solve_method([2, 2, 1], 3) == 3
```