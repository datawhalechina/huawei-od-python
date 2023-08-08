# 039 勾股数

## 题目描述

如果三个正整数`A`、`B`、`C`，满足$A^2 + B^2 = C^2$则为勾股数。

如果ABC之间两两互质，即`A`与`B`、`A`与`C`、`B`与`C`均互质没有公约数，则称其为勾股数元组。

请求出给定n\~m范围内所有的股数元组。

## 输入描述

输入n、m的值，表示起止范围，其中1 < n < 10000、n < m < 10000。 

## 输出描述

输出ABC，保证`A < B < C`，输出格式`A B C`。

多组勾股数元组，按照`A B C`升序的排序方式输出，若给定范围内，找不到勾股数元组时，输出`Na`。

## 示例描述

### 示例一

**输入：**

```text
1
20
```

**输出：**

```text
3 4 5
5 12 13
8 15 17
```

### 示例二

**输入：**

```text
5
10
```

**输出：**

```text
Na
```

## 解题思路

**基本思路：** 

1. 从`n`遍历到`m`：
   - 先根据题目求出勾股数A、B、C三个数
   - 对A、B、C三个数进行判断，如果两两互质`is_coprime`，则存入结果列表中。
2. 最后返回结果列表。

## 解题代码

```Python
import math


def solve_method(n, m):
    result = []

    # 判断是否是互质
    def is_coprime(a, b, c):
        return math.gcd(a, b) == 1 and math.gcd(b, c) == 1 and math.gcd(a, c) == 1

    # 求勾股数A、B、C
    for a in range(n, m + 1):
        for b in range(a + 1, m + 1):
            # c^2 = i^2+b^2
            c_squared = a ** 2 + b ** 2
            c = int(c_squared ** 0.5)
            if c_squared == c ** 2 and c <= m and is_coprime(a, b, c):
                result.append([a, b, c])

    return result if result else "Na"


if __name__ == '__main__':
    assert solve_method(1, 20) == [[3, 4, 5], [5, 12, 13], [8, 15, 17]]
    assert solve_method(5, 10) == "Na"
```



