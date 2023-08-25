# 079 找到它

## 题目描述

“找到它”是一个小游戏，你需要在一个矩阵中找到给定的单词。

假设给定单词`HELLOWORLD`，在矩阵中只要能找`HELLOWORLD`就算通过，注意区分英文字母大小写，并且你只能上下左右行走不能走回头路。

## 输入描述

输入第一行包含两个整数`M`与`N`（0 < N,M < 21）分别表示`N`行`M`列的矩阵。

第二行是长度不超过100的单词`W`，在整个矩阵中给定单词`W`只会出现一次。

从第3行到第N+2是只包含大小写英文字母的长度为`M`的字符串矩阵。

## 输出描述

如果能在矩阵中连成给定的单词，则输出给定单词首字母在矩阵中的位第几行第几列，否则输出`NO`。

## 示例描述

### 示例一

**输入：**
```text
5 5
HELLOWORLD
CPUCY
EKLQH
CHELL
LROWO
DGRBC
```

**输出：**
```text
3 2
```

### 示例二

**输入：**
```text
5 5
Helloworld
CPUCh
wolle
orldo
EKLQo
PGRBC
```

**输出：**
```text
NO
```

**说明**

区分大小写。

## 解题思路

**基本思路：** 使用深度优先搜索DFS求解。

1. 遍历矩阵中每一个字母，使用深度优先搜索：
    - 确定参数：当前字母的坐标`row`和`col`、目标字母的位置`k`、已访问字母的坐标列表`visited`。
    - 终止条件：如果遍历到最后一个单词，则表示找到了单词，返回单词首字母的坐标。
    - 递归处理：
        - 如果出界、字母已访问过、该位置的字母不是目标字母，则没有找到，继续遍历。
        - 添加该字母的坐标存入已访问列表中。
        - 如果遍历到最后一个单词，则表示找到了单词。
        - 上下左右进行寻找目标单词的下一个字母。
2. 如果没有找到，则返回`NO`。    

## 解题代码

```python
def solve_method(matrix, word):
    def dfs(row, col, k, visited):
        # 如果出界、字母已访问过、该位置的字母不是目标字母，则没有找到，继续遍历
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k] or [row, col] in visited:
            return False
        # 添加该字母的坐标存入已访问列表中
        visited.append([row, col])
        # 如果遍历到最后一个单词，则表示找到了单词
        if k == len(word) - 1:
            return True
        # 上下左右进行寻找目标单词的下一个字母
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = dfs(row + d1, col + d2, k + 1, visited)
            if res:
                return res

        return False

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                visited = []
                res = dfs(i, j, 0, visited)
                if res:
                    # 如果找到了，则返回单词首字母的坐标
                    return i + 1, j + 1
    return "NO"


if __name__ == '__main__':
    matrix = ["CPUCY",
              "EKLQH",
              "CHELL",
              "LROWO",
              "DGRBC"]
    assert solve_method(matrix, "HELLOWORLD") == (3, 2)

    matrix = ["CPUCh",
              "wolle",
              "orldo",
              "EKLQo",
              "PGRBC"]
    assert solve_method(matrix, "Helloworld") == "NO"
```

