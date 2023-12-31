# 017 天然蓄水池

## 题目描述

公元2919年，人类终于发现了一颗宜居星球——X星。现想在X星一片连绵起伏的山脉间建一个天然蓄水库，如何选取水库边界，使蓄水量最大？

要求：
- 山脉用正整数数组`s`表示，每个元素代表山脉的高度。
- 选取山脉上两个点作为蓄水库的边界，则边界内的区域可以蓄水，蓄水量需排除山脉占用的空间。
- 蓄水量的高度为两边界的最小值。
- 如果出现多个满足条件的边界，应选取距离最近的一组边界。

输出边界下标（从0开始）和最大蓄水量；如果无法蓄水，则返回0，此时不返回边界。

例如，当山脉为`s=[3,1,2]`时，则选取`s[0]`和`s[2]`作为水库边界，则蓄水量为1，此时输出：`0 2:1`

当山脉`s=[3,2,1]`时，不存在合理的边界，此时输出：`0`。

## 输入描述

一行正整数，用空格隔开，例如输入

```text
1 2 3
```

表示`s=[1,2,3]`。

## 输出描述

当存在合理的水库边界时，输出左边界、空格、右边界、英文冒号、蓄水量，例如：

```text
0 2:1
```

当不存在合理的水库边界时，输出0，例如：

```text
0
```

## 备注

- 1 <= length(s) <= 10000
- 0 <= s[i] <= 10000

## 示例描述

### 示例一

**输入：**
```text
1 9 6 2 5 4 9 3 7
```

**输出：**
```text
1 6:19
```

**说明：**  

经过分析，选取`s[1]`和`s[6]`，水库蓄水量为19（3+7+4+5）。

### 示例二

**输入：**
```text
1 8 6 2 5 4 8 3 7
```

**输出：**
```text
1 6:15
```

**说明：**  

经过分析，选取`s[1]`和`s[8]`时，水库蓄水量为15；同样选取`s[1]`和`s[6]`时，水库蓄水量也为15。由于后者下标距离小（为5），故应选取后者。

### 示例三

**输入：**
```text
1 2 3
```

**输出：**
```text
0
```

**说明：**

不存在合理的水库边界

## 解题思路

**基本思路：** 使用双指针法求解。

1. 初始化左右指针，分别设置为山脉的两端。
2. 遍历所有山脉：
    - 计算从左指针到右指针的山脉中间的蓄水量`area`。
    - 通过比较，获取最大的蓄水量。
    - 如果左端较低，则左指针向右移动，如果右端较低，则右指针向左移动。
3. 返回左右坐标和最大蓄水量。    

## 解题代码
```python
def solve_method(s):
    # 分别从左右两端向中间遍历，如果左端较低，则移动左端，如果右端较低，则移动右端
    left, right = 0, len(s) - 1
    max_area = 0
    max_i, max_j = 0, len(s) - 1

    while left < right - 1:
        area = 0
        for i in range(left + 1, right):
            area += min(s[left], s[right]) - s[i]
        if area >= max_area:
            max_area = area
            max_i, max_j = left, right

        if s[left] < s[right]:
            left += 1
        else:
            right -= 1

    if max_area == 0:
        return 0
    else:
        return max_i, max_j, max_area


if __name__ == '__main__':
    s = [3, 1, 2]
    assert solve_method(s) == (0, 2, 1)

    s = [3, 2, 1]
    assert solve_method(s) == 0

    s = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solve_method(s) == (1, 6, 15)

    s = [1, 9, 6, 2, 5, 4, 9, 3, 7]
    assert solve_method(s) == (1, 6, 19)
```