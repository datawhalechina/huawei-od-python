# 250 服务中心选址、服务中心的最佳位置

## 题目描述

一个快递公司希望在一条街道建立新的服务中心。公司统计了该街道中所有区域在地图上的位置，并希望能够以此为依据为新的服务中心选址：使服务中心到所有区域的距离的总和最小。

给你一个数组 `positions`，其中 `positions[i] = [left, right]` 表示第 i 区域在街道上的位置，其中 left 代表区域的左侧的起点， right 代表区域的右侧终点，假设服务中心的位置为 `location`。

如果第 i 个区域的右侧终点 `right` 满足 `right < location`，则第 i 个区域到服务中心的距离为 `location - right`;

.如果第 i 个区域的左侧起点 `left` 满足 `left > location`，则第 i 个区域到服务中心的距离为 `left - location`;

如果第 i 个区域的两侧 `left`，`right` 满足 `left <= location <= right`，则第 `i` 个区域到服务中心的距离为 0;

选择最佳的服务中心位置为 `location`，请返回最佳的服务中心位置到所有区域的距离总和的最小值。

## 输入描述

先输入区域数组positions的长度n（1＜＝n＜＝10^5）

接下来 n 行每行输入成对的left和right值，以空格隔开。
```
-10^9<left<=10^9
-10^9<right<=10^9
```

## 输出描述

输出为 `location`

## 补充说明
不同的 `positions` 的区间可能存在重叠；`location` 的位置可以有多个。

## 示例描述

### 示例一

**输入：**
```text
3
1 2
3 4
10 20
```

**输出：**
```text
8
```

**说明：**
我们选择最佳服务中心位置可以选择*****，此时的最小距离为8

### 示例二

**输入：**
```text
2
1 4
4 5
```

**输出：**
```text
0
```

**说明：**
我们选择最佳服务中心位置可以选择4，此时的最小距离为0

### 示例三

**输入：**
```text
4
1 3
2 6
8 10
15 18
```

**输出：**
```text
14
```

**说明：**
我们选择最佳服务中心位置可以选择7，此时的最小距离为14

## 解题思路

**基本思路：**

从数据层面来看：输入数据量级为10^9 -> 考虑不超时O(n)的n量级为10^8，O(nlogn)的n量级为10^7 -> 排序后二分？

从理解层面来看：如果我们将服务中心定在某个点，求解距离总和可以等价为求解：该点左侧的特定点数之和 + 该点右侧的特定点数之和。随着服务中心的右移，左侧点数之和减少，右侧点数之和增加。

**代码思路：**
二分查找，右侧区间的初始最大值定为长度n的最大值10^5

## 解题代码
```python
def solve_method(n, positions):
    # 区域数组positions的长度n范围为：1＜＝n＜＝10^5
    left, right = 0, 100000
    while left < right:
        mid = (left + right) >> 1
        if get_distance(mid, positions) < get_distance(mid+1, positions):
            right = mid
        else:
            left = mid + 1
    return get_distance(left, positions)

def get_distance(location, positions):
    distance = 0
    for position in positions:
        if position[0] > location:
            distance += position[0] - location
        elif position[1] < location:
            distance += location - position[1]
    return distance

if __name__ == "__main__":
    # 3
    # 1 2
    # 3 4
    # 10 20
    n = int(input())
    positions = []
    for _ in range(n):
        positions.append(list(map(int, input().split())))
    print(solve_method(n, positions))

    assert solve_method(3, [[1,2], [3,4], [10,20]]) == 8
    assert solve_method(2, [[1,4], [4,5]]) == 0
    assert solve_method(4, [[1,3], [2,6], [8,10], [15,18]]) == 14
```