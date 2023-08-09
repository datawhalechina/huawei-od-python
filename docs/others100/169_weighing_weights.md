# 169 称砝码

## 题目描述

现有 $n$ 种砝码，重量互不相等，分别为 $m_1 ,m_2 ,m_3 ...m_n$ 。每种砝码对应的数量为 $x_1 ,x_2 ,x_3 ....x_n$ 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。

**注意:**

称重重量包括0

数据范围:每组输入数据满足1≤ $n$ ≤10 , 1≤ $m_i$ ≤2000,1≤ $x_i$ ≤10



## 输入描述

对于每组测试数据:

- 第—行: n—砝码的种数(范围[1,10])
- 第二行: $m_1 m_2 m_3 ... m_n$，每种砝码的重量(范围[1,2000])
- 第三行: $x_1, x_2, x_3 ... x_n$，每种砝码对应的数量(范围[1,10])



## 输出描述

利用给定的砝码可以称出的不同的重量数



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

可以表示出0，1，2，3，4五种重量。



## 解题思路

**基本思路：**

这一题明显是一个背包问题。

因为每个砝码有多个次数，所以实际上是个多重背包问题，但是多重背包可以转化为简单的01背包，即将多个相同砝码都合并到一起。所以两个做法皆可。

dp 数组中的元素表示能否使用给定的砝码组成对应的重量，而不是最大价值。默认重量为0也是一种，则初始化dp[0]=True。

dp[j] = dp[j] or dp[j-w] 为状态转移方程。

它的含义是，想知道重量j是否存在为True，那么需要知道dp[j-w]即j-w重量是否存在为True，因为加上w就是j重量。但并不是所有dp[j-w]都存在，那么就可能让dp[j]变为False，所以我们加个dp[j] or 表示已经有w重量的物品能让重量变为j为True，后面即便有False也不改变它。

最终dp中不同背包大小，能被装满的背包已经被标注为True，不能的默认为False，最后返回求和sum即可。

## 解题代码

```python
# 01背包
def solve_method1(n, weights, nums):
    new_weights = []
    for i in range(n):
        new_weights.extend([weights[i]]*nums[i])
    # dp 数组中的元素表示能否使用给定的砝码组成对应的重量，而不是最大价值。
    # 默认重量为0也是一种，则初始化dp[0]=True。
    total_weight = sum(new_weights)
    dp = [False]*(total_weight+1)
    dp[0]=True
    for w in new_weights:
        for j in reversed(range(w, total_weight+1)):
            dp[j] = dp[j] or dp[j-w]
            # 标准01背包状态转移方程，求装满j的最大重量
            # dp[j] = max(dp[j], dp[j-w]+w)
    return sum(dp)

# 多重背包
def solve_method2(n, weights, nums):
    total_weight = sum([weights[i]*nums[i] for i in range(len(weights))])
    dp = [False] * (total_weight + 1)
    dp[0] = True
    # 循环物品
    for i in range(len(weights)):
        # 循环物品数量
        for k in range(1, nums[i]+1):
            # 循环背包
            for j in range(total_weight, weights[i]-1, -1):
                # 背包 与 物品及物品数量的关系
                if j >= k * weights[i]:
                    dp[j] = dp[j] or dp[j - k * weights[i]]
    return sum(dp)

if __name__ == '__main__':
    assert solve_method1(2, [1,2],[2,1]) == 5
    assert solve_method2(2, [1,2],[2,1]) == 5
```



