# 266 任务总执行时长

## 题目描述

任务编排服务负责对任务精选组合调度。参与编排的任务有两种类型，其中一种任务执行时长为`taskA`，另一种执行时长为`taskB`。任务一旦开始执行不能被打断，且任务可连续执行。服务每次可以编排`num`个任务。

请编写一个方法，生成每次编排后的任务所有可能的总执行时长。

## 输入描述

一行输入三个数字，第一个数字表示第一种任务`taskA`的执行时长，第二个数字表示第二种任务`taskB`的执行时长，第三个数字表示要编排的任务个数`num`，并以逗号分隔。

## 输出描述

数组形式返回所有总执行时长，需要按从小到大排列。

## 示例描述

### 示例一

**输入：**
```
1,2,3
```

**输出：**
```
[3, 4, 5, 6]
```

**说明：**
一共有4次任务编排的总时长，分别是3、4、5、6，其中：
- 可以执行3次`taskA`，得到结果3
- 可以执行2次`taskA`和1次`taskB`，得到结果4
- 可以执行1次`taskA`和2次`taskB`，得到结果5
- 可以执行3次`taskB`，得到结果6

## 解题思路

1. 分别从输入字符串中读取`taskA`和`taskB`的执行时长、要编排的任务个数`num`。
2. 观察输出可知，可用循环依次递减计算`taskA`的执行次数的时长，并加上依次递增的`taskB`的执行次数的时长，可得到单次计算时长的关系式：
$$
\text{total_time} = i \dot \text{taskA} + (\text{num} - i) \dot \text{taskB}    
$$
3. 将单次时长存放到数组中，由于需要去重和排序，可将数组用`set`进行去重，并使用`sorted`进行排序，得到结果。   

## 解题代码

```python
def solve_method(string):
    str_list = string.split(",")
    taskA = int(str_list[0])
    taskB = int(str_list[1])
    num = int(str_list[2])

    result = []
    for i in range(num + 1):
        total_time = i * taskA + (num - i) * taskB
        result.append(total_time)

    return sorted(list(set(result)))


if __name__ == '__main__':
    assert solve_method("1,2,3") == [3, 4, 5, 6]
```