# 248 最少数量线段覆盖

## 题目描述

给定坐标轴上的一组线段，线段的起点和终点均为整数并且长度不小于1。

请你从中找到最少数量的线段，这些线段可以覆盖住所有线段。

## 输入描述

第一行输入为所有线段的数量，不超过10000。

后面每行表示一条线段，格式为`x,y`，`x`和`y`分别表示起点和终点，取值范围是[-10^5, 10^5]。

## 输出描述

最少线段数量，为正整数。

## 示例描述

### 示例一

**输入：**
```text
3
1,4
2,5
3,6
```

**输出：**
```text
2
```

**说明：**

选取2条线段`[1,4]`和`[3,6]`即可，这两条线段可以覆盖`[2,5]`。

## 解题思路

1. 遍历所有线段，初始化整数频次字典`line_dict`，`key`为整数，`value`为出现次数。
2. 遍历所有线段：
   - 如果若线段上每个点出现次数均大于1，则可以删除该线段
   - 记录删除线段的个数`del_count`。
3. 返回结果，即剩余线段的个数等于总线段个数减去已删除线段的个数。   

## 解题代码
```python
from collections import defaultdict


def solve_method(n, points):
    # line_dict存储整数点和出现的次数
    line_dict = defaultdict(int)
    for point in points:
        for i in range(point[0], point[1] + 1):
            line_dict[i] += 1
    # del_count记录可删除的线段数
    del_count = 0
    for point in points:
        # 如果若线段上每个点出现次数均大于1，则可以删除该线段
        if all([True if line_dict[i] > 1 else False for i in range(point[0], point[1] + 1)]):
            for i in range(point[0], point[1] + 1):
                line_dict[i] -= 1
            del_count += 1
    return n - del_count


if __name__ == "__main__":
    # n = int(input())
    # points = []
    # for _ in range(n):
    #     x, y = map(int, input().split(','))
    #     points.append((x, y))
    # print(solve_method(n, points))

    assert solve_method(3, [[1, 4], [2, 5], [3, 6]]) == 2
```