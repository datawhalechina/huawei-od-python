# 033 分解质因数

## 题目描述

给定一个正整数，将其分解成两个质数的乘积，输出两个质数，按从小到大排序，有多组只需输出一组，如果没有则输出`NO`。

## 示例描述

### 示例一

**输入：**

```text
15
```

**输出：**

```text
3 5
```

### 示例二

**输入：**

```text
7
```

**输出：**

```text
NO
```

## 解题思路

1. 找出所有小于num的素数，存入因数为素数的`factors`集合中。
2. 遍历`factors`集合，找出两个素数，满足因数分解。
3. 如果找到，返回两个素数，如果找不到，返回`NO`。

## 解题代码

```Python
def solve_method(num):
    # 找出所有小于num的素数
    tmp = num
    f = 2
    factors = set()
    while tmp != 1:
        if tmp % f != 0:
            f += 1
        else:
            factors.add(f)
            tmp //= f

    # 找出两个素数，满足因数分解
    for f1 in factors:
        for f2 in factors:
            if f1 * f2 == num:
                return min(f1, f2), max(f1, f2)

    return "NO"


if __name__ == '__main__':
    assert solve_method(15) == (3, 5)
    assert solve_method(7) == "NO"
```

