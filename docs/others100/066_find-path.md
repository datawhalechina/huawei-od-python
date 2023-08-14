# 066 寻找路径

## 题目描述

二叉树也可以用数组来存储，给定一个数组，树的根节点的值储存在下标1，
对于储存在下标n的节点，他的左子节点和右子节点分别储存在下标2n和2n+1，并且我们用-1代表一个节点为空。
给定一个数组存储的二叉树，试求从根节点到最小的叶子节点的路径，路径由节点的值组成。


## 输入描述
输入一行为数组的内容，数组的每个元素都是正整数，元素间用空格分割。
注意第一个元素即为根节点的值，即数组的第n元素对应下标n。
下标0在树的表示中没有使用，所以我们省略了。
输入的树最多为7层。

## 输出描述
输出从根节点到最小叶子节点的路径上各个节点的值，由空格分割，用例保证最小叶子节点只有一个

## 示例描述

### 示例一

**输入：**
```text
3 5 7 -1 -1 2 4
```

**输出：**
```text
3 7 2
```

### 示例二

**输入：**
```text
5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6
```

**输出：**
```text
5 8 7 6
```

## 解题思路
首先根据元素个数n(包含-1)确定树的深度depth，depth=log2(n+1)向上取整,根据树的深度可以确定哪些是叶节点，
选出值最小的叶节点，然后记录根节点到叶节点的值

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 066_find-path
@time:  14/8/2023 下午 2:51
@project:  huawei-od-python 
"""
import math


def solve_method(nums):
    depth = math.ceil(math.log2(len(nums)))  # nums第一个元素无意义，为额外添加元素，目的是对齐下标
    start = 2 ** (depth - 1)
    min_value, index = float('inf'), -1
    for i in range(start, len(nums)):
        if nums[i] != -1 and nums[i] < min_value:
            min_value, index = nums[i], i
    path = []
    while index > 0:
        path.append(nums[index])
        index = index // 2
    return path[::-1]


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(' ')))
    nums.insert(0, 0)
    res = solve_method(nums)
    print(res)


```

