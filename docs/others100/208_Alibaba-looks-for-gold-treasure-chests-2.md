# 208 阿里巴巴找黄金宝箱（2）

## 题目描述

一贫如洗的樵夫阿里巴巴在去砍柴的路上，无意中发现了强盗集团的藏宝地，藏宝地有编号从0\~N的箱子，每个箱子上面贴有箱子中藏有的金币的数量。

从金币数量中选出一个数字集合，并销毁贴有这些数字的每个箱子，如果能销毁一半及以上的箱子，则返回这个数字集合的最小大小。

## 输入描述

输入一个数字串，数字之间使用`,`分隔，例如
```text
6,6,6,6,3,3,3,1,1,5
```

字串中的数字的个数为偶数，并且1 <= 个数 <= 100000，1 <= 每个数字 <= 10000。

## 输出描述

输出这个数字集合的最小大小，例如：2。

## 示例描述

### 示例一

**输入：**
```text
1,1,1,1,3,3,3,6,6,8
```

**输出：**
```text
2
```

**说明：**  
选择集合{1,8}，销毁后的结果数组为[3，3，3，6，6]，长度为5，长度为原数组的一半。大小为2的可行集合还有{1,3}、{1,6}、{3,6}。

选择集合{6,8}是不可信的，它销毁后的结果数组为[1,1,1,1,3,3,3]，新数组长度大于原数组的二分之一。

### 示例一

**输入：**
```text
2,2,2,2
```

**输出：**
```text
1
```

**说明：**  
只能选择集合{2}，销毁后的结果数组为空。

## 解题思路

1. 计算每个数字的频度，用`num_freq`表示。
2. 按照频度降序排序。
3. 使用`while`循环，统计频度的值：
   - 当累计的频度值大于数组长度的一半，则返回结果。
   - 如果没有达到，则继续累加频度值。

## 解题代码

```python
from collections import defaultdict


def solve_method(nums):
    half = len(nums) // 2
    num_freq = defaultdict(int)

    for num in nums:
        num_freq[num] += 1

    num_freq = sorted(num_freq.items(), key=lambda x: -x[1])
    count = 0
    result = 0
    while count < half:
        count += num_freq[result][1]
        result += 1

    return result


if __name__ == '__main__':
    assert solve_method([6, 6, 6, 6, 3, 3, 3, 1, 1, 5]) == 2
    assert solve_method([1, 1, 1, 1, 3, 3, 3, 6, 6, 8]) == 2
    assert solve_method([2, 2, 2, 2]) == 1
```