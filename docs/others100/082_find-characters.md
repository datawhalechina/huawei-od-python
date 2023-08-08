# 082 找字符

## 题目描述

给定两个字符串，从字符串2中找出字符串1中的所有字符，去重并按照ASCII码值从小到大排列。

## 输入描述

字符范围满足ASCII编码要求，输入字符串1长度不超过1024，字符串2长度不超过100。

## 输出描述

按照ASCII由小到大排序。

## 示例描述

### 示例一

**输入：**
```text
bach
bbaaccddfg
```

**输出：**
```text
abc
```

### 示例二

**输入：**
```text
fach
bbaaccedfg
```

**输出：**
```text
acf
```

## 解题思路

1. 将字符串`str1`和字符串`str2`分别转换成对应的集合。
2. 求集合的交集，并按照字典序排序。
3. 组合成字符串后，返回结果。

## 解题代码

```python
def solve_method(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    return "".join(sorted(str1.intersection(str2)))


if __name__ == '__main__':
    assert solve_method("bach", "bbaaccddfg") == "abc"
    assert solve_method("fach", "bbaaccedfg") == "acf"
```