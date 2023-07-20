# 202 连续子串

## 题目描述

给定两个字符串`t`和`p`，要求从`t`中找到一个和`p`相同的连续子串，并输出该子串第一个字符的下标。

## 输入描述

输入包括两行，分别表示字符串`t`和`p`，保证`t`的长度不小于`p`，且`t`的长度不超过1000000，`p`的长度不超过10000。

## 输出描述

如果能从`t`中找到一个和`p`相等的连续子串，则输出该子串第一个字符串在`t`中的下标，下标从1开始。如果不能，则输出`No`，如果含有多个这样的子串，则输出第一个字符串下标最小的。

## 示例描述

### 示例一

**输入：**
```text
AVERDXIVYERDIAN
RDXI
```

**输出：**
```text
4
```

## 解题思路

**基本思路：** 用滑动窗口的思想，实现`str`的`find`方法。
1. 设置滑动窗口大小`window_length`为字符串`p`的长度。
2. 按字符串`t`的长度逐个遍历窗口：
    - 获取滑动窗口中的子串`substring`。
    - 判断子串`substring`是否与字符串`p`相等，如果相等，返回下标。
3. 如果找不到，返回`No`。

## 解题代码
```python
def solve_method(t, p):
    # 实现 t.find(p) + 1
    window_length = len(p)
    for i in range(len(t) - window_length + 1):
        substring = t[i:i + window_length]
        if substring == p:
            return i + 1

    return "No"


if __name__ == '__main__':
    assert solve_method("AVERDXIVYERDIAN", "RDXI") == 4
```