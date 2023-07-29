# 040 单词反转

## 题目描述

给定一段英文文章片段，由若干单词组成，单词间以空格间隔，单词下标从0开始。
请翻转片段中指定区域的单词顺序并返回翻转后的内容。
例如给定的英文文章片段为 I am a developer ，
例如给定的英文文章片段为工是个开发人员，
翻转区间为[0,3] ，则输出developer a am I 。
String reversewords (String s, int start, int end) 。

## 输入描述

使用换行隔开三个参数，第一个参数为文章内容即英文字符串，
第二个参数为待翻转内容起始单词下标，下标从0开始，第三个参数为待翻转内容最后一个单词下标。

## 输出描述

翻转后的英文文章片段所有单词之间以一个半角空格分隔进行输出。


## 示例描述

### 示例一

**输入：**
```text
I am a developer
1
2
```

**输出：**
```text
I a am developer
```

### 示例二

**输入：**

```text
Hello world
-1
1
```

**输出：**

```text
world Hello
```
**说明：**

下标小于0时从第一个单词开始

### 示例三

**输入：**

```text
I am a developer
0
5
```

**输出：**

```text
developer a am I
```
**说明：**

下标大于实际单词个数 则按最大下标算

### 示例四

**输入：**

```text
I am a developer
-2
-1
```

**输出：**

```text
I am a developer
```
**说明：**

翻转区间无效时不做翻转。

## 解题思路

+ 读入一个字符串和两个整数start和end。
+ 如果start > end或start > len(words)- 1或 end<0，则直接输出读入的字符串。
+ 否则，通过交换字符串中 words 列表的元素来反转该字符串中的单词。


## 解题代码

```python
def solve_method(line, start, end):
    words = line.strip().split(" ")
    if start > end or start > len(line) -1 or end <0:
        return line.strip()
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

