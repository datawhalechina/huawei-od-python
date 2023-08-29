# 191 计算最接近的数

## 题目描述

给定一个数组`X`和正整数`K`，请找出使表达式`X[i] - X[i+1] - ... - X[i+K-1]`结果最接近于数组中位数的下标`i`，如果有多个`i`满足条件，请返回最大的`i`。

其中，数组中位数是长度为`N`的数组按照元素的值大小升序排列后，下标为`N/2`元素的值。

**补充说明：**

1. 数组`X`的元素均为正整数。
2. `X`的长度`N`取值范围是2 <= N <= 1000。
3. `K`大于0且小于数组的大小。
4. `i`的取值范围是0 <= i < 1000。
5. 题目的排序数组`X[N]`的中位数是`X[N/2]`。

## 输入描述

输入一个数组`X`和正整数`K`。

## 输出描述

输出结果最接近数组中位数的下标`i`，如果有多个`i`满足条件，请返回最大的`i`。

## 示例描述

### 示例一

**输入：**

```text
[1,2,3,3],2
```

**输出：**

```text
2
```

### 示例二

**输入：**

```text
[50,50,2,3],2
```

**输出：**

```text
1
```

**说明：**

中位数为50，`[50,50,2,3]`升序排序后变成`[2,3,50,50]`，中位数为下标`4/2=2`的元素50；

计算结果为1，根据数组`[50,50,2,3]`，按照题目的计算公式`X[i] - X[i+1] - ... - X[i+K-1]`得出三个数：
- X[0] - X[1]= 50 - 50 = 0
- X[1] - X[2] = 50 - 2 = 48
- X[2] - X[3] = 2 - 3 = -1 

其中，48最接近50，因此返回下标1。

## 解题思路

1. 得到数组的中位数`mid`。
2. 遍历数组的索引：
    - 计算表达式`X[i] - X[i+1] - ... - X[i+K-1]`的值。
    - 计算该值与中位数的之差的绝对值。
    - 得到最小的绝对值（即最近的距离）和下标。
3. 返回下标。    

## 解题代码

```python
def find_median(nums):
    sorted_nums = sorted(nums)
    N = len(sorted_nums)
    return sorted_nums[N // 2]


def solve_method(nums, K):
    # 得到数组的中位数
    mid = find_median(nums)
    min_distance = float('inf')
    index = -1
    for i in range(len(nums) - K + 1):
        # 计算表达式
        count = nums[i]
        for j in range(i + 1, i + K):
            count -= nums[j]

        # 计算与中位数的之差的绝对值
        distance = abs(count - mid)

        # 得到最近的距离和下标
        if distance < min_distance:
            min_distance = distance
            index = i
    return index


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 3], 2) == 2
    assert solve_method([50, 50, 2, 3], 2) == 1
```

