# 117 最佳植树距离、种树问题

## 题目描述

小明在直线的公路上种树，现在给定可以种树的坑位的数量和位置，以及需要种多少棵树苗，问树苗之间的最小间距是多少时，可以保证种的最均匀（两棵树苗之间的最小间距最大）。

## 输入描述

输入三行：

- 第1行是一个整数，表示坑位的数量。
- 第2行以空格分隔的数组，表示坑位的位置。
- 第3行是一个整数，表示需要种植树苗的数量。

## 输出描述

树苗之间的最小间距。

## 示例描述

### 示例一

**输入：**

```text
7
1 3 6 7 8 11 13
3
```

**输出：**

```text
6
```

**说明：**  

三颗树苗分别种在 1、7、13 的位置，可以保证种的最均匀，树苗之间的最小间距为6。

## 解题思路

**基本思路：** 使用二分查找最佳的树苗间距。

1. 初始化最小间距的可能范围（上限`max_dist`， 下限`min_dist`）。
2. 从可能范围中间`mid`开始检查，当最小间距为`mid`时可以种树的数量。检查方式如下：
   - 初始化`previous`为第一个坑的位置，种树数目`count`为1。
   - 以`previous`为基准，找下一个大于等于`mid`距离的坑的位置，`count`累加，`previous`记录为现在坑的位置。
   - 继续遍历，直到最后一个坑。
3. 如果当最小间距为`mid`时可以种树的数量大于等于需要种植树苗的数量`target`，把搜索范围缩小，下限值为`mid+1`，以找到更大的`mid`。
4. 如果当最小间距为`mid`时可以种树的数量小于需要种植树苗的数量`target`，把搜索范围缩小，上限值为`mid-1`，以找到更小的`mid`。
5. 重复2到4步，直到下限值大于上限值（`min_dist>max_dist`），返回结果。

## 解题代码

```python
def solve_method(holes, target):
    holes.sort()
    min_dist = 0
    max_dist = holes[-1] - holes[0]
    answer = -1

    while min_dist <= max_dist:
        mid = min_dist + (max_dist - min_dist) // 2
        # 第一个树种植的位置为第一个坑位
        count = 1
        previous = holes[0]
        for i in range(1, len(holes)):
            if holes[i] - previous >= mid:
                count += 1
                previous = holes[i]

                if count >= target:
                    answer = mid
                    min_dist = mid + 1
                    break

        if count < target:
            max_dist = mid - 1

    return answer


if __name__ == '__main__':
    assert solve_method([1, 3, 6, 7, 8, 11, 13], 3) == 6
    assert solve_method([1, 2, 6, 8, 14], 3) == 6
    assert solve_method([1, 7, 14], 2) == 13
```



