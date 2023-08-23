# 256 硬件产品销售方案

## 题目描述

某公司目前推出了AI开发者套件、AI加速卡、AI加速模块、AI服务器、智能边缘多种硬件产品，每种产品包含若干个型号。现某合作厂商要采购金额为`amount`元的硬件产品搭建自己的AI基座。假设当前库存有`N`种产品，每种产品的库存量充足，给定每种产品的价格，记为`price`（不存在价格相同的产品型号）。请为合作厂商列出所有可能的产品组合。

## 输入描述

输入包含采购金额`amount`和产品价格列表`price`。第一行为`amount`，第二行为`price`。例如：
```
500
[100,200,300,500]
```

## 输出描述

输出为组合列表。例如：

`[[500], [200, 300], [100,200, 200], [100, 100,300], [100, 100, 100,200],[100,100,100, 100,100]]`

## 备注

1．对于给定输入，产品组合少于150种。输出的组合为一个数组，数组的每个元素也是一个数组，表示一种组合方案。如果给定产品无法组合金额为`amount`元的方案，那么返回空列表。
2．两种组合方案，只要存在一种产品的数量不同，那么方案认为是不同的。
3．每种产品型号价格不相同。
4. 1 <= 产品类型数量 <= 30。
5. 100 <= 产品价格 <= 20000。
6. 100 <= 采购金额 <= 50000。

## 示例描述

### 示例一

**输入：**
```text
500
[100, 200, 300, 500]
```

**输出：**
```text
[[100, 100, 100, 100, 100], [100, 100, 100, 200], [100, 100, 300], [100, 200, 200], [200, 300], [500]]
```

### 示例二

**输入：**
```text
100
[100]
```

**输出：**
```text
[[100]]
```

## 解题思路

**基本思路：** 使用深度优先搜索DFS求解。
1. 对产品价格列表`prices`从小到大进行排序。
2. 进行深度优先搜索：
   - 确定参数：产品价格列表`prices`、采购金额`amount`、遍历索引`index`、当前组合`combination`、组合列表`combinations`。
   - 终止条件：当`amount`等于0，说明已经找到了一个组合，存入组合列表中；或者最小的价格大于amount，说明没有解。
   - 递归处理：遍历所有产品价格，如果当前价格小于`amount`，则加入当前组合中，并从采购金额中减去当前价格，继续递归。
3. 返回组合列表。   

## 解题代码

```python
def solve_method(amount, prices):
    prices.sort()
    combinations = []
    dfs(prices, amount, 0, [], combinations)
    combinations.sort(key=lambda x: (x[0], -len(x)))
    return combinations


def dfs(prices, amount, index, combination, combinations):
    # 当前amount等于0，说明已经找到了一组解
    if amount == 0:
        combinations.append(combination)
        return
    # 最小的价格大于amount，说明没有解
    if index >= len(prices) or prices[index] > amount:
        return

    for i in range(index, len(prices)):
        if prices[i] <= amount:
            dfs(prices, amount - prices[i], i, combination + [prices[i]], combinations)


if __name__ == "__main__":
    # 500
    # [100, 200, 300, 500]
    # amount = int(input().strip())
    # prices = list(map(int, input().strip('[').strip(']').split(',')))
    # print(solve_method(amount, prices))

    assert sorted(solve_method(500, [100, 200, 300, 500])) == [[100, 100, 100, 100, 100], [100, 100, 100, 200],
                                                               [100, 100, 300], [100, 200, 200], [200, 300], [500]]

    assert sorted(solve_method(100, [100])) == [[100]]
```