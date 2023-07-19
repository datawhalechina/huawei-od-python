# 140 正方形数量、构成正方形的数量

## 题目描述

输入`N`个互不相同的二维整数坐标，求这`N`个坐标可以构成的正方形数量。

注：内积为0的两个向量垂直。

## 输入描述

第1行是一个正整数`N`，表示坐标的数量，N <= 100。

之后的`K`行分别为多个坐标`(x,y)`，`x`,`y`为整数，其中，-10 <= x, y < 10。

## 输出描述

输出可以构成的正方形数量。

## 示例描述

### 示例一

**输入：**
```text
3
1 3
2 4
3 1
```

**输出：**
```text
0
```

**说明：**  
3个点不足以构成正方形。

### 示例二

**输入：**
```text
4
0 0
1 2
3 1
2 -1
```

**输出：**
```text
1
```

## 解题思路

**基本思路：** xxxxx（注：如果存在基本思路，可编写）
1. 使用`itertools.combinations`随机选取4个点，组成一个点阵。
2. 判断这4个点是否能组成一个正方形，编写`check_square`方法。
3. `check_square`方法：
   - 从4个点中随机选取2个点，计算两点之间的距离，存入到`distances`字典中。
   - 判断4个点组成的距离中，是否存在2个距离相等（对角线相等），并且存在4个距离相等（4条边相等），可判断是否为一个正方形。
4. 统计正方形的数量。

## 解题代码

```python
import itertools
from collections import defaultdict


def check_square(square_points):
    distances = defaultdict(int)
    two_points = itertools.combinations(range(4), 2)
    for two_point in two_points:
        i = two_point[0]
        j = two_point[1]
        x = square_points[i][0] - square_points[j][0]
        y = square_points[i][1] - square_points[j][1]

        distance = x * x + y * y
        distances[distance] += 1

    # 判断4个点组成的距离中，是否存在对角线相等，并且4条边也相等
    return len(distances) == 2 and {2, 4}.issubset(distances.values())


def solve_method(points):
    if len(points) < 4:
        return 0

    count = 0
    # 随机选取4个点，组成一个点阵
    squares = itertools.combinations(range(len(points)), 4)
    for square in squares:
        square_points = [points[square[0]], points[square[1]], points[square[2]], points[square[3]]]
        # 判断这4个点是否能组成一个正方形
        if check_square(square_points):
            count += 1

    return count
```