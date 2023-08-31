# 034 查找单入口空闲区域

## 题目描述
给定一个`m*n`的矩阵，由若干字符`X`和`O`构成，`X`表示该处已被占据，`O`表示该处空闲，请找到最大的单入口空闲区域。

空闲区域是由连通的`O`组成的区域，位于边界的`O`可以构成入口，单入口空闲区域即有且只有一个位于边界的`O`作为入口的由连通的`O`组成的区域。如果两个元素在水平或垂直方向相邻，则称它们是`连通`的。

## 输入描述

第一行输入为两个数字，第一个数字为行数`m`，第二个数字列数`n`，两个数字以空格分隔，取值范围是1 <= m,n <= 200。

剩余各行为矩阵各行元素，元素为`X`或`O`，各元素间以空格分隔。

## 输出描述

若有唯一符合要求的最大单入口空闲区域，输出三个数字：

- 第一个数字为入口行坐标（范围为[0,行数-1]）。
- 第二个数字为入口列坐标（范围为[0,列数-1]）。
- 第三个数字为区域大小，三个数字以空格分隔。

若有多个符合要求的最大单入口空闲区域，输出一个数字，代表区域的大小；若没有，输出NULL。

## 示例描述

### 示例一

**输入：**
```text
4 4
X X X X
X O O X
X O O X
X O X X
```

**输出：**
```text
3 1 5
```

**说明：**  

存在最大单入口区域，入口行坐标3，列坐标1，区域大小5。

### 示例二

**输入：**
```text
4 5
X X X X X
O O O O X
X O O O X
X O X X O
```

**输出：**
```text
3 4 1
```

**说明：**  
存在最大单入口区域，入口行坐标3，列坐标4，区域大小1。

### 示例三

**输入：**
```text
5 4
X X X X
X O O O
X O O O
X O O X
X X X X
```

**输出：**
```text
NULL
```

### 示例四

**输入：**
```text
5 4
X X X X
X O O O
X X X X
X O O O
X X X X
```

**输出：**
```text
3
```

**说明：**  
存在两个大小为3的最大单入口区域，两个入口的横纵坐标分别为1,3和3,3。

## 解题思路

**基本思路：** 使用深度优先搜索DFS解题。
1. 遍历所有区域，先行后列。
2. 使用深度优先搜索DFS：
   - 确定参数：坐标`i`和`j`、区域大小`count`、入口坐标列表`out`。
   - 终止条件：如果到了边界、遇到了X或已经在连通域中，则直接返回区域大小。
   - 递归处理：
      - 当遇到入口时，则加入到坐标列表`out`中。
      - 继续对各个方向进行深度优先搜索
3. 判断入口坐标列表：
   - 当列表长度为0时，没有找到单入口空闲区域，返回`NULL`。
   - 当列表长度为1时，只有一个单入口空闲区域，返回结果。
   - 如果长度大于1，按照区域大小排序，返回最大单入口空闲区域。 

## 解题代码

```python
def dfs(i, j, count, out):
    # 如果到了边界、遇到了X或已经在连通域中，则直接返回结果。
    if i < 0 or i >= m or j < 0 or j >= n \
            or areas[i][j] == "X" or (i, j) in checked:
        return count

    checked.add((i, j))
    # 当遇到入口时，则加入到结果列表中
    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
        out.append([i, j])

    count += 1
    # 继续对各个方向进行深度优先搜索
    for offsetX, offsetY in directions:
        newI = i + offsetX
        newJ = j + offsetY
        count = dfs(newI, newJ, count, out)

    return count


def solve_method(areas):
    global checked, m, n, directions
    m = len(areas)
    n = len(areas[0])
    checked = set()
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    ans = []

    for i in range(m):
        for j in range(n):
            if areas[i][j] == "O" and (i, j) not in checked:
                out = []
                count = dfs(i, j, 0, out)
                if len(out) == 1:
                    # 只能有一个入口
                    tmp = out[0][:]
                    ans.append((tmp[0], tmp[1], count))

    if len(ans) == 0:
        return "NULL"
    elif len(ans) == 1 or ans[0][2] > ans[1][2]:
        return ans[0]
    elif len(ans) > 1:
        # 如果有多个，取出最大单入口空闲区域
        ans.sort(key=lambda x: -x[2])
        return ans[0][2]


if __name__ == '__main__':
    areas = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "O", "O", "X"],
             ["X", "O", "X", "X"]]
    assert solve_method(areas) == (3, 1, 5)

    areas = [["X", "X", "X", "X", "X"],
             ["O", "O", "O", "O", "X"],
             ["X", "O", "O", "O", "X"],
             ["X", "O", "X", "X", "O"]]
    assert solve_method(areas) == (3, 4, 1)

    areas = [["X", "X", "X", "X"],
             ["X", "O", "O", "O"],
             ["X", "O", "O", "O"],
             ["X", "O", "O", "X"],
             ["X", "X", "X", "X"]]
    assert solve_method(areas) == "NULL"

    areas = [["X", "X", "X", "X"],
             ["X", "O", "O", "O"],
             ["X", "X", "X", "X"],
             ["X", "O", "O", "O"],
             ["X", "X", "X", "X"]]
    assert solve_method(areas) == 3
```