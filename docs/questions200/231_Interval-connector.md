# 231 区间连接器

## 题目描述
有一组区间 `[a0, b0], [a1, b1], ...` (`a`, `b` 表示起点, 终点)，区间有可能重叠、相邻，重叠或相邻则可以合并为更大的区间；

给定一组连接器`[x1, x2, x3, ...]`（`x` 表示连接器的最大可连接长度，即 `x >= gap`），可用于将分离的区间连接起来，但两个分离区间之间只能使用1个连接器；

请编程实现使用连接器后，最少的区间数结果。

`区间数量 < 10000；a, b <= 10000`

`连接器梳理 <10000; x <= 10000`

## 输入描述
区间组：`[1,10],[15,20],[18,30],[33,40]`

连接器组：`[5,4,3,2]`

## 输出描述
`1`

说明：区间合并后为：`[1,10], [15,30], [33,40]`，使用 `5, 3` 两个连接器连接后只剩下 `[1,40]`

## 示例描述

### 示例一

**输入：**
```
[1,10],[15,20],[18,30],[33,40]
[5,4,3,2]
```

**输出：**
```
1
```

**说明：** 
合并后：`[1,10], [15,30], [33,40]`，使用 `5, 3` 两个连接器连接后只剩下 `[1,40]`

### 示例二

**输入：**
```
[1,2],[3,5],[7,10],[15,20],[30,100]
[5,4,3,2,1]
```

**输出：**
```
2
```

**说明：** 
无重叠和相邻，使用 `1，2，5` 三个连接器连接后只剩下 `[1, 20], [30, 100]`

## 解题代码
``` python
import re

def solve_method(regions, linkers):
    # 将区间按照左端点升序排列
    regions.sort(key = lambda x: (x[0], x[1]))

    region = None
    i = 0
    # 合并重叠和相邻的区间
    while i < len(regions):
        next = regions[i]
        if region is None:
            region = next
        elif region[1] >= next[0]:
            if region[1] < next[1]:
                region[1] = next[1]
            regions.pop(i)
        else:
            region = next 
            i += 1

    gaps = [0]
    region = None
    # 计算合并后，区间之间的距离
    for i in range(len(regions)):
        next = regions[i]
        if region is not None:
            gap = next[0] - region[1]
            gaps.append(gap)
        region = next

    # 将距离和连接器长度 按照升序排列
    gaps.sort()
    linkers.sort()
    
    i = 0
    j = 0
    # 遍历计算连接器是否足够连接距离
    while i < len(gaps) and j < len(linkers):
        if linkers[j] >= gaps[i]:
            gaps[i] = 0
            i += 1
            j += 1
        else:
            j += 1

    return sum(1 for g in gaps if g > 0) + 1

if __name__ == '__main__':
    regions = [[1,10], [15, 20], [18, 30], [33, 40]]
    linkers = [5, 4, 3, 2]
    assert solve_method(regions, linkers) == 1

    regions = [[1,2], [3, 5], [7, 10], [15, 20], [30, 100]]
    linkers = [5, 4, 3, 2, 1]
    assert solve_method(regions, linkers) == 2
```