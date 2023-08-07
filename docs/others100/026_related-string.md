# 026 关联字串

## 题目描述

给定两个字符串`str1`和`str2`，如果字符串`str1`中的字符，经过排列组合后的字符串中只要有一个是`str2`的子串，则认为`str1`是`str2`的关联子串 ，若不是关联子串则返回-1。

预制条件:
1. 输入的字符串只包含小写字母。
2. 两个字符串的长度范围1\~100000。
3. 若`str2`中有多个`str1`的组合子串，请返回第一个子串的起始位置。

## 输入描述

输入两个字符串，分别为题目中描述的`str1`和`str2`。

## 输出描述

如果`str1`是`str2`的关联子串，则返回子串在`str2`中的起始位置，如果不是则返回-1。

若`str2`中有多个`str1`的组合子串，请返回最小的起始位置。

## 示例描述

### 示例一

**输入：**

```text
abc efghicabiii
```

**输出：**

```text
5
```

**说明：**

`str2`包含`str1`的一种排列组合是`cab`，其在`str2`的起始位置为5（从0开始计数）。

### 示例二

**输入：**

```text
abc  efghicaibii
```

**输出：**

```text
-1
```

**说明：**

`abc`字符串中三个字母的各种组合（`abc`、`acb`、`bac`、`bca`、`cab`、`cba`），`str2`中均不包含，因此返回-1。

## 解题思路

**基本思路：** 使用滑动窗口求解。

1. 初始化滑动窗口的长度，为字符串`str1`的长度。
2. 遍历`str2`中在窗口长度中的子串：
   - 如果子串的`Counter`类与`str1`构建的`Counter`类相等，将该位置作为结果返回。
3. 如果全部遍历完，都没有找到，则返回-1。    

## 解题代码

```Python
from collections import Counter


def solve_method(str1, str2):
    length = len(str1)
    for i in range(len(str2) - length + 1):
        sub_str = list(str2[i:i + length])
        if Counter(sub_str) == Counter(str1):
            return i
    return -1


if __name__ == '__main__':
    assert solve_method("abc", "efghicabiii") == 5
    assert solve_method("abc", "efghicaibii") == -1
```

