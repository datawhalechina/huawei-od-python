# 015 交换字符

## 题目描述

给定一个字符串`S`，将字符串进行变换，变化规则是交换字符串中任意两个不同位置的字符`M`，其中`S`都是由小写字符组成，字符串的长度范围是`1 <= S.length <= 1000`。

## 输入描述

一串小写字母组成的字符串。

## 输出描述

按照要求变换得到最小字符串。

## 示例描述

### 示例一

**输入：**
```text
abcdef
```

**输出：**
```text
abcdef
```

### 示例二

**输入：**

```text
bcdefa
```

**输出：**

```text
acdefb
```

## 解题思路

1. 初始化最小的字符`min_char`、字符对应的位置`pos`。
2. 遍历字符串：获取按字典序最小的字符，并得到对应的位置。
3. 将最小的字符与第一个字符进行交换。
4. 返回结果字符串。

## 解题代码

```python
def solve_method(string):
    string = list(string)
    pos = 0
    min_char = string[0]
    for i in range(1, len(string)):
        char = string[i]
        if char <= min_char:
            min_char, pos = char, i

    if pos != 0:
        string[pos], string[0] = string[0], min_char

    return "".join(string)


if __name__ == '__main__':
    assert solve_method("abcdef") == "abcdef"
    assert solve_method("bcdefa") == "acdefb"
```

