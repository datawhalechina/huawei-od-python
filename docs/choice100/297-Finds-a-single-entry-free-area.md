# 297 查找单入口空闲区域

## 题目描述
给定一个 $m \times n$ 的矩阵，由若干字符 X 和 O 构成，
X表示该处已被占据，O表示该处空闲，请找到最大的单入口空闲区域。

空闲区域是由连通的O组成的区域，位于边界的O可以构成入口，
单入口空闲区域即有且只有一个位于边界的O作为入口的由连通的O组成的区域。
如果两个元素在水平或垂直方向相邻，则称它们是“连通”的。

## 输入描述
第一行输入为两个数字，
1. 第一个数字为行数 m，
2. 第二个数字列数 n，两个数字以空格分隔，\
$1≤m,n≤200$

剩余各行为矩阵各行元素，元素为X 或 O，各元素间以空格分隔。

## 输出描述

若有唯一符合要求的最大单入口空闲区域，输出三个数字，

1. 第一个数字为入口行坐标（范围为0~行数-1）
2. 第二个数字为入口列坐标（范围为0~列数-1），
3. 第三个数字为区域大小，三个数字以空格分隔；


若有多个符合要求的最大单入口空闲区域，输出一个数字，代表区域的大小；
若没有，输出NULL。

### 示例一
**输入：**
```shell
4 4
X X X X
X O O X
X O O X
X O X X
```

**输出：**
```shell
3 1 5
```

**说明：**  
存在最大单入口区域，入口行坐标3，列坐标1，区域大小5


### 示例二
**输入：**
```shell
4 5
X X X X X
O O O O X
X O O O X
X O X X O
```

**输出：**
```shell
3 4 1
```

**说明：**  
存在最大单入口区域，入口行坐标3，列坐标4，区域大小1


## 解题思路

## 解题代码

```python
# 输入获取
m, n = map(int, input().split())
matrix = [input().split() for i in range(m)]


# 算法入口
def getResult(matrix, m, n):
    checked = set()

    offsets = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def dfs(i, j, count, out):
        pos = f"{i}-{j}"

        if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] == "X" or pos in checked:
            return count

        checked.add(pos)

        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            out.append([i, j])

        count += 1

        for offsetX, offsetY in offsets:
            newI = i + offsetX
            newJ = j + offsetY
            count = dfs(newI, newJ, count, out)

        return count

    ans = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "O" and f"{i}-{j}" not in checked:
                out = []
                count = dfs(i, j, 0, out)
                if len(out) == 1:
                    tmp = out[0][:]
                    tmp.append(count)
                    ans.append(tmp)

    if len(ans) == 0:
        return "NULL"

    ans.sort(key=lambda x: -x[2])

    if len(ans) == 1 or ans[0][2] > ans[1][2]:
        return " ".join(map(str, ans[0]))
    else:
        return ans[0][2]


# 算法调用
print(getResult(matrix, m, n))
```