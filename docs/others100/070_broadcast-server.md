# 070 广播服务器

## 题目描述

服务器连接方式包括直接相连，间接连接。
A和B直接连接，B和C直接连接，则A和C间接连接。直接连接和间接连接都可以发送广播。
给出一个N * N数组。代表N个服务器，
matrix[i][j]=1，则代表服务器i和j直接连接；
不等于1时，代表i和j不直接连接。matrix[i][i]==1,即自己和自已直接连接。
计算初始需要给几台服务器广播，才可以使每个服务器都收到广播。


## 输入描述
输入为N行，每行有N个数字，为0或1，由空格分隔，构成N*N的数组
，N的范围为1<=N<=40




## 输出描述
输出一个数字，为需要广播的服务器的数量




## 示例描述

### 示例一

**输入：**
```text
1 0 0
0 1 0
0 0 1
```

**输出：**
```text
3
```
### 示例二

**输入：**
```text
1 1 
1 1
```

**输出：**
```text
1
```

## 解题思路
无向图求连通分量个数，可以使用深度优先遍历来解决

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 070_broadcast-server
@time:  23/8/2023 下午 7:46
@project:  huawei-od-python 
"""


def solve_method(nums):
    def dfs(nums, visited, index):
        visited[index] = True
        for j in range(len(nums)):
            if nums[index][j] == 1 and not visited[j]:
                dfs(nums, visited, j)

    n = len(nums)
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(nums, visited, i)
            count += 1
    return count


if __name__ == '__main__':
    nums = [list(map(int, input().strip().split(' ')))]
    n = len(nums[0])
    for _ in range(n-1):
        nums.append(list(map(int, input().strip().split(' '))))
    res = solve_method(nums)
    print(res)


```

