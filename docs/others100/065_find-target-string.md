# 065 寻找目标字符串


## 题目描述

给定一个字符串
和一个二维字符数组Q，
如果该字符串存在于该数组当中，
则按照字符串的字符顺序输出字符串每个字符所在单元格的位置下标。字符串如果找不到返回字符串"N"
1. 需要按照字符串的字符组成顺序搜索，
且搜索到的位置必须是相邻单元格
其中"相邻单元格"是指那些水平相邻或垂直相邻的单元格
2. 同一个单元格内的字母不允许被重复使用
3. 假定在数组中最多只存在一个可能的匹配



## 输入描述

1. 第一行为一个数字(N)，
指示二维数组在后续输入所占的行数
2. 第二行到第N+1行输出为二维大写字符串数组，每行字符用半角逗号分割
3. 第N+2行为待查找的字符串。
由大写字符组成
4. 字符数组的大小为N*N,0 < N <= 1005.单词长度为K，0 < K < 1000

## 输出描述
输出一个位置下标字符串，拼接格式为：

第一个字符行下标+","+第一个字符列下标+","+第二个字符行下标+","+
第二个字符列下标....+","+第N个字符行下标+","+第N个字符列下标

## 示例描述

### 示例一

**输入：**
```text
4
A,C,C,F
C,D,E,D
D,E,S,S
F,E,C,A
ACCESS
```

**输出：**
```text
0,0,0,1,0,2,1,2,2,2,2,3
```
**说明：**

ACCESS分别对应二维数组的[0,0][0,1][0,2] [1,2] [2,2] [2,3]下标位置


## 解题思路
二位数组循环遍历，首先判断第一个字母是否能匹配，若能匹配深度优先遍历，尝试找到完整路径
  

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 065_find-target-string
@time:  21/8/2023 下午 4:32
@project:  huawei-od-python 
"""


def solve_method(nums, target):
    def infect(row, col, k, m, n, nums, target):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or (k < len(target) and nums[row][col] != target[k]):
            return []
        if k == len(target) - 1 and nums[row][col] == target[k]:
            return [[row, col]]

        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            value = nums[row][col]
            nums[row][col] = '#'
            res = infect(row + d1, col + d2, k + 1, m, n, nums, target)
            nums[row][col] = value
            if res:
                return [[row, col]] + res
        return []

    m, n = len(nums), len(nums[0])
    for i in range(m):
        for j in range(n):
            if nums[i][j] == target[0]:
                ans = infect(i, j, 0, m, n, nums, target)
                if ans:
                    return ','.join([','.join([str(item[0]), str(item[1])]) for item in ans])
    return 'N'


if __name__ == '__main__':
    n = int(input().strip())
    nums = []
    for _ in range(n):
        nums.append(input().strip().split(','))
    target = input().strip()
    res = solve_method(nums, target)
    print(res)

```

