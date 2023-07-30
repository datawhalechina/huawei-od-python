# 080 找单词

## 题目描述

给一个字符串和一个二维字符数组Q，如果该字符串存在于该数组中，
则按字符串的字符顺序输出字符串每个字符所在单元格的位置下
标字符串，如果找不到返回字符串N。
1. 需要按照字符串的字符组成顺序搜索，
且搜索到的位置必须是相邻单元格，其中"相邻单元格"是指那些水平相邻或垂直相邻的单元格。
2. 同一个单元格内的字母不允许被重复使用。
3. 假定在数组中最多只存在一个可能的匹配。

## 输入描述
1. 第1行为一个数字N指示二维数组在后续输入所占的行数。
2. 第2行到第N+1行输入为一个二维大写字符数组，每行字符用半角，分割。
3. 第N+2行为待查找的字符串，由大写字符组成。
4. 二维数组的大小为N*N，0<N<=100 
5. 单词长度K，0<K<1000。



## 输出描述
输出一个位置下标字符串，拼接格式为:
第1个字符行下标+","+第1个字符列下标+","+第2个字符行下标+","+第2个字符列
下标...+","+第N个字符行下标+“,"+第N个字符列下标
## 示例描述

### 示例一

**输入：**
```text
4
A,C,C,F
C,D,E,D
B,E,S,S
F,E,C,A
ACCESS

```

**输出：**
```text
0,0,0,1,0,2,1,2,2,2,2,3
```
**说明：**
ACCESS 分别对应二维数组的[0,0][0,1][0,2][1,2] [2,2] [2,3]下标位置

## 解题思路
本题实现了简单的字符矩阵匹配问题。
通过递归算法来检查word是否存在于矩阵中。
遍历矩阵的每一个元素，如果发现字符串的第一个字符和该元素相同，
就递归检查这个字符串是否存在于以这个元素为起点的四周的位置。
## 解题代码

```python
def solve_method(matrix, word):
    def check(row, col, k, word, matrix, m, n):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k]:
            return []
        if k == len(word) - 1:
            return [[row, col]]
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = check(row + d1, col + d2, k + 1, word, matrix, m, n)
            if res:
                return [[row, col]] + res
        return []

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                res = check(i, j, 0, word, matrix, m, n)
                if res:
                    return res
    return []


if __name__ == '__main__':
    N = int(input().strip())
    matrix = [input().strip().split(',') for _ in range(N)]
    word = input().strip()
    res = solve_method(matrix, word)
    if res:
        print(','.join([','.join([str(item[0]), str(item[1])]) for item in res]))
    else:
        print('N')
```

