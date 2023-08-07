# 022 众数和中位数

## 题目描述

1. 众数是指一组数据中出现次数多的数，众数可以有多个。
2. 中位数是指把一组数据从小到大排列，最中间的那个数
    - 如果这组数据的个数是奇数，那最中间那个就是中位数。
    - 如果这组数据的个数为偶数，那就把中间的两个数之和除以2，结果就是中位数。
3. 查找整型数组中元素的众数并组成一个新的数组，求新数组的中位数。

## 输入描述

输入一个一维整型数组，数组大小取值范围是0 < n < 1000，数组中每个元素取值范围是0 < e < 1000。

## 输出描述

输出众数组成的新数组的中位数。

## 示例描述

### 示例一

**输入：**

```text
10 11 21 19 21 17 21 16 21 18 16
```

**输出：**

```text
21
```

### 示例二

**输入：**

```text
2 1 5 4 3 3 9 2 7 4 6 2 15 4 2 4
```

**输出：**

```text
3
```

### 示例三

**输入：**

```text
5 1 5 3 5 2 5 5 7 6 7 3 7 11 7 55 7 9 98 9 17 9 15 9 9 1 39
```

**输出：**

```text
7
```

## 解题思路

**基本思路：** 

1. 用`Counter()`计数，并获取最大的频数即众数。
2. 取出所有频数为众数的数字，组成新的数组`modes`。
3. 对数组进行排序。
4. 计算中位数：
   - 如果为奇数，则取中间的数为中位数。
   - 如果为偶数，取中间两个数的平均值为中位数。
5. 返回结果。

## 解题代码

```Python
from collections import Counter


def solve_method(nums):
    # 使用Counter计数
    count = Counter(nums)

    # 获取最大的频次
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]

    # 将数组按照从小到大排序
    sorted_nums = sorted(modes)
    length = len(sorted_nums)

    mid = length // 2
    if length % 2 == 1:
        # 如果数组长度为奇数，中位数为中间的那个元素
        median = sorted_nums[mid]
    else:
        # 如果数组长度为偶数，中位数为中间两个元素的平均值
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) // 2

    return median


if __name__ == '__main__':
    nums = [10, 11, 21, 19, 21, 17, 21, 16, 21, 18, 16]
    assert solve_method(nums) == 21

    nums = [2, 1, 5, 4, 3, 3, 9, 2, 7, 4, 6, 2, 15, 4, 2, 4]
    assert solve_method(nums) == 3

    nums = [5, 1, 5, 3, 5, 2, 5, 5, 7, 6, 7, 3, 7, 11, 7, 55, 7, 9, 98, 9, 17, 9, 15, 9, 9, 1, 39]
    assert solve_method(nums) == 7
```
