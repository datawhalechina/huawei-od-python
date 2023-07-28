# 310 贪心的商人、最大利润

## 题目描述
商人经营一家店铺，有 `number` 种商品，
由于仓库限制每件商品的最大持有数量是 `item[index]`   
每种商品的价格是 `item-price[item_index][day]`  
通过对商品的买进和卖出获取利润  
请给出商人在days天内能获取的最大的利润  
注：同一件商品可以反复买进和卖出
## 输入描述
`3` 第一行输入商品的数量 `number`  
`3` 第二行输入商品售货天数 `days`  
`4 5 6` 第三行输入仓库限制每件商品的最大持有数量是 `item[index]`  
`1 2 3` 第一件商品每天的价格  
`4 3 2` 第二件商品每天的价格  
`1 5 3` 第三件商品每天的价格  

## 输出描述
输出商人在这段时间内的最大利润
例如：32

### 示例一
**输入：**
```shell
3
3
4 5 6
1 2 3
4 3 2
1 5 2
```

**输出：**
```shell
32
```

**说明：**  

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

**说明：**  

## 解题思路

我们只要找到商品价格走势的上升区段，然后低价allin买入，高价allout卖出即可求得最大利润
那么如何找到上升区段呢？
我们假设商品1的第i天的价格为 `price1[i]`，那么只要 `price1[i]<price1[i+1]`，则说明当前处于上升区段的低价位，因此可以allin，然后到`i+1`天的时候allout


## 解题代码

```python
# 输入获取
number = int(input())
days = int(input())
item = list(map(int, input().split()))
prices = [list(map(int, input().split())) for i in range(number)]
 
 
# 如果当前解法通过率较低，可以尝试将第5行的prices的初始化，改为下面这种，通过率应该会有所上升
# prices = []
# for i in range(number):
#     prices.append(list(map(int, input().split())))
#     print(0)
 
# 算法入口
def getResult(number, days, item, prices):
    """
    :param number: 几种商品
    :param days: 几天
    :param item: 每种商品的最大囤货数量
    :param prices: 每种商品的在days天内的价格变动情况
    :return: 最大利润
    """
    ans = 0
    for i in range(number):
        price = prices[i]
        for j in range(days - 1):
            if price[j] < price[j + 1]:
                ans += (price[j + 1] - price[j]) * item[i]
    return ans
 
 
# 算法调用
print(getResult(number, days, item, prices))
```