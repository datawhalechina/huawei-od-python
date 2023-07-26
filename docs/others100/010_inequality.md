# 010 不等式

## 题目描述

给定一组不等式，判断是否成立并输出不等式的最大差（输出浮点数的整数部分）

要求：
1. 不等式系数为double类型，是一个二维数组。
2. 不等式的变量为int类型，是一维数组。
3. 不等式的目标值为double类型，是一维数组。
4. 不等式约束为字符串数组，只能是大于、大于等于、小于、小于等于、等于。

例如：不等式组： 
```text
a11*x1+a12*x2+a13*x3+a14*x4+a15*x5<=b1 
a21*x1+a22*x2+a23*x3+a24*x4+a25*x5<=b2 
a31*x1+a32*x2+a33*x3+a34*x4+a35*x5<=b3
```

则不等式的最大差：
```
最大差=max{
(a11*x1+a12*x2+a13*x3+a14*x4+a15*x5-b1),
(a21*x1+a22*x2+a23*x3+a24*x4+a25*x5-b2),
(a31*x1+a32*x2+a33*x3+a34*X4+a35*x5-b3)
}
```

输出的数字类型为整数（输出浮点数的整数部分）。

## 输入描述

1. 不等式组系数（double类型）
```text
a11,a12,a13,a14,a15
a21,a22,a23,a24,a25
a31,a32,a33,a34,a35
```   

2. 不等式变量（int类型）
```text
x1,x2,x3,x4,x5
```
   
3. 不等式目标值（double类型）
```text
<=,<=,<=
```   
   
输入：
```text
a11,a12,a13,a14,a15;a21,a22,a23,a24,a25;a31,a32,a33,a34,a35;x1,x2,x3,x4,x5;<=,<=,<=
```

## 输出描述

## 示例描述

### 示例一

**输入：**
```
2.3,3,5.6,7,6;11,3,8.6,25,1;0.3,9,5.3,66,7.8;1,3,2,7,5;340,670,80.6;<=,<=,<=
```

**输出：**
```
false 458
```

### 示例二

**输入：**
```
2.36,3,6,7.1,6;1,30,8.6,2.5,21;0.3,69,5.3,6.6,7.8;1,13,2,17,5;340,67,300.6;<=,>=,<=
```

**输出：**
```
false 758
```

## 解题思路

1. 使用`zip`方法，计算每一个表达式：
    - 计算左侧的值`value`。
    - 计算误差`e`。
    - 验证不等式是否成立，得到验证结果。
    - 将误差存入到结果列表中。
2. 使用`max`方法，得到最大差。    
3. 返回表达式的验证结果和最大差。

## 解题代码

```python
def check_and_calc(value, b, sign):
    if sign == ">":
        return value > b
    elif sign == "<":
        return value < b
    elif sign == ">=":
        return value >= b
    elif sign == "<=":
        return value <= b
    elif sign == "=":
        return value == b


def solve_method(A, X, B, signs):
    result = []
    right = True
    for a, b, sign in zip(A, B, signs):
        # 计算左侧value值
        value = 0
        for i in range(len(a)):
            value += a[i] * X[i]

        # 计算误差
        e = int(abs(value - b))
        # 验证不等式是否成立
        right = check_and_calc(value, b, sign) and right
        # 存储误差
        result.append(e)
    
    return "true" if right else "false", max(result)


if __name__ == '__main__':
    A = [[2.3, 3, 5.6, 7, 6],
         [11, 3, 8.6, 25, 1],
         [0.3, 9, 5.3, 66, 7.8]]
    X = [1, 3, 2, 7, 5]
    B = [340, 670, 80.6]
    sign = ["<=", "<=", "<="]
    assert solve_method(A, X, B, sign) == ("false", 458)

    A = [[2.36, 3, 6, 7.1, 6],
         [1, 30, 8.6, 2.5, 21],
         [0.3, 69, 5.3, 6.6, 7.8]]
    X = [1, 13, 2, 17, 5]
    B = [340, 67, 300.6]
    sign = ["<=", "<=", "<="]
    assert solve_method(A, X, B, sign) == ("false", 758)
```

