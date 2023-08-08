# 161 - 环中最长子串

## 题目

给你一个字符串`s`，首位相连成一个环形，请你在环中找出`o`字符出现了偶数次最长子字符串的长度。

**备注：**

$1<= s.length<=5 \times 10^5$

`s`只包含小写英文字母



## 输入

输入是一个小写字母组成的字符串



## 输出描述

输出是一个整数



## 示例一

### 输入

```python
alolobo
```

### 输出

```
6
```

### 说明

最长子字符串之一是`alolob`，它包含`2`个`o`



## 示例二

### 输入

```
looxdolx
```

### 输出

```
7
```

### 说明

最长子字符串`oxdolxl`，由于是首尾连接一起的，所以最后一个`x`和开头的`l`是连接在一起的此字符串包含`2`个`o`



## 示例三

### 输入

```
bcbcbc
```

### 输出

```
6
```

### 说明

这个示例中，字符串`bcbcbc`本身就是最长的，因为`o`出现了`0`次



## 解题思路

1. 如果o为偶数，那个就是整个字符串的长度
2. 如果o为基数，那么去掉一个o就是偶数个o，因为是环形串，所以整个长度减去去掉一个o即可。



## 解题代码

```python
def solve_method(s):
    n = len(s)
    # 统计o的个数，便于计算奇偶性
    cnt = s.count('o')
    # 偶数最长为整个s的长度，奇数则为去掉一个o的长度
    return n-1 if cnt%2 else n


if __name__ == '__main__':
    assert solve_method("alolobo") == 6
    assert solve_method("looxdolx") == 7
    assert solve_method("bcbcbc") == 6
    assert solve_method("olo") == 3

```



