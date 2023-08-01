# 251 机器人活动区域

## 题目描述

现有一个机器人，可放置于MxN的网格中任意位置，每个网格包含一个非负整数编号。当相邻网格的数字编号差值的绝对值小于等于1时，机器人可以在网格间移动。

问题：求机器人可活动的最大范围对应的网格点数目。

说明：

1．网格左上角坐标为（0.0），右下角坐标为（m-1，n-1）

2．机器人只能在相邻网格间上下左右移动

## 输入描述

第1行输入为M和N，M表示网格的行数 N表示网格的列数

之后M行表示网格数值，每行N个数值（数值大小用k表示），数值间用单个空格分隔，行首行尾无多余空格

M、N、k均为整数，且1≤M，N≤150，0≤k≤50

## 输出描述

输出1行，包含1个数字，表示最大活动区域的网格点数目

行首行尾无多余空格

## 示例描述

### 示例一

**输入：**
```text
4 4
1 2 5 2
2 4 4 5
3 5 7 1
4 6 2 4
```

**输出：**
```text
6
```

**说明：**
![251-001-sample1-analysis](./images/251-001-sample2-analysis.png)

图中绿色区域，相邻网格差值绝对值都小于等于1， 且为最大区域，对应网格点数目为6

### 示例二

**输入：**
```text
2 3
1 3 5
4 1 3
```

**输出：**
```text
1
```

**说明：**

任意两个相邻网格的差值绝对值都大于1，机器人不能在网格间移动，只能在单个网格内活动 对应网格点数目为1

## 解题思路

**代码思路：**
1. 外层循环：遍历机器人所有可能的起始位置
2. 内层循环dfs计算从当前位置，可活动的最大网格数
- visited数组标记已访问过的位置
- 遍历可能访问的上下左右4个方位，并进行数值判断
3. 计算最大网格数

## 解题代码
```python
def solve_method(M, N, matrix):
    maxCount = 0
    # 遍历所有可能的起始位置
    for i in range(M):
        for j in range(N):
            maxCount = max(maxCount, dfs(M, N, matrix, i, j, [[0] * N for _ in range(M)]))
    return maxCount

def dfs(M, N, matrix, i, j, visited):
    count = 1
    visited[i][j] = 1
    for x, y in [[1,0], [-1,0], [0,1], [0,-1]]:
        if i+x >= 0 and i+x < M and j+y >= 0 and j+y < N:
            if not visited[i+x][j+y] and abs(matrix[i+x][j+y] - matrix[i][j]) <= 1:
                count += dfs(M, N, matrix, i+x, j+y, visited)
    return count

if __name__ == "__main__":
    # 4 4
    # 1 2 5 2
    # 2 4 4 5
    # 3 5 7 1
    # 4 6 2 4
    # M网格行数，N网格列数
    M, N = map(int, input().split())
    matrix = []
    for _ in range(M):
        matrix.append(list(map(int, input().split())))
    print(solve_method(M, N, matrix))

    assert solve_method(4, 4, [[1,2,5,2], [2,4,4,5], [3,5,7,1], [4,6,2,4]]) == 6
    assert solve_method(2, 3, [[1,3,5], [4,1,3]]) == 1
```