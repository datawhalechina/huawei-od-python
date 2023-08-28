# 152 流水线

## 题目描述

一个工厂有`m`条流水线，来并行完成`n`个独立的作业，该工厂设置了一个调度系统。在安排作业时，总是优先执行处理时间最短的作业。

现给定流水线个数`m`，需要完成的作业数`n`，每个作业的处理时间分别为`t1,t2,...,tn`。请你编程计算处理完所有作业的耗时为多少？

规则如下：
- 当`n>m`时，首先处理时间短的`m`个作业进入流水线，其他的等待。
- 当某个作业完成时，依次从剩余作业中取处理时间最短的进入处理。

## 输入描述

第一行是两个整数（使用空格分隔），分别表示流水线个数`m`和作业数`n`，取值范围是0 < m,n < 100。

第二行输入`n`个整数（使用空格分隔），表示每个作业的处理时长`t1,t2...tn`， 取值范围是0 < t1,t2,...,tn < 100。

## 输出描述

输出处理完所有作业的总时长。 

## 示例描述

### 示例一

**输入：**

```text
3 5
8 4 3 2 10
```

**输出：**

```text
13
```

**说明：**

- 先安排时间为2、3、4的三个作业，第一条流水线先完成作业。
- 调度剩余时间最短的作业8，第二条流水线完成作业。
- 调度剩余时间最短的作业10。

总共耗时是两条流水线完成作业时间，时间为3+10=13。

## 解题思路

首先将作业处理时间按升序排序，然后使用一个列表`pipelines`来表示每个流水线的处理时间。在每次循环中，找到处理时间最短的流水线，将当前作业分配给它，并更新总时长。最后，处理剩余的作业并更新总时长。最后输出总时长。

请注意，该代码没有对输入进行严格的合法性检查，如输入的范围是否满足要求等。在实际应用中，需要根据具体情况进行适当的输入验证和错误处理。

## 解题代码

```python
def calculate_processing_time(m, n, job_times):
    job_times.sort()  # 将作业处理时间按升序排序
    pipelines = [0] * m  # 初始化流水线的处理时间为0
    total_time = 0  # 总时长

    for i in range(n):
        min_pipeline = min(pipelines)  # 找到处理时间最短的流水线
        #total_time += min_pipeline  # 更新总时长
        index = pipelines.index(min_pipeline)  # 找到最短处理时间的流水线的索引
        pipelines[index] += job_times[i]  # 将当前作业分配给最短处理时间的流水线


    total_time += max(pipelines)

    return total_time


# 读取输入
m, n = map(int, input().split())
job_times = list(map(int, input().split()))

# 调用函数计算总时长
total_time = calculate_processing_time(m, n, job_times)

# 输出结果
print(total_time)def solve_method(lights):
    lights_list = []
    for light in lights:
        id = light[0]
        x1 = light[1]
        y1 = light[2]
        x2 = light[3]
        y2 = light[4]
        # id, x坐标的平均值, y坐标的平均值, 灯高半径
        lights_list.append([id, (x1 + x2) // 2, (y1 + y2) // 2, (y2 - y1) // 2])

    # 将灯按行粗排
    lights_list.sort(key=lambda x: x[2])

    result = []

    # 设置每一行的起始索引
    row_start_index = 0
    # 先使用第1行第1个作为基准灯
    for i in range(1, len(lights_list)):
        # 高低偏差超过灯高度的一半
        if lights_list[i][2] - lights_list[row_start_index][2] > lights_list[row_start_index][3]:
            # 把之前的灯按x坐标排序，并存入结果列表中
            lights_list[row_start_index:i] = sorted(lights_list[row_start_index:i], key=lambda x: x[1])
            result.extend([light[0] for light in lights_list[row_start_index:i]])
            # 记录新一行对应的灯位置
            row_start_index = i

    # 把该行剩余的灯全部加入到结果列表中
    lights_list[row_start_index:] = sorted(lights_list[row_start_index:], key=lambda x: x[1])
    result.extend([light[0] for light in lights_list[row_start_index:]])

    return result
```

