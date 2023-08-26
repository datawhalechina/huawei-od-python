# 198 踢石子问题

## 题目描述

有一堆石子，一次编号1-100围成圈，给定一个数`K`，从1开始数`K`个，将此石子踢出，继续报数，最后当石子总数小于`K`时，输出最后剩余石子编号。

## 输入描述

输入`K`，例如`K`为3。

## 输出描述

输出最后剩余石子编号。

## 示例描述

### 示例一

**输入：**

```text
3
```

**输出：**

```text
58 91
```

## 解题思路

这段代码实现的是"约瑟夫环 "问题的解决方法。给定一个正整数n，假设有一个由1到100的整数组成的列表，初始时列表中所有的数字都没有被标记（标记为-1)。从列表的第一个数字开始，从1开始计数，每数到第n个数字时，将该数字标记为-1，直到列表中所有数字都被标记为止。最后输出没有被标记的数字。

## 解题代码

```python
def solve_method(n):
    nums = [i for i in range(1,101)]
    max_index = len(nums) - 1
    index = 0
    count = 0
    num_n = 0
    while count < 98:
        while True:
            if index > max_index:
                index = 0
            if nums[index] != -1:
                num_n += 1
            if num_n == n:
                num_n = 0
                break
            index += 1
        count += 1
        nums[index] = -1

    for item in nums:
        if item != -1:
            print(item, end=" ")



k = int(input())
solve_method(k)
```

