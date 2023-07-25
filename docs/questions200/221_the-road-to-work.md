# 221 上班之路

## 题目描述

Jungle生活在美丽的蓝鲸城，大马路都是方方正正，但是每天马路的封闭情况都不一样。  
地图由以下元素组成：

1. `.` — 空地，可以达到;
2. `*` — 路障，不可达到;
3. `S` — Jungle的家;
4. `T` — 公司.  

    其中我们会限制Jungle拐弯的次数，同时Jungle可以清除给定个数的路障，现在你的任务是计算Jungle是否可以从家里出发到达公司。

## 输入描述

输入的第一行为两个整数 $t,c（0≤t,c≤100）$, $t$ 代表可以拐弯的次数，$c$ 代表可以清除的路障个数。  
输入的第二行为两个整数 $n,m（1≤n,m≤100）$,代表地图的大小。  
接下来是 $n$ 行包含 $m$ 个字符的地图。$n$ 和 $m$ 可能不一样大。  
我们保证地图里有 $S$ 和 $T$。

## 输出描述

输出是否可以从家里出发到达公司，是则输出`YES`，不能则输出`NO`。

## 示例描述
### 示例一

**输入**
```
2 0
5 5
..S..
****.
T....
****.
.....
```

**输出**
```
YES
```
### 示例二

**输入**
```
1 2
5 5
.*S*.
*****
..*..
*****
T....
```
**输出**
```
NO
```
**说明**

该用例中，至少需要拐弯1次，清除3个路障，所以无法到达

## 解题思路
**相关知识点**：

`图的模拟；深度优先搜索；队列；集合；二维数组`

**简单提示**：
通过DFS进行模拟，将寻找一条可行路径抽象为走到公司，或继续找遍历其他路径。

**分析输入输出要求**：

- 对输入的分析如下图所示：
![示例输入分析](images/221-001-sample-analysis.png?width=50%) 

**一种可行的算法步骤**：
1. 找到地图中的起点S，并将其标记为已访问。
2. 开始DFS，判断当前位置是否为终点，如果是，则返回YES。
   ![算法步骤](images/221-002-dfs-description.png?width=50%) 
   - 如果不是终点，则遍历该节点的上下左右四个方向，对于每个方向，判断是否在地图范围内，是否可达（空地或路障），是否已经访问过。
   - 如果调整了方向，判断是否还有拐弯次数，如果没有则当前方向不可行；
   - 如果是路障，判断是否还有清除路障的次数，如果没有则当前方向不可行；
   - 如果当前方向没有前面的问题，则继续就当前方向进行新一轮的DFS；
   - 直到走到终点，或尝试完起点的四个方向，结束DFS。如果没有找到终点，则返回NO。

**代码debug说明**
![调试代码时的截图](images/221-003-debug.png?width=50%) 
根据上图所示，使用for循环，去尝试当前节点的四个方向，
- 如果 **走出范围** 或 **已经走过** 或 **没有转弯次数** 或 **没有清障次数**，则说明当前方向不可行，继续尝试其他方向或回退此位置。
- 如果 没有前面的问题，则可继续使用新的位置去进行DFS，搜索可行路径。

## 解题代码
```python
from collections import defaultdict

# DFS搜索函数
def dfs(i, j, ut, uc, last_dir, path):
    # 达到目标(公司) return True
    if matrix[i][j] == 'T':
        return True 

    # 使用DFS的方式，尝试四个方向 上、下、左、右，i是行，j是列
    for di, dj, dir in [(-1, 0, 1), (1, 0, 2), (0, -1, 3), (0, 1, 4)]:        
        # 计算下一个位置的新 行、列值
        newI, newJ = i + di, j + dj  
        
        # 检查边界以及是否已访问
        if 0 <= newI < N and 0 <= newJ < M:
            pos = newI * M + newJ # 计算新位置的值
            if pos in path:  
                continue
            
            flagT = 0
            # 检查转向次数，如果还有次数可以记录消耗次数
            if last_dir and last_dir != dir:
                if ut + 1 > T: continue
                flagT = 1
                
            flagC = 0
            # 检查清障次数，如果还有次数可以记录消耗次数
            if matrix[newI][newJ] == '*':
                if uc + 1 > C: continue
                flagC = 1
                
            # 添加坐标到访问记录
            path.add(pos)  
            
            # DFS递归，继续走看能否到达 ‘T’
            ut, uc = ut + flagT, uc + flagC
            if dfs(newI, newJ, ut, uc, dir, path):
                return True

            # 回溯移除坐标，减去未成功消耗的次数
            path.remove(pos)
            ut, uc = ut - flagT, uc - flagC
            
    return False

def solution(M , N, matrix):
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'S':                
                # 从起点(Jungle的家)开始DFS
                path = set()
                path.add(i * M + j)  # 使用 i * M + j 来表示具体位置
                return "YES" if dfs(i, j, 0, 0, 0, path) else  "NO"
            
    return "NO"

if __name__ == '__main__':
    # 输入参数，按照格式，分别代表 转弯次数、清障次数、地图 行、列
    T, C = map(int, input().split())  
    N, M = map(int, input().split())
    # 将地图内容读取成为矩阵列表
    matrix = [list(input()) for _ in range(N)]

    print(solution(M, N, matrix))
```