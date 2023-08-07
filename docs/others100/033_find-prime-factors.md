# 033 分解质因数

## 题目描述

给定一个正整数，将其分解成两个质数的乘积，输出两个质数，按从小到大排序，有多组只需输出一组，如果没有则输出 NO.

## 示例描述

### 示例一

**输入：**

```Plain Text
15
```

**输出：**

```Plain Text
3 5
```

### 示例二

**输入：**

```Plain Text
7
```

**输出：**

```Plain Text
NO
```

## 解题思路

基本思路：将num分解成两个整数相乘，然后分别判断是否都是质数。如果是返回结果，不是返回`NO`

## 解题代码

```Python
def find_prime_factors(num):  
    # 判断是否是质数
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # 将num分解成两个数相乘
    for i in range(2, num):
        if num % i ==0:
            if is_prime(i) and is_prime(num // i):
                return (i, num // i)
    
    return "NO"

if __name__ == '__main__':
    num = int(input())
    result = find_prime_factors(num)
    print(result)
```

