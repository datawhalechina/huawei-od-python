# 040 单词反转

## 题目描述

输入一个英文文章片段，翻转指定区域的单词顺序，标点符号和普通字母一样处理。

## 输入描述

使用换行隔开3个参数，第一个参数为文章内容即英文字符串，第二个参数为翻转起始单词下标，下标从0开始，第三个参数为结束单词下标。

## 输出描述

翻转后英文文章片段每个单词之间以一个半角空格分隔输出。

## 示例描述

### 示例一

**输入：**
```text
I am a developer.
0
3
```

**输出：**
```text
developer. a am I
```

### 示例二

**输入：**

```text
hello world!
0
3
```

**输出：**

```text
world! hello
```

## 解题思路

1. 对字符串进行空格分隔，形成字符串数组`words`。
2. 提取区域内的字符串并反转。
3. 合并字符串数组并返回结果。

## 解题代码

```python
def solve_method(line, start, end):
    words = line.strip().split(" ")
    if end > len(words) - 1:
        end = len(words) - 1
    if len(words) == 0 or start < 0 or end <= start:
        return line

    # 提取区域内的字符串并反转
    sub_words = words[start:end + 1]
    sub_words.reverse()
    # 合并字符串数组并输出
    if end + 1 < len(words):
        result = words[:start] + sub_words + words[end + 1:]
    else:
        result = words[:start] + sub_words

    return " ".join(result)


if __name__ == '__main__':
    assert solve_method("I am a developer.", 0, 3) == "developer. a am I"
    assert solve_method("hello world!", 0, 3) == "world! hello"
    assert solve_method("I am a developer", 1, 2) == "I a am developer"
    assert solve_method("hello world", -1, 1) == "hello world"
```

