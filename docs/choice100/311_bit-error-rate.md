# 311 通信误码

## 题目描述

信号传播过程中会出现一些误码，不同的数字表示不同的误码ID，取值范围为1\~65535，用一个数组记录误码出现的情况，每个误码出现的次数代表误码频度，请找出记录中包含频度最高误码的最小子数组长度。

## 输入描述

输入的第一行是误码总数目：取值范围为0\~255，取值为0表示没有误码的情况。

输入的第二行是误码出现频率数组：误码ID范围为1\~65535，数组长度为1\~1000。

## 输出描述

输出包含频率最高的误码最小子数组长度。

## 示例描述

### 示例一

**输入：**
```text
5 
1 2 2 4 1
```

**输出：**
```text
2
```

**说明：**  

频度最高的有1和2，频度是2（2和1出现的次数都是2）。

可以包含频度最高的记录数组是`[2 2]`和`[1 2 2 4 1]`，其中最短是`[2 2]`，最小长度为2。

### 示例二

**输入：**
```text
7 
1 2 2 4 2 1 1
```

**输出：**
```text
4
```

**说明：**  

频度最高的是1和2，最短的是`[2 2 4 2]`，长度为4。

## 解题思路

1. 构建误码索引字典`num_index`，`key`为数字值，`value`为该值所在的位置。
2. 遍历误码出现频率数组，初始化误码索引字典`num_index`。
3. 遍历误码索引：如果出现次数较大，或次数相同时，距离较大，则记录最大出现次数和最小距离。
4. 返回最小距离，即包含频率最高的误码最小子数组的长度。

## 解题代码

```python
import math
from collections import defaultdict


def solve_method(arr):
    # 构建误码索引字典，key为误码值，value为该值所在的位置
    num_index = defaultdict(list)

    for i in range(len(arr)):
        num_index[arr[i]].append(i)

    max_count = 0
    min_len = math.inf

    for values in num_index.values():
        count = len(values)
        length = values[-1] - values[0] + 1

        # 如果出现次数较大，或次数相同时，距离较小，则记录最大出现次数和最小距离。
        if count > max_count or (count == max_count and length < min_len):
            max_count = max(count, max_count)
            min_len = min(length, min_len)

    return min_len


if __name__ == '__main__':
    assert solve_method([1, 2, 2, 4, 1]) == 2
    assert solve_method([1, 2, 2, 4, 2, 1, 1]) == 4
```