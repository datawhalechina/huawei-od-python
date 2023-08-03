# 039 勾股数

## 题目描述

如果三个正整数`A，B，C`，`A^2 + B^2 = C^2` 则为勾股数
如果ABC 之间两两互质，即`A 与B，A与C，B 与C` 均互质没有公约数，则称其为勾股数元组.
请求出给定 n ~ m 范围内所有的股数元组

## 输入描述

起始范围

`1 < n < 10000 
 n < m < l0000` 

## 输出描述

ABC保证`A < B < C`
输出格式`A B C`
多组勾股数元组，按照 `A B C` 升序的排序方式输出
若给定范围内，找不到勾股数元组时，输出 `Na`。

## 示例描述

### 示例一

**输入：**

```Plain Text
3
20
```

**输出：**

```Plain Text
3 4 5
5 12 13
8 15 17
```

### 示例二

**输入：**

```Plain Text
5
10
```

**输出：**

```Plain Text
Na
```

## 解题思路

**基本思路：** 

1. 先根据题目求出勾股数A、B、C三个数

2. 再对A、B、C三个数进行判断，如果两两互质，则放入`result`。

3. 最后返回`result`

## 解题代码

```Python
def solve(n, m):
    result = []
    
    # 判断是否是互质
    def is_coprime(a, b, c):
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x
        
        return gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) == 1
    
    # 求勾股数A、B、C
    for a in range(n, m+1):
        for b in range(a, m+1):
            # c^2 = a^2+b^2
            c_squared = a**2 + b**2
            c = int(c_squared ** 0.5)
            if c_squared == c**2 and c <= m and is_coprime(a, b, c):
                result.append((a, b, c))
    
    return result

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    res = solve(n,m)
    print(res)
```



