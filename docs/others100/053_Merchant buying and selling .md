# 053 商人买卖

## 题目描述

商人经营一家店铺，有`number`种商品，

由于仓库限制每件商品的最大持有数量是`item［index］`每种商品的价格是`item-price［item＿index］［day］` 通过对商品的买进和卖出获取利润

请给出商人在`days`天内能获取的最大的利润注：同一件商品可以反复买进和卖出

## 输入描述
3 第一行输入商品的数量`number`

3 第二行输入商品售货天数 `days`

4 5 6 第三行输入仓库限制每件商品的最大持有数量是`item［index］`

1 2 3第一件商品每天的价格

4 3 2 第二件商品每天的价格153第三件商品每天的价格

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

### 示例二

**输入：**

```text
1
1
1
1
```

**输出：**
```text
0
```
**编码思路**

该题的编码思路是通过给定的天数和物品数量，读入每个物品的购买数量和每个物品在每个给定的天数的价格。对于每个物品，找到在购买它的那一天和之前的价格差最大的一天。然后将这个差乘以物品的购买数量，并将所有物品的差之和加起来。这是一种简单的贪心算法Q，它寻找最便宜的价格买入并在最高价格处卖出，而不考虑其他价格点。重要的是要使用max（）函数来找到在所有天数中的最大价格差。在内部循环中，要从后往前遍历，因为要找到最大的差。此外，还需要注意 Python 中的列表和数组索引是从零开始的，而不是从一开始的。

**核心知识点**
Python 中的列表索引是从零开始的。

可以使用for循环以及range（）函数来遍历列表和数组。可以使用max（）函数找到列表或数组中的最大值

**使用说明**
参加华为od机试，一定要注意不要完全背诵代码，需要理解之后模仿写出，通过率才会高。

## 解题代码

```python
def main():
    # 读取物品数量和天数
    number, _ = map(int, input().split())
    # 读取每个物品的数量
    items = list(map(int, input().split()))
    # 读取每个物品在不同天数的价格
    prices = [list(map(int, input().split())) for _ in range(number)]
    # 调用求解函数，并打印最终结果
    print(solve(items, prices))


def solve(items, prices):
    total_sum = 0  # 初始化总和

    # 遍历每个物品的数量和价格
    for item, price in zip(items, prices):
        # 计算每个物品在不同天数的最大价格差异
        # 使用列表推导式遍历所有价格，并找到两个不同天数的价格之间的最大差值
        print("Price list for current item:", price)
        max_diff = max(price[i] - price[j] for i in range(len(price)) for j in range(i) if i != j)

        # 将最大价格差异与该物品的数量相乘，并累加到总和中
        total_sum += item * max_diff

    return total_sum  # 返回总和


if __name__ == "__main__":
    main()  # 调用主函数

```

