# 064 寻找最大价值的矿堆


## 题目描述

给你一个由0（空地）、1（银矿）、2（金矿）组成的的地图，矿堆只能由上下左右相邻的金矿或银矿连接形成。超出地图范围可以认为是空地。

假设银矿价值1，金矿价值2，请你找出地图中最大价值的矿堆并输出该矿堆的价值。

## 输入描述

地图元素信息如：
```text
22220
00000
00000
11111
```

地图范围最大`300*300`，每个元素的取值范围是0 <= 地图元素 <= 2。

## 输出描述

矿堆的最大价值。

## 示例描述

### 示例一

**输入：**
```text
22220
00000
00000
01111
```

**输出：**
```text
8
```

### 示例二

**输入：**
```text
22220
00020
00010
01111
```

**输出：**
```text
15
```

### 示例三

**输入：**
```text
20000
00020
00000
00111
```

**输出：**
```text
3
```

## 解题思路
深度遍历每一个矿堆，计算矿堆价值

   

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 064_find-max-value
@time:  17/8/2023 上午 11:44
@project:  huawei-od-python 
"""

def solve_method(nums):
    m, n = len(nums), len(nums[0])
    if m < 1:
        return 0

    def infect(row, col, nums, m, n):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or nums[row][col] == 0 or nums[row][col] == -1:
            return 0
        else:
            value = nums[row][col]
            nums[row][col] = -1
            for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                value += infect(row + d1, col + d2, nums, m, n)
            return value

    ans = -1
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 1 or nums[i][j] == 2:
                value = infect(i, j, nums, m, n)
                if value > ans:
                    ans = value
    return ans


if __name__ == '__main__':
    n = int(input().strip())
    nums = [list(map(int, list(input().strip()))) for _ in range(n)]
    res = solve_method(nums)
    print(res)
```

