# 153 滑动窗口

## 题目描述

有一个`N`个整数的数组，和一个长度为`M`的窗口。窗口从数组内的第一个数开始滑动，直到窗口不能滑动为止。每次滑动产生一个窗口和窗口内所有数的和，求窗口滑动产生的所有窗口和的最大值。

## 输入描述

第一行输入一个正整数`N`，表示整数个数，取值范围是0 < N < 100000。 

第二行输入`N`个整数，整数取值范围`[-100,100]`。

第三行输入正整数`N`，表示窗口的大小，取值范围是M <= N <= 100000。

## 输出描述

窗口滑动产生所有窗口和的最大值。

## 示例描述

### 示例一

**输入：**

```text
6
12 10 20 30 15 23
3
```

**输出：**

```text
68
```

## 解题思路

1. 当滑动窗口大于数组长度，则返回数组所有元素之和。
2. 遍历数组：计算滑动窗口内的和，并比较大小，取最大和。
3. 返回结果，即窗口滑动产生所有窗口和的最大值。

## 解题代码

```python
import math


def solve_method(nums, window_size):
    if window_size > len(nums):
        return sum(nums)

    max_sum = - math.inf
    for i in range(len(nums) - window_size + 1):
        max_sum = max(max_sum, sum(nums[i:i + window_size]))

    return max_sum


if __name__ == '__main__':
    assert solve_method([12, 10, 20, 30, 15, 23], 3) == 68
```

