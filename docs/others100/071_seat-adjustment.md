# 071 座位调整

## 题目描述

疫情期间课堂的座位进行了特殊的调整，不能出现两个同学紧挨着，必须隔至少一个空位。

给你一个整数数组`desk`表示当前座位的占座情况，由若干0和1组成，其中0表示没有占位，1表示占位。在不改变原有座位秩序情况下，还能安排坐几个人？

## 输入描述

第一行是个数组表示座位占座情况，由若干0和1组成，其中0表示没有占位，1表示占位

## 输出描述

输出数值表示还能坐几个人

**说明：**

1 <= desk.length <= 2*10^4

## 示例描述

### 示例一

**输入：**
```text
1 0 0 0 1
```

**输出：**
```text
1
```

**说明：**

只有`desk[2]`的位置可以坐一个人。

### 示例二

**输入：**
```text
0 0 0 0 0
```

**输出：**
```text
3
```

## 解题思路
数组长度为n，则最多可以坐n//2 + 1人，首先判断首位是否可以再坐人，之后遍历数组，使用贪心算法，越靠左侧位置可以
再坐人，优先安排。

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 071_seat-adjustment
@time:  24/8/2023 上午 10:31
@project:  huawei-od-python 
"""


def solve_method(nums):
    if len(nums) < 3:
        if sum(nums) > 0:
            return 0
        else:
            return 1
    if sum(nums) >= len(nums) // 2 + 1:
        return 0
    ans = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            continue
        elif i == 0 and nums[i + 1] == 0:
            ans += 1
            nums[i] = 1
        elif i == n - 1 and nums[i - 1] == 0:
            ans += 1
        else:
            if nums[i - 1] == 0 and nums[i + 1] == 0:
                ans += 1
                nums[i] = 1
    return ans


if __name__=='__main__':
    nums = list(map(int,input().strip().split(' ')))
    res = solve_method(nums)
    print(res)

```

