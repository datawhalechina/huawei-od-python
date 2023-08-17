# 228 几何平均值最大子数组

## 题目描述
以一个长度为 `N` 的正数数组 `numbers` 中找出长度至少为 `L` 且几何平均值最大子数组，并输出位置和大小。（`K` 个数的几何平均值为 `K` 个数的乘积的 `K` 次方根）

若有多个子数组的几何平均值均为最大值，则输出长度最小的子数组。

若有多个长度相同的子数组的几何平均值均为最大值，则输出最前面的子数组。

## 输入描述
第一行输入为 `N、L，N` 表示`numbers` 的大小 (`1 <= N <= 100000`)，`L` 表示子数组的最小长度 (`1 <= L <= N`)

之后 `N` 行表示 `numbers` 中的 `N` 个数，每个一行 ($10^{-9} \leq numbers[i] \leq 10^9$)。

## 输出描述
输出子数组的位置 (从 `0` 开始计数) 和大小，中间用一个空格隔开

## 说明
用例保证除几何平均值为最大值的子数组外，其他子数组的几何平均值至少比最大值小最大值的 $10^{-10}$ 倍

## 示例描述

### 示例一

**输入：**
```
3 2
2
2
3
```

**输出：**
```
1 2
```

**说明：** 
长度至少为 `2` 的子数组共三个，分别是 {2,2}、{2,3}、{2,2,3}，其中 {2,3}的几何平均值最大，故输出其位置 `1` 和长度 `2`

### 示例二

**输入：**
```
10 2
0.2
0.1
0.2
0.2
0.2
0.1
0.2
0.2
0.2
0.2
```

**输出：**
```
2 2
```

**说明：** 
有多个长度至少为 `2` 的子数组的几何平均值为 `0.2`，其中长度最短的为 `2`，也有多个，长度为 `2` 几何平均值为 `0.2` 的子数组最前面的那个为从第二个数开始的两个 `0.2` 组成的子数组

## 解题代码
``` python
import math

def calc_mean(numbers):
    value = 1.0
    for num in numbers:
        value *= num
    return math.pow(value, 1.0 / len(numbers))

def solve_method(N, L, numbers):
    lo, size = 0, 0
    max_mean = float("-inf")
    for i in range(N - L + 1):
        for j in range(i + L, N + 1):
            # 计算子数组的几何平均值
            mean_value = calc_mean(numbers[i:j])
            if mean_value - max_mean > 1e-5:
                max_mean = mean_value
                lo = i
                size = j - i
            # 题目用例保证几何平均值相差小于等于 1e-10 即为相同
            elif mean_value - max_mean <= 1e-10:
                if j - i < size:
                    lo = i
                    size = j - i

    return (lo, size)

if __name__ == '__main__':
    numbers = [2, 2, 3]
    assert solve_method(3, 2, numbers) == (1, 2)

    numbers = [0.2, 0.1, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.2, 0.2]
    assert solve_method(10, 2, numbers) == (2, 2)
```