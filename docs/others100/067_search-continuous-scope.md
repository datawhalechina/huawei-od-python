# 067 寻找连续区间

## 题目描述

给定一个含有N个正整数的数组，
求出有多少个连续区间(包括单个正整数)，它们的和大于等于x。

## 输入描述
第一行两个整数N与x (0 < N <= 100000 , 0 <= x <= 10000000 )。第二行有N个正整数(每个正整数小于等于100)。

## 输出描述
输出一个整数，表示所求的个数。
## 示例描述

### 示例一

**输入：**
```text
3 7
3 4 7
```

**输出：**
```text
4
```

### 示例二

**输入：**
```text
10 10000000
1 2 3 4 5 6 7 8 9 10
```

**输出：**
```text
0
```

## 解题思路
遍历以每个位置为起点的子数组，如果当前字数组的和已经超过目标值，往后添加正整数元素的字数组必定也超过目标值。
   

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 067_search-continuous-scope
@time:  13/8/2023 下午 11:38
@project:  huawei-od-python 
"""


def solve_method(nums, target):
    n = len(nums)
    ans = 0
    if sum(nums) < target:
        return ans
    for i in range(n):
        for j in range(i + 1, n + 1):
            if sum(nums[i:j]) >= target:
                ans += n - j + 1
                break
    return ans

if __name__ == '__main__':
    N, x = list(map(int, input().strip().split(' ')))
    nums = list(map(int, input().strip().split(' ')))
    res = solve_method(nums, x)
    print(res)

```

