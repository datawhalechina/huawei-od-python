# 012 乱序整数序列两数之和绝对值最小

## 题目描述

给定一个随机的整数数组（可能存在正整数和负整数）`nums`，请你在该数组中找出两个数，其和的绝对值（`|nums[x]+nums[y]|`）为最小值，并返回这两个数（按从小到大返回）以及绝对值。每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

## 输入描述

一个通过空格分隔的有序整数序列字符串，最多1000个整数，且整数数值范围是[-65535,65535]。

## 输出描述

两个数和两数之和绝对值。

## 示例描述

### 示例一

**输入：**
```text
-1 -3 7 5 11 15
```

**输出：**
```text
-3 5 2
```

**说明：**  
因为`|nums[0]+nums[2]|=|-3+5|=2`最小。

## 解题思路

1. 初始化最小和的绝对值`min_value`、两个数中较小的数`min_num`、两个数中较大的数`max_num`。
2. 遍历数组：
    - 如果两个数不相同，则计算两个数的和的绝对值
    - 与最小值进行比较，如果符合要求，则获取这两个数
3. 返回较小数、较大数、最小和的绝对值。    

## 解题代码

```python
import math


def solve_method(nums):
    min_value = math.inf
    min_num = 0
    max_num = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            a, b = nums[i], nums[j]
            if a != b:
                value = abs(a + b)
                if value < min_value:
                    min_value = value
                    min_num = min(a, b)
                    max_num = max(a, b)

    return [min_num, max_num, min_value]


if __name__ == '__main__':
    assert solve_method([-1, -3, 7, 5, 11, 15]) == [-3, 5, 2]
```

