# 119 最大排列

## 题目描述

给定一组整数，重排序后输出一个最大的整数。

## 输入描述

输入一行数字组合，用空格分隔。

## 输出描述

输出一个数字，表示最大的整数。

## 示例描述

### 示例一

**输入：**

```text
10 9
```

**输出：**

```text
910
```

## 解题思路

1. 遍历字符串数组。 
2. 再次遍历后面的字符串数组：
    - 比较交换前组成的数字和交换后组成的数字，如果交换后的较大，则交换两个字符串的位置。
3. 将排列好的字符串拼接成结果字符串，并返回。

## 解题代码

```python
def solve_method(nums):
    length = len(nums)

    for i in range(length):
        for j in range(i + 1, length):
            if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                nums[i], nums[j] = nums[j], nums[i]

    return int("".join(nums))


if __name__ == '__main__':
    assert solve_method(["10", "9"]) == 910
```
