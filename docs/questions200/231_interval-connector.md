# 231 区间连接器

## 题目描述

有一组区间`[a0, b0], [a1, b1], ...`，其中`a`表示起点，`b`表示终点，区间有可能重叠、相邻，重叠或相邻则可以合并为更大的区间；

给定一组连接器`[x1, x2, x3, ...]`，其中`x`表示连接器的最大可连接长度，可用于将分离的区间连接起来，但两个分离区间之间只能使用1个连接器；

其中：
- 区间数量 < 10000
- a, b <= 10000
- 连接器数量 < 10000
- x <= 10000

请编程实现使用连接器后，最少的区间数结果。

## 输入描述

第一行是区间组，例如：`[1,10],[15,20],[18,30],[33,40]`

第二行是连接器组，例如：`[5,4,3,2]`

## 输出描述

使用连接器后，最少的区间数结果。

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

合并后，区间组为`[1,10], [15,30], [33,40]`，使用5和3两个连接器连接后，区间为`[1,40]`，所以区间数为1。

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

无重叠和相邻，使用1、2、5三个连接器连接后，区间组为`[1, 20], [30, 100]`，所以最少的区间数是2。

## 解题思路

1. 将区间组按照左端点从小到大排列。
2. 合并重叠和相邻的区间。
3. 计算合并后，区间之间的距离`distances`。
4. 将区间距离`distances`和连接器组的长度按照从小到大排列。
5. 遍历区间距离和连接器组，判断连接器是否足够连接距离，如果能连接，则将相应的距离置0。
6. 统计距离中不为0的个数，加上1之后，返回结果。

## 解题代码

```python
def solve_method(regions, linkers):
    # 将区间按照左端点从小到大排列
    regions.sort(key=lambda x: (x[0], x[1]))

    prev_region = None
    i = 0
    # 合并重叠和相邻的区间
    while i < len(regions):
        cur_region = regions[i]
        if prev_region is None:
            prev_region = cur_region
        elif prev_region[1] >= cur_region[0]:
            # 如果重叠
            if prev_region[1] < cur_region[1]:
                # 合并区域
                prev_region[1] = cur_region[1]
            regions.pop(i)
        else:
            prev_region = cur_region
            i += 1

    distances = [0]
    prev_region = None
    # 计算合并后，区间之间的距离
    for i in range(len(regions)):
        cur_region = regions[i]
        if prev_region is not None:
            gap = cur_region[0] - prev_region[1]
            distances.append(gap)
        prev_region = cur_region

    # 将距离和连接器长度按照从小到大排列
    distances.sort()
    linkers.sort()

    i = 0
    j = 0
    # 遍历计算连接器是否足够连接距离
    while i < len(distances) and j < len(linkers):
        if linkers[j] >= distances[i]:
            distances[i] = 0
            i += 1
            j += 1
        else:
            j += 1

    return len(list(filter(lambda x: x > 0, distances))) + 1


if __name__ == '__main__':
    regions = [[1, 10], [15, 20], [18, 30], [33, 40]]
    linkers = [5, 4, 3, 2]
    assert solve_method(regions, linkers) == 1

    regions = [[1, 2], [3, 5], [7, 10], [15, 20], [30, 100]]
    linkers = [5, 4, 3, 2, 1]
    assert solve_method(regions, linkers) == 2
```