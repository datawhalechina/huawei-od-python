# 246 最多几个直角三角形

## 题目描述

有`N`条线段，长度分别为`a[1]-a[N]`。

现要求你计算这`N`条线段最多可以组合成几个直角三角形，每条线段只能使用一次，每个三角形包含三条线段。

## 输入描述

第一行输入一个正整数`T`，表示有`T`组测试数据，取值范围是1 <= T <= 100。

对于每组测试数据，接下来有`T`行，每行第一个正整数`N`，表示线段个数，取值范围是3 <= N < 20，接着是`N`个正整数，表示每条线段长度，其中 0 < a[i] < 100。

## 输出描述

对于每组测试数据输出一行，每行包括一个整数，表示最多能组合的直角三角形个数。

## 示例描述

### 示例一

**输入：**
```text
1
7 3 4 5 6 5 12 13
```

**输出：**
```text
2
```

**说明：**

可以组成2个直角三角形(3,4,5)、(5,12,13)。

### 示例二

**输入：**
```text
1
7 3 4 5 6 6 12 13
```

**输出：**
```text
1
```

**说明：**

可以组成1个直角三角形(3,4,5)或(5,12,13)，5只能使用一次，所以只有1个。

## 解题思路

1. 遍历每一个测试用例：
  - 将数组转成`Counter`的元素频次字典。
  - 遍历所有数组元素：
      - 如果满足`a**2 + b**2 == c**2`，则计数器累加1。
  - 将计数器的值放入结果列表中。
2. 返回结果列表

## 解题代码

```python
import math
from collections import Counter


def solve_method(arr):
    result = []
    for nums in arr:
        nums = nums[1:]

        count = 0
        counter = Counter(nums)
        num_keys = list(counter.keys())
        for i in range(len(num_keys)):
            for j in range(i + 1, len(num_keys)):
                a = num_keys[i]
                b = num_keys[j]
                if counter[a] > 0 and counter[b] > 0:
                    c = math.sqrt(a ** 2 + b ** 2)
                    if c in num_keys and counter[c] > 0:
                        counter[a] -= 1
                        counter[b] -= 1
                        counter[c] -= 1
                        count += 1
        result.append(count)
    return result


if __name__ == "__main__":
    arr = [[7, 3, 4, 5, 6, 5, 12, 13]]
    assert solve_method(arr) == [2]

    arr = [[7, 3, 4, 5, 6, 6, 12, 13]]
    assert solve_method(arr) == [1]
```