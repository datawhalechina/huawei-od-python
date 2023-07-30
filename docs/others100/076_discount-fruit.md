# 076 打折买水果

## 题目描述

有m个水果超市（橡皮擦开的)在1一n个小时的不同时间段提供不同价格的打折水果，
如果某餐厅每个小时都要新采购一种水果给餐厅使用的话，请选出n个小时内，采购水果的最便宜的花费总和。
(假设m个超市打折时间段可以覆盖n小时)

## 输入描述
+ n：总小时数
+ m：水果超市个数
+ x[0]x[1]×[2]：第2~m+1行：每行长度为3的数组，代表各超市在×[0]~x[1]小时(包含〔x1]）提供价格为[x2]的水果。
范围提示：1<=n<210(1024)


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

第1小时选15元的水果，第2小时10元水果，第3选8元水果，第4小时选8元水果，共15+10+8+8=41。


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
## 解题代码

```python
def solve_method(m, n, price):
    '''
    m:水果超市个数
    n:小时数
    :param m:
    :param n:
    :param price:
    :return:
    '''
    price = sorted(price, key=lambda x: x[2])
    cost = 0
    for i in range(n):
        for j in range(m):
            if price[j][0] <= i + 1 <= price[j][1]:
                cost += price[j][2]
                break
    return cost


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    price = [list(map(int, input().strip(' '))) for _ in range(m)]
    res = solve_method(m, n, price)
    print(res)
```

