# 142 查字典

## 题目描述

输入一个单词前缀和一个字典，输出包含该前缀的单词。

## 输入描述

输入是单词前缀+字典长度+字典内容，每项内容间以空格分隔。字典是一个有序单词数组。输入输出都是小写英文字母。

## 输出描述

所有包含该前缀的单词；如果有多个单词，则每个单词换行输出；如果没有任何单词，输出-1。

## 示例描述

### 示例一

**输入：**

```text
b 3 a b c
```

**输出：**

```text
b
```

**说明：**  

单词前缀是`b`，字典里只有第二个单词`b`与之对应，所以输出。

### 示例二

**输入：**

```text
abc 4 a ab abc abcd
```

**输出：**

```text
abc
abcd
```

**说明：**  

前缀是`abc`，字典本身是有序的单词数组, `abc`和之后的`abcd`都有前缀`abc`，故输出。

### 示例三

**输入：**

```text
a 3 b c d
```

**输出：**

```text
-1
```

## 解题思路

**基本思路：** 

1. 初始化结果列表`result`，存储与前缀相匹配的单词。
2. 遍历单词字典：
   - 判断字符串的前缀是否与给定的前缀相同，如果相同，将该字符串添加到结果列表。
3. 返回结果列表，如果结果列表为空，则返回-1。    

## 解题代码

```python
from typing import List


def solve_method(prefix: str, length: int, words: List[str]):
    # 空列表results，存储与前缀相匹配的单词
    results = []

    for word in words:
        # 判断字符串的前缀是否与给定的前缀相同，如果相同，将该字符串添加到results列表中
        if word.startswith(prefix):
            results.append(word)

    return results if results else -1


if __name__ == '__main__':
    assert solve_method("b", 3, ["a", "b", "c"]) == ["b"]
    assert solve_method("abc", 4, ["a", "ab", "abc", "abcd"]) == ["abc", "abcd"]
    assert solve_method("a", 3, ["b", "c", "d"]) == -1
```