# 189 观看文艺汇演问题、最多能看几场演出

## 题目描述

为了庆祝成立100周年，某公园将举行多场文艺表演，很多演出都是同时进行，一个人只能同时观看一场演出，且不能迟到早退，由于演出分布在不同的演出场地，所以连续观看的演出最少有15分钟的时间间隔，小明是一个狂热的文艺迷，想观看尽可能多的演出。

现给出演出时间表，请帮小明计算他最多能观看几场演出。

## 输入描述

第一行是一个数`N`，表示演出场数，其中1 <= N <= 1000。

接下来`N`行，每行两个空格分隔的整数，第一个整数`T`表示演出的开始时间，第二个整数`L`表示演出的持续时间，`T`和`L`的单位为分钟，取值范围是0 <= T <= 1440、0 < L <= 100。

## 输出描述

最多能观看的演出场数。

## 示例描述

### 示例一

**输入：**

```text
2
720 120
840 120
```

**输出：**

```text
1
```

### 示例二

**输入：**

```text
2
0 60
90 60
```

**输出：**

```text
2
```

## 解题思路

1. 将演出的时间段重新按照起止时间存储。
2. 按照演出结束时间进行排序。
3. 遍历所有演出：
    - 如果15分钟能赶得上，则可以看这场演出，计数值累加1。
    - 用`prev_start_time`存储当前演出的结束时间，用于与下场演出的开始时间比较。
4. 返回计数值。    

## 解题代码

```python
def solve_method(show_times):
    times = []
    for start_time, duration in show_times:
        times.append([start_time, start_time + duration])
    
    # 按照结束时间进行排序
    times.sort(key=lambda x: x[1])
    result = 1

    prev_start_time = times[0][1]
    for i in range(1, len(times)):
        start_time, end_time = times[i]
        if start_time - prev_start_time >= 15:
            # 如果15分钟能赶得上，则可以看这场演出
            result += 1
            prev_start_time = end_time

    return result


if __name__ == '__main__':
    show_times = [[720, 120],
                  [840, 120]]
    assert solve_method(show_times) == 1

    show_times = [[0, 60],
                  [90, 60]]
    assert solve_method(show_times) == 2
```

