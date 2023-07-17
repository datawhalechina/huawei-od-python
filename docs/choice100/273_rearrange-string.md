# 273 字符串重新排序

## 题目描述

给定一个字符串`s`，包含以空格分隔的若干个单词，请对`s`进行如下处理后输出：
1. 单词内部调整：对每个单词字母重新按字典序排序；
2. 单词间顺序调整：
    - 统计每个单词出现的次数，并按次数降序排列
    - 次数相同时，按单词长度升序排列
    - 次数和单词长度均相同时，按字典序升序排列

请输出处理后的字符串，每个单词以一个空格分隔。    

## 输入描述

一行字符串，每个字符取值范围：[a-zA-Z0-9]以及空格，字符串长度范围：[1, 1000]。

## 输出描述

重新排序后的字符串，每个单词间隔1个空格，且首尾无空格。

## 示例描述

### 示例一

**输入：**
```text
This is an apple
```

**输出：**
```text
an is This aelpp
```

### 示例二

**输入：**
```text
My sister is in the house not in the yard
```

**输出：**
```text
in in eht eht My is not adry ehosu eirsst
```

## 解题思路

1. 用空格分隔原始字符串，并用字典统计词频。
2. 使用`sorted`函数按次数降序、单词长度升序、按字典序升序排列。
3. 根据排序之后的字典，转换成字符串列表，注意单词需要按照词频进行重复记录。
4. 用`join`重新转成字符串并返回。

## 解题代码

```python
from collections import defaultdict


def solve_method(string):
    words = string.split()
    word_freqs = defaultdict(int)
    for word in words:
        rearrange_word = "".join(sorted(word))
        word_freqs[rearrange_word] += 1

    sorted_freqs = sorted(word_freqs.items(),
                          key=lambda x: (-x[1], len(x[0]), x[0]))

    result = []
    for (word, freqs) in sorted_freqs:
        result.extend([word] * freqs)

    result = " ".join(result)
    return result
```