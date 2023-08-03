# 313 预订酒店

## 题目描述

放暑假了，小明决定到某旅游景点游玩，他在网上搜索到了各种价位的酒店（长度为`n`的数组`A`），他的心理价位是`x`元，请帮他筛选出`k`个最接近`x`元的酒店（`n>=k>0`），并由低到高打印酒店的价格。

## 输入描述

第一行是`n`、`k`、`x`，`n`表示在网上搜索的酒店数量，`x`表示心理价位，`k`表示最接近心理价位的酒店个数。  

第二行是`n`个酒店的价格数组`A[0] A[1] A[2]...A[n-1]`

## 输出描述

按照从低到高输出筛选出的酒店价格。

## 示例描述

### 示例一

**输入：**

```text
10 5 6
1 2 3 4 5 6 7 8 9 10
```

**输出：**

```text
4 5 6 7 8
```

### 示例二

**输入：**

```text
10 4 6
10 9 8 7 6 5 4 3 2 1
```

**输出：**

```text
4 5 6 7
```

**说明：**
数组长度`n = 10`，筛选个数`k = 4`，目标价位`x = 6`。当4和8距离`x`相同时，优先选择价格低的4。

### 示例三

**输入：**

```text
6 3 1000
30 30 200 500 70 300
```

**输出：**

```text
200 300 500
```

## 备注

1. 酒店价格数组`A`和小明的心理价位`x`均为整型数据，取值范围是0 < n,k,x < 10000。 
2. 优先选择价格最接近心理价位的酒店，若两家酒店和心理价位差价相同，则选择价格较低的酒店。（比如100元和300元距离心理价位200元同样接近，此时选择100元）。
3. 酒店价格可能相同重复。

## 解题思路

1. 计算各个价格与心理价位的距离`near_prices`，数组中的元素值是一个元组，元组的第一个数表示酒店价格，元组的第二个数表示与心理价位的距离。
2. 对`near_prices`按照距离从小到大排序，距离相同时，按照价格从小到大排序。
3. 取前k个与心理价位最近的酒店价格，并排序。
4. 返回排序之后的酒店价格。

## 解题代码

```python
def solve_method(k, x, prices):
    near_prices = []

    # 计算各个价格与心理价位的距离
    for p in prices:
        near_prices.append((p, abs(p - x)))

    # 按照距离从小到大排序，距离相同时，按照价格从小到大排序
    near_prices.sort(key=lambda x: (x[1], x[0]))

    # 取前k个与心理价位最近的酒店价格
    ans = list(map(lambda x: x[0], near_prices[:k]))
    ans.sort()

    return ans


if __name__ == '__main__':
    assert solve_method(5, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 5, 6, 7, 8]
    assert solve_method(4, 6, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [4, 5, 6, 7]
    assert solve_method(3, 1000, [30, 30, 200, 500, 70, 300]) == [200, 300, 500]
```