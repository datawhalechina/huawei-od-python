# 047 贪心的商人、最大利润

## 题目描述

商人经营一家店铺，有`number`种商品，由于仓库限制每件商品的最大持有数量是`item[index]`，每种商品每天的价格是`item-price[item_index][day]`

通过对商品的买进和卖出获取利润，请给出商人在`days`天内能获取的最大的利润。

注：同一件商品可以反复买进和卖出

## 输入描述

第一行输入商品的数量`number`。  
第二行输入商品售货天数`days`。  
第三行输入仓库限制每件商品的最大持有数量是 `item[index]`。
以下`numbers`行，输入每件商品每天的价格。

## 输出描述

输出商人在这段时间内的最大利润。

## 示例描述

### 示例一
**输入：**
```text
3
3
4 5 6
1 2 3
4 3 2
1 5 2
```

**输出：**
```text
32
```

**说明：**  

根据输入的信息可知：
```text
number = 3
days = 3
item[3] = {4, 5, 6}
item_price[3][3] = {{1, 2, 3}, {4, 3, 2}, {1, 5, 2}}
```
以下是计算步骤：
- 针对第1件商品，商人在第1天的价格是`item_price[0][0]=1`，买入`itme[0]`件，在第3天`item_price[0][2]=3`的时候卖出，获利最大是8。
- 针对第2件商品，不进行交易，获利最大是0。
- 针对第3件商品，商人在第1天的价格是`item_price[2][0]=1`，买入`item[2]`件，在第2天`item_price[2][1]=5`的时候卖出，获利最大时候24。
因此，这段时间中，商人能获取的最大利润是8+24=32。
  
### 示例二
**输入：**
```shell
1
1
1
1
```

**输出：**
```shell
0
```

## 解题思路

**基本思路：** 使用动态规划求解。
1. 遍历每种商品，使用动态规划计算该商品的最大利润。
2. 动态规划计算最大利润：
    - 确定`dp`数组以及下标的含义：`dp[i][0]`表示第`i`天持有商品所得现金，`dp[i][1]`表示第`i`天不持有商品所得最多现金。
    - 确定递推公式：
        - 第i天持有商品所得现金=第i-1天持有商品与第i天买入商品的最大值：`dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])`
        - 第i天不持有商品所得最多现金=第i-1天不持有商品和第i天卖出商品的最大值：`dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])`
    - `dp`数组如何初始化：
        - `dp[0][0]`表示第0天持有商品所得现金，即买入商品，为`-prices[0]`。
        - `dp[0][1]`表示第0天不持有商品，为0。
    - 确定遍历顺序：从前先后。
3. 根据计算出的最大利润，乘以商品的件数，累加得到最大利润总和。
4. 返回商人在这段时间内的最大利润。

## 解题代码

```python
def max_profit(prices) -> int:
    length = len(prices)
    # dp[i][0] 表示第i天持有商品所得现金。
    # dp[i][1] 表示第i天不持有商品所得最多现金
    dp = [[0] * 2 for _ in range(length)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0
    for i in range(1, length):
        # 第i天持有商品所得现金=第i-1天持有商品与第i天买入商品的最大值
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        # 第i天不持有商品所得最多现金=第i-1天不持有商品和第i天卖出商品的最大值
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
    return dp[-1][1]


def solve_method(number, days, item, item_price):
    """
    :param number: 商品种类数量
    :param days: 天数
    :param item: 每种商品的个数
    :param item_price: 每种商品每天的价格
    :return: 最大利润
    """

    ans = 0
    for i in range(number):
        # 该种商品每天的价格
        prices = item_price[i]
        ans += max_profit(prices) * item[i]
    return ans


if __name__ == '__main__':
    item_price = [[1, 2, 3],
                  [4, 3, 2],
                  [1, 5, 2]]
    assert solve_method(3, 3, [4, 5, 6], item_price) == 32
    assert solve_method(1, 1, [1], [[1]]) == 0
```