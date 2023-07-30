# 079 找到它

## 题目描述

找到它是个小游戏，你需要在一个矩阵中找到给定的单词
假设给定单词HELLOWORLD，
在矩阵中只要能找HELLOWORLD就算通过，注意区分英文字母大小写，并且你只能上下左右行走不能走回头路。

## 输入描述
输入第一行包含两个整数M与N(0<N，M<21)分别表示N行M列的矩阵，
第二行是长度不超过100的单词W，
在整个矩阵中给定单词W只会出现一次，
从第3行到第N+2是只包含大小写英文字母的长度为M的字符串矩阵

## 输出描述
如果能在矩阵中连成给定的单词，则输出给定单词首字母在矩阵中的位第几行第几列
否则输出NO

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

区分大小写

## 解题思路
本题实现了简单的字符矩阵匹配问题。
通过递归算法来检查word是否存在于矩阵中。
遍历矩阵的每一个元素，如果发现字符串的第一个字符和该元素相同，
就递归检查这个字符串是否存在于以这个元素为起点的四周的位置。
## 解题代码

```python
def solve_method(matrix, word):
    def check(row, col, k, visited, word, matrix, m, n):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k] or [row, col] in visited:
            return False
        visited.append([row, col])
        if k == len(word) - 1:
            return True
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = check(row + d1, col + d2, k + 1, visited, word, matrix, m, n)
            if res:
                return res
        return False

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                visited = []
                res = check(i, j, 0, visited, word, matrix, m, n)
                if res:
                    return [i + 1, j + 1]
    return []


if __name__ == '__main__':
    M, N = input().strip().split(' ')
    word = input().strip()
    matrix = [list(input().strip()) for _ in range(int(N))]
    res = solve_method(matrix, word)
    if res:
        print(' '.join([str(res[0]), str(res[1])]))
    else:
        print('NO')
```

