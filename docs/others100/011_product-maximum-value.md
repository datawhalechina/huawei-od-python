# 011-乘积最大值

## 题目描述

给定一个元素类型为小写字符串的数组
请计算两个没有相同字符的元素长度乘积的最大值
如果没有符合条件的两个元素返回0

## 输入描述

输入为一个半角逗号分割的小写字符串数组Q
2<=数组长度<=100
0<字符串长度<=50

## 输出描述

两个没有相同字符的元素长度乘积的最大值

## 示例描述

### 示例一

**输入：**
```
iwdvpbn,hk,iuop,iikd,kadgpf
```

**输出：**
```
14
```

**说明：**  
数组中有5个元组第一个和第二个元素没有相同字符
满足条件输出7*2=14

## 解题思路

读入一个字符串，将字符串按照“，”分割成多个字符串存储在数组split中，然后遍历数组split,对于数组中的任意两个字符串，判断这两个字符串是否可以组成一个更大的字符串，如果可以，就更新最大的字符串的长度。最后，输出max_val。

## 解题代码

```python
# coding:utf-8
line = input().strip()
split = line.split(',')

max_val =0
for i in range(len(split)):
    for j in range(i,len(split)):
        chars = list(split[j])
        k = 0
        while k < len(chars):
            if split[i].find(chars[k]) != -1:
                break
            k += 1
        tmp = len(split[i]) * len(split[j])
        if k == len(chars) and tmp > max_val:
            max_val = tmp
print(max_val)
```

