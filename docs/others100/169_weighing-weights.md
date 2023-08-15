# 169 称砝码

## 题目描述

现有`n`种砝码，重量互不相等，分别为$m_1 ,m_2 ,m_3, \cdots, m_n$ 。每种砝码对应的数量为$x_1 ,x_2 ,x_3, \cdots, x_n$。

现在要用这些砝码去称物体的重量（放在同一侧），问能称出多少种不同的重量。

**注意：** 称重重量包括0

数据范围：每组输入数据满足 1 <= n <= 10、 1 <= m[i] <= 2000, 1 <= x[i] <= 10。

## 输入描述

对于每组测试数据:

- 第一行：`n`表示砝码的种数，取值范围是[1,10]。
- 第二行： $m_1, m_2, m_3, \cdots, m_n$表示每种砝码的重量，取值范围是[1,2000]
- 第三行： $x_1, x_2, x_3, \cdots, x_n$表示每种砝码对应的数量，取值范围是[1,10]

## 输出描述

利用给定的砝码可以称出的不同的重量数。

## 示例描述

### 示例一

**输入：**

```text
2
1 2
2 1
```

**输出：**

```text
5
```

**说明：**

可以表示出0、1、2、3、4五种重量。

## 解题思路

**基本思路：** 用动态规划的01背包问题求解。

1. 将所有砝码按照重量存入列表`new_weights`中。
2. 用动态规划的01背包问题方法：
    - 确定dp数组以及下标的含义：`dp[i]`表示能否使用给定的砝码组成为`i`的重量。
    - 确定递推公式：`dp[j]`可以表示为，想知道重量`j`是否存在为`True`，那么需要知道`dp[j-w]`即`j-w`重量是否存在为`True`，即`dp[j] = dp[j] or dp[j - w]`。
    - dp数组初始化：数组都初始化为`False`，`dp[0]`初始化为`True`。
    - 确定遍历顺序：砝码从前到后，重量从大到小。
3. 返回dp数组为`True`的个数，即能表示的重量的种类个数。

## 解题代码

```python
def solve_method(n, weights, nums):
    # 每个砝码的重量
    new_weights = []
    for i in range(n):
        new_weights.extend([weights[i]] * nums[i])
    # dp数组中的元素表示能否使用给定的砝码组成对应的重量
    # 默认重量为0也是一种，则初始化dp[0]=True。
    total_weight = sum(new_weights)
    dp = [False] * (total_weight + 1)
    dp[0] = True
    for w in new_weights:
        for j in range(total_weight, w - 1, -1):
            dp[j] = dp[j] or dp[j - w]
    return sum(dp)


if __name__ == '__main__':
    assert solve_method(2, [1, 2], [2, 1]) == 5
```



