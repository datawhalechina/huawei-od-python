# 255 狼羊过河or羊、狼、农夫过河

## 题目描述

一农夫带着m只羊，n只狼过河，农夫有一条可载x只狼／羊的船；农夫在时或者羊的数量大于狼时，狼不会攻击羊；农夫在不损失羊的情况下，运输几次可以完成运输？（返程不计入次数）

## 输入描述

输入参数为m，n，x；

m为羊的数量、n为狼的数量、x为可载狼和羊的数量

## 输出描述

返回运输次数即可

**说明：** 如果无法完成运输返回0

## 示例描述

### 示例一

**输入：**
```text
5 3 3
```

**输出：**
```text
3
```

**详解**
```text
第一次：2只狼
第二次：三只羊
```

## 解题思路

**基本思路：**

存在重复子问题，所以可以用DFS
边界条件： 河两侧羊的数量大于狼的数量，或没有羊

**代码思路：**
1. DFS的输入参数如下
    - m0, n0表示剩余的羊和狼的数量
    - m1, n1表示运送到对岸的羊和狼的数量
    - x为船的容量，count为运输次数
2. DFS截止条件：全部运到对岸，即`m0 == 0 and n0 == 0`，记录当前运输次数
3. DFS核心函数
    - 尝试运输i只羊和j只狼
    - 不必运输0只羊和0只狼、狼羊的总数不能超出船的容量、离岸时两侧的狼羊数量满足要求
4. global变量`min_count`记录最小运输次数

## 解题代码
```python
def solve_method(m, n, x):
    # min_count为最小运输次数
    global min_count
    min_count = (m + n) * x
    dfs(m, n, 0, 0, x, 0)
    return 0 if min_count == (m + n) * x else min_count

# m0, n0表示剩余的羊和狼的数量
# m1, n1表示运送到对岸的羊和狼的数量
# x为船的容量，count为运输次数
def dfs(m0, n0, m1, n1, x, count):
    global min_count
    # 截止条件：全部运到对岸
    if m0 == 0 and n0 == 0:
        min_count = min(min_count, count)
        return

    # 尝试运输i只羊和j只狼
    for i in range(min(m0+1, x+1)):
        for j in range(min(n0+1, x+1)):
            # 不必运输0只羊和0只狼
            if i == 0 and j == 0:
                continue
            # 狼羊的总数不能超出船的容量
            if i + j > x:
                break
            # 离岸时检查两侧的狼羊数量
            if (m0 - i > n0 - j or m0 - i == 0) and (m1 + i > n1 + j or m1 + i == 0):
                dfs(m0 - i, n0 - j, m1 + i, n1 + j, x, count + 1)

if __name__ == "__main__":
    # m只羊，n只狼，x为船容量
    m, n, x = map(int, input().split())
    print(solve_method(m, n, x))

    assert solve_method(5, 3, 3) == 3
```