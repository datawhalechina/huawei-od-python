# 056 子序列长度

## 题目描述

有`N`个正整数组成的一个序列，给定一个整数`sum`，求长度最长的的连续子序列使他们的和等于`sum`，返回子序列的长度，如果没有满足要求的序列，返回-1。

## 输入描述

第一行是`,`拼接的正整数序列。

第二行是一个整数`sum`。

## 输出描述

满足条件的子序列的长度，如果没有满足要求的序列，则返回-1。

## 示例描述

### 示例一

**输入：**

```text
1,2,3,4,2
6
```

**输出：**

```text
3
```

**说明：**

`1,2,3`和`4,2`两个序列均能满足要求，所以最长的连续序列为`1,2,3`，因此结果为3。

### 示例二

**输入：**

```text
1,2,3,4,2
20
```

**输出：**

```text
-1
```

**说明：**

没有满足要求的子序列，返回-1。

## 解题思路

**基本思路：** 使用双指针法求解。

1. 如果数组之和小于目标值，则返回-1。
2. 使用双指针遍历（滑动窗口）：
   - 如果右指针抵达了数组最后一个位置，则判断当前子序列之后，如果小于目标值，则跳出遍历。
   - 如果子序列之和等于目标值，记录此时的长度与最大长度进行比较并更新，左指针向右移。
   - 如果子序列之和大于目标值，左指针向右移。
   - 如果子序列之和小于目标值，右指针向左移。
3. 返回最大长度。

## 解题代码

```python
def solve_method(nums, target_sum):
    max_len = -1

    if sum(nums) < target_sum:
        return -1

    left, right = 0, 1
    while left < len(nums):
        sub_sum = sum(nums[left:right])
        if right == len(nums) - 1 and sub_sum < target_sum:
            break

        if sub_sum == target_sum:
            length = right - left
            if max_len < length:
                max_len = length
            left += 1
        elif sub_sum > target_sum:
            left += 1
        else:
            right += 1

    return max_len


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 2]
    assert solve_method(nums, 6) == 3

    nums = [1, 2, 3, 4, 2]
    assert solve_method(nums, 20) == -1
```



