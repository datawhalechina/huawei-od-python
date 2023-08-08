# 036 删除重复数字后的最大数字

## 题目描述

一个长整型数字，消除重复的数字后，得到最大的一个数字。

如12341，消除重复的1，可得到1234或2341，取最大值2341。

如42234，消除4后，得到4223或者2234，再消除2，得到423或234，取最大值423。

## 输入描述

输入一个数字，范围是[1,100000]。

## 输出描述

输出经过删除操作后的最大值。

## 示例描述

### 示例一

**输入：**

```text
12341
```

**输出：**

```text
2341
```

### 示例二

**输入：**

```text
42234
```

**输出：**

```text
423
```

## 解题思路

**基本思路：** 使用回溯算法求解。

1. 将数字转成列表形式，用于计算每个十足出现的次数。
2. 使用回溯算法：
   - 确定参数：数字列表`nums`、存储无重复数字的列表`paths`。
   - 终止条件：当所有频数都为1时，将消除重复的数字存入到`paths`列表中。
   - 回溯处理：遍历每个数字：
      - 删除该位置的数字。
      - 调用回溯方法。
      - 在该位置插入数字。
3. 返回`paths`中的最大值。   
         

1. 创建一个字典`number_count`，遍历`number`统计每个数字出现的频率，同时将数字压入栈res[]中

2. 遍历`number_count`,当键值count≥2时：

    3. 如果后一个位置res[i+1]大于当前位置res[i]，则删除当前位置

    4. 如果是最后一个数字且还有剩余，那么删除最后一个数字

5. 最后返回结果

## 解题代码

```Python
from collections import Counter


def backstracking(nums: list, paths: list):
    num_count = Counter(nums)
    # 当所有频数都为1时，可得到消除重复的数字
    if all([True if x[1] == 1 else False for x in num_count.items()]):
        paths.append(int("".join(nums)))
        return

    for i, num in enumerate(nums):
        if num_count[num] > 1:
            nums.pop(i)
            backstracking(nums, paths)
            nums.insert(i, num)


def solve_method(num):
    nums = list(str(num))
    paths = []
    backstracking(nums, paths)

    return max(paths)


if __name__ == '__main__':
    assert solve_method(12341) == 2341
    assert solve_method(42234) == 423
```

