# 020 找数字

## 题目描述

给定一个二维数组`nums`，对于每个元素`nums[i]`，找出距离最近的且值相等的元素，输出横纵坐标值的绝对值之和，如果没有等值元素，则输出-1。

例如：输入数组`nums`为
```text
0 3 5 4 2
2 5 7 8 3
2 5 4 2 4
```

- 对于`nums[0][0] = 0`，不存在相等的值。
- 对于`nums[0][1] = 3`，存在一个相等的值，最近的坐标为`nums[1][4]`，最小距离为4。
- 对于`nums[0][2] = 5`，存在两个相等的值，最近的坐标为`nums[1][1]`，最小距离为2。
...
- 对于`nums[1][1] = 5`，存在两个相等的值，最近的坐标为`nums[2][1]`，最小距离为1。
...
  
故输出为
```text
-1 4 2 3 3
1 1 -1 -1 4
1 1 2 3 2
```

## 输入描述

输入第1行为二维数组的行`n`，第2行为二维数组的列`m`。之后为`n`行`m`列的数组。

## 输出描述

数组形式返回所有最小距离。

## 示例描述

### 示例一

**输入：**
```text
3
5
0 3 5 4 2
2 5 7 8 3
2 5 4 2 4
```

**输出：**
```text
[[-1, 4, 2, 3, 3], [1, 1, -1, -1, 4], [1, 1, 2, 3, 2]]
```

## 解题思路

1. 本题需要构建一个字典，用于存储每个数字对应的位置。
2. 遍历数组，统计每个数字的所在位置。
3. 初始化结果列表，最小位置都设置为-1。
4. 遍历数组，计算最小位置，并保存到结果列表中。
5. 返回结果列表。

## 解题代码

```python
import math
from collections import defaultdict


def solve_method(arr):
    n = len(arr)
    m = len(arr[0])
    num_pos = defaultdict(list)
    # 统计每个数字的所在位置
    for i in range(n):
        for j in range(m):
            num = arr[i][j]
            num_pos[num].append((i, j))

    # 初始化列表，最小位置都设置为-1
    result = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            num = arr[i][j]
            all_pos = num_pos[num]

            min_diff = math.inf
            if len(all_pos) != 1:
                for pos in all_pos:
                    if i == pos[0] and j == pos[1]:
                        continue
                    # 计算距离值
                    diff = abs(i - pos[0]) + abs(j - pos[1])
                    # 得到最近距离
                    min_diff = min(min_diff, diff)
                result[i][j] = min_diff

    return result


if __name__ == '__main__':
    arr = [
        [0, 3, 5, 4, 2],
        [2, 5, 7, 8, 3],
        [2, 5, 4, 2, 4]
    ]
    assert solve_method(arr) == [[-1, 4, 2, 3, 3], [1, 1, -1, -1, 4], [1, 1, 2, 3, 2]]
```