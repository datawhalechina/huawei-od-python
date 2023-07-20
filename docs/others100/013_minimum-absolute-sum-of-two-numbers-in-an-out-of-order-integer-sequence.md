# 013-乱序整数序列两数之和绝对值最小

## 题目描述

给定一个随机的整数数组（可能存在正整数和负整数）nums,
请你在该数组中找出两个数，其和的绝对值(|nums[x]+nums[y]|)为最小值
并返回这两个数（按从小到大返回）以及绝对值。
每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

## 输入描述

一个通过空格空格分割的有序整数序列字符串，最多1000个整数，
且整数数值范围是[-65535,65535]

## 输出描述

两个数和两数之和绝对值

## 示例描述

### 示例一

**输入：**
```
-1 -3 7 5 11 15
```

**输出：**
```
-3 5 2
```

**说明：**  
因为|nums[0]+nums[2]| = | -3+5 |=2最小

## 解题思路

1. 将字符串按空格分隔为整数列表。
2. 去重后枚举列表中的数，找到其中和绝对值最小的两个数，记录它们和的绝对值和这两个数。
3. 输出这两个数和它们的和。

### 核心知识点

1. Python中列表的去重可以使用set()函数或list(set()),前者返回集合，后者返回列表。
2. Python中不需要导入java.util.*,可直接使用内置函数和模块。例如，Math.abs()可以替换为abs(),Arrays.stream()可以替换为
   map()函数，等等。
3. sys.maxsize是Python中的一个常量，表示能表示的最大整数。

## 解题代码

```python
# coding: utf-8
import sys

def solve_method(nums_str):
    # 将输入的数字字符串转换为整数列表
    nums = list(map(int, nums_str.split()))
    # 去除重复的数字
    nums = list(set(nums))
    # 初始化最小和为系统最大值
    min_sum = sys.maxsize
    # 初始化结果集合
    res_set = set()
    # 遍历数字列表
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            a, b = nums[i], nums[j]
            if a != b:
                # 计算当前两个数字的绝对值和
                cur_sum = abs(a + b)
                if cur_sum < min_sum:
                    # 如果当前和小于最小和，则更新最小和和结果集合
                    min_sum = cur_sum
                    res_set = set([a, b])
    # 如果结果集合不为空，则输出结果集合中的数字和最小和
    if len(res_set) != 0:
        print(*res_set, min_sum)

if __name__ == "__main__":
    # 输入数字字符串，调用 solve_method 函数进行处理
    nums_str = input()
    solve_method(nums_str)
```

