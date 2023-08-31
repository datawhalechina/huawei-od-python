# 032 服务中心选址、服务中心的最佳位置

## 题目描述

一个快递公司希望在一条街道建立新的服务中心。公司统计了该街道中所有区域在地图上的位置，并希望能够以此为依据为新的服务中心选址：使服务中心到所有区域的距离的总和最小。

给你一个数组`positions`，其中`positions[i] = [left, right]`表示第`i`个区域在街道上的位置，其中`left`代表区域的左侧的起点，`right`代表区域的右侧终点，假设服务中心的位置为`location`。

- 如果第`i`个区域的右侧终点`right`满足`right < location`，则第`i`个区域到服务中心的距离为`location - right`。
- 如果第`i`个区域的左侧起点`left`满足`left > location`，则第`i`个区域到服务中心的距离为`left - location`。
- 如果第`i`个区域的两侧`left`、`right`满足`left <= location <= right`，则第`i`个区域到服务中心的距离为0。

选择最佳的服务中心位置为`location`，请返回最佳的服务中心位置到所有区域的距离总和的最小值。

## 输入描述

先输入区域数组`positions`的长度`n`，取值范围是1 <= n <= 10^5。

接下来`n`行每行输入成对的`left`和`right`值，以空格隔开，取值范围是-10^9 < left,right <= 10^9。

## 输出描述

输出最佳的服务中心位置到所有区域的距离总和的最小值。

**补充说明：**

不同的`positions`的区间可能存在重叠；`location` 的位置可以有多个。

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

我们选择最佳服务中心位置可以选择4，此时的最小距离为8。

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

我们选择最佳服务中心位置可以选择4，此时的最小距离为0。

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

我们选择最佳服务中心位置可以选择7，此时的最小距离为14。

## 解题思路

**基本思路：** 用二分法求解。
1. 得到整个数组的最大值`right`和最小值`left`。
2. 使用二分法遍历：
    - 计算中间值`mid`
    - 比较中间值到所有区域的距离总和，如果更小，则向左偏，如果更大，则向右偏

**代码思路：**
二分查找，右侧区间的初始最大值定为长度n的最大值10^5

## 解题代码
```python
def solve_method(n, positions):
    positions.sort(key=lambda x: (x[0], x[1]))

    left = positions[0][0]
    right = positions[-1][1]
    while left < right:
        mid = (right + left) // 2
        if get_distance(mid, positions) < get_distance(mid + 1, positions):
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
    # n = int(input())
    # positions = []
    # for _ in range(n):
    #     positions.append(list(map(int, input().split())))
    # print(solve_method(n, positions))

    assert solve_method(3, [[1, 2], [3, 4], [10, 20]]) == 8
    assert solve_method(2, [[1, 4], [4, 5]]) == 0
    assert solve_method(4, [[1, 3], [2, 6], [8, 10], [15, 18]]) == 14
```