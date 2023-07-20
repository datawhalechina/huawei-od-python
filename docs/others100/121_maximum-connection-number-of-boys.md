# 121 最大相连男生数

## 题目描述

学校组织活动，将学生排成一个矩形方阵。请在矩形方阵中找到最大的位置相连的男生数量。这个相连位置在一个直线上，方向可以是水平的、垂直的、成对角线的或者反对角线的。

注：学生个数不会超过10000。

## 输入描述

输入的第一行表示矩阵的行数和列数，接下来的`n`行是矩阵元素，元素间用`,`分隔。

## 输出描述

输出一个整数，表示矩阵中最长的位置相连的男生个数。

## 示例描述

### 示例一

**输入：**
```text
3,4
F,M,M,F
F,M,M,F
F,F,F,M
```

**输出：**
```text
3
```

## 解题思路

**基本思路：** 本题使用深度优先搜索。
1. 用相对位置数组`positions`表示水平、垂直、对角线或者反对角线方向。
2. 遍历数组，再遍历相对位置，使用深度优先搜索，搜索最大长度。
3. 深度优先搜索：
    - 终止条件：当超出边界时，停止搜索。
    - 当数组元素为`M`时，长度加1。
    - 继续搜索下一个位置。
4. 返回最大长度。

## 解题代码

```python
def dfs(pos, arr, row, column, lenght):
    if not (0 <= row < len(arr) and 0 <= column < len(arr[0])):
        return lenght

    if arr[row][column] == "M":
        lenght += 1
    
    return dfs(pos, arr, row + pos[0], column + pos[1], lenght)


def solve_method(arr):
    # 表示水平、垂直、对角线或者反对角线方向
    positions = [[0, 1], [1, 0], [1, 1], [-1, -1]]

    max_len = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for pos in positions:
                max_len = max(max_len, dfs(pos, arr, i, j, 0))

    return max_len


if __name__ == '__main__':
    arr = [
        ["F", "M", "M", "F"],
        ["F", "M", "M", "F"],
        ["F", "F", "F", "M"]
    ]
    assert solve_method(arr) == 3
```