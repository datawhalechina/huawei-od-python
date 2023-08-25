# 076 打折买水果

## 题目描述

有`m`个水果超市在`1~n`个小时的不同时间段提供不同价格的打折水果，如果某餐厅每个小时都要新采购一种水果给餐厅使用的话，请选出`n`个小时内，采购水果的最便宜的花费总和。（假设`m`个超市打折时间段可以覆盖`n`小时）

## 输入描述

第1行输入是`n`，表示总小时数，取值范围是1 <= n < 2^10。

第2行输入是`m`，表示水果超市个数。

接下来的第3行到第`m+2`行，每行是长度为3的数组：`x[0] x[1] x[2]`，代表各超市在`x[0]~x[1]`小时（包含`x[1]`）提供价格为`x[2]`的水果。

## 输出描述

采购水果的最便宜的花费总和。

## 示例描述

### 示例一

**输入：**
```text
4
6
2 3 10
2 4 20
1 3 15
1 4 25
3 4 8
1 4 16
```

**输出：**
```text
41
```
**说明**

- 第1小时选15元的水果
- 第2小时选10元水果
- 第3小时选8元水果
- 第4小时选8元水果
  
所以，采购水果的最便宜的花费总和，共15+10+8+8=41。

### 示例二

**输入：**
```text
5
3
1 2 30
1 5 20
3 5 10
```

**输出：**
```text
70
```

## 解题思路

1. 构建时刻价格字典`hour_price_dict`，key为时刻，value为水果价格列表。
2. 遍历小时数，获取每个时刻的最小价格进行累加。
3. 返回累加值，即采购水果的最便宜的花费总和。

## 解题代码

```python
from collections import defaultdict


def solve_method(n, hour_prices):
    """
    :param n: 总小时数
    :param hour_prices: 不同时间段提供不同价格的打折水果的价格
    :return: 采购水果的最便宜的花费总和
    """
    hour_price_dict = defaultdict(list)

    # 构建时刻价格字典，key为时刻，value为水果价格列表
    for start_time, end_time, price in hour_prices:
        for x in range(start_time, end_time + 1):
            hour_price_dict[x].append(price)

    total_cost = 0
    for i in range(n):
        total_cost += min(hour_price_dict[i+1])

    return total_cost


if __name__ == '__main__':
    hour_prices = [[2, 3, 10],
                   [2, 4, 20],
                   [1, 3, 15],
                   [1, 4, 25],
                   [3, 4, 8],
                   [1, 4, 16]]
    assert solve_method(4, hour_prices) == 41

    hour_prices = [[1, 2, 30],
                   [1, 5, 20],
                   [3, 5, 10]]
    assert solve_method(5, hour_prices) == 70
```

