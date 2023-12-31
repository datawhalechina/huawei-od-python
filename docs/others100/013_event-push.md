# 013 事件推送

## 题目描述

同一个数轴`X`上有两个点的集合`A={A1,A2,...,Am}`和`B={B1,B2,...,Bn}`，`Ai`和`Bj`均为正整数，`A`、`B`已经按照从小到大排好序，`A`、`B`均不为空。

给定一个距离`R`（正整数），列出同时满足如下条件的所有`(Ai,Bj)`数对：

1. `Ai <= Bj`。
2. `Ai`、`Bj`之间的距离小于等于`R`。
3. 在满足1、2的情况下，每个`Ai`只需输出距离最近的`Bj`。
4. 输出结果按`Ai`从小到大的顺序排序。

## 输入描述

第1行三个正整数`m`、`n`、`R`。

第2行`m`个正整数，表示集合`A`。

第3行`n`个正整数，表示集合`B`。

输入限制：

- 1 <= R <= 100000
- 1 <= n,m <= 100000
- 1 <= Ai,Bj <= 1000000000

## 输出描述

每组数对输出一行`Ai`和`Bj`，以空格分隔。

## 示例描述

### 示例一

**输入：**
```
4 5 5
1 5 5 10
1 3 8 8 20 
```

**输出：**
```
1 1
5 8 
5 8
```

## 解题思路

1. 初始化集合B的索引`index`。
2. 遍历集合A：
    - 遍历集合B：
        - 当当前A集合的数字小于当前B[index]的值，并且二者距离小于等于`R`，则将两数存入结果列表中，退出集合B的遍历，继续集合A的遍历。
        - 索引`index`累加，继续遍历集合B。
3. 返回结果列表。

## 解题代码

```python
def solve_method(A, B, R):
    result = []
    index = 0
    for a in A:
        while index < len(B):
            if a <= B[index] and B[index] - a <= R:
                result.append([a, B[index]])
                break
            index += 1

    return result


if __name__ == '__main__':
    A = [1, 5, 5, 10]
    B = [1, 3, 8, 8, 20]
    assert solve_method(A, B, 5) == [[1, 1], [5, 8], [5, 8]]
```