# 035 删除最少的字符

## 题目描述

删除字符串中出现次数最少的字符，如果多个字符出现次数一样则都删除。

## 输入描述

输入只包含小写字母。

## 输出描述

输出删除后剩余的字符，若删除后字符串长度为0，则输出`empty`。

## 示例描述

### 示例一

**输入：**

```text
abcdd
```

**输出：**

```text
dd
```

### 示例二

**输入：**

```text
aabbccdd
```

**输出：**

```text
empty
```

## 解题思路

**基本思路：** 

1. 用`collections`中的`Counter`统计字符串中每个字符出现的频率，用`min()`求出最小值`min_freq`。
2. 逐个字符进行判断，如果不等于`min_freq`，存于结果列表`result`中。
3. 如果结果列表为空，则返回`empty`，不为空，则返回结果列表。

## 解题代码

```Python
from collections import Counter


def solve_method(chars):
    # 统计字符频率
    freq = Counter(chars)
    # 求最小值
    min_freq = min(freq.values())
    result = ""
    for c in chars:
        if freq[c] != min_freq:
            result += c
    if len(result) == 0:
        return 'empty'
    return result


if __name__ == '__main__':
    assert solve_method("abcdd") == "dd"
    assert solve_method("aabbccdd") == "empty"
```

