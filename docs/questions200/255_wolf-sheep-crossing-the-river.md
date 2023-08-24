# 255 狼羊过河、羊狼农夫过河

## 题目描述

一农夫带着`m`只羊和`n`只狼过河，农夫有一条可载`x`只狼/羊的船；农夫在时或者羊的数量大于狼时，狼不会攻击羊；农夫在不损失羊的情况下，需要几次可以完成运输？（返程不计入次数）

## 输入描述

输入参数为`m`、`n`、`x`，其中`m`为羊的数量、`n`为狼的数量、`x`为可载狼和羊的数量。

## 输出描述

返回运输次数即可，如果无法完成运输返回0。

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

**说明：**  
- 第1次：2只狼。
- 第2次：3只羊。
- 第3次：2只羊。
所以，需要3次。

## 解题思路

**基本思路：** 使用深度优先搜索DFS求解。
1. 初始化最小运输次数`min_count`。
2. 使用深度优先搜索：
   - 确定参数：剩余的羊的数量`m0`、剩余的狼的数量`n0`、运送到对岸的羊的数量`m1`、运送到对岸的狼的数量`n1`、船的容量`x`、运输次数`count`。
   - 终止条件：当全部羊狼运到对岸，则终止递归，记录最小运输次数。
   - 递归处理：遍历所有的羊狼：
       - 当羊和狼都为0时，继续当前遍历。
       - 当狼羊的总数超出船的容量时，跳出当前遍历。
       - 离岸时两侧的狼羊数量满足要求，继续递归。
3. 返回最小运输次数。    

## 解题代码

```python
def solve_method(m, n, x):
    # min_count为最小运输次数
    global min_count
    min_count = (m + n) * x
    dfs(m, n, 0, 0, x, 0)
    return 0 if min_count == (m + n) * x else min_count


def dfs(m0, n0, m1, n1, x, count):
    """
    :param m0: 剩余的羊的数量
    :param n0: 剩余的狼的数量
    :param m1: 运送到对岸的羊的数量
    :param n1: 运送到对岸的狼的数量
    :param x: 船的容量
    :param count: 运输次数
    """
    # 终止条件：全部运到对岸
    global min_count
    if m0 == 0 and n0 == 0:
        min_count = min(min_count, count)
        return

    # 尝试运输i只羊和j只狼
    for i in range(min(m0 + 1, x + 1)):
        for j in range(min(n0 + 1, x + 1)):
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
    # m, n, x = map(int, input().split())
    # print(solve_method(m, n, x))

    assert solve_method(5, 3, 3) == 3
```