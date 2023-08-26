# 200 身高体重排序

## 题目描述

某学校举行运动会，学生们按编号（1、2、3、...、n）进行标识，现需要按照身高由低到高排列，对身高相同的人，按体重由轻到重排列，对于身高体重都相同的人，维持原有的编号顺序关系，请输出排列后的学生编号。

## 输入描述

两个序列，每个序列由`n`个正整数组成（0 < n < 100）。

第一个序列中的数值代表身高，第二个序列中的数值代表体重。

## 输出描述

排列结果，每个数值都是原始序列中的学生编号，编号从1开始。

## 示例描述

### 示例一

**输入：**

```text
3
90 110 90 
45 60 45
```

**输出：**

```text
132
```

## 解题思路

首先定义了一个函数 `solve_method`，该函数接受三个参数：人数 `n`、身高列表 `height` 和体重列表 `weight`。然后，在循环中，对于每个人，将其身高、体重和索引信息封装为元组，添加到名为 `arr1` 的列表中。接下来，使用 `sorted` 函数对 `arr1` 进行排序，排序依据是元组中的身高。排序后的结果被存储在名为 `arr2` 的列表中。主程序部分首先从输入中获取人数、身高列表和体重列表，然后调用 `solve_method` 函数，获取按照身高排序后的人的信息列表。最后，通过遍历 `arr2` 列表，输出每个人的索引，实现了根据身高排序并输出索引的功能。

## 解题代码

```python
def solve_method(n, height, weight):
    arr1 = []
    for i in range(n):
        arr1.append(((height[i], weight[i]),i+1))

    arr2 = sorted(arr1, key=lambda x: x[0])
    return arr2


n = int(input())
height = list(map(int, input().split()))
weight = list(map(int, input().split()))
arr2 = solve_method(n, height, weight)
for i in arr2:
    print(i[1], end='')
                                         
```

