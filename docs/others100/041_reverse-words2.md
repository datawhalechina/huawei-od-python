# 041 单词反转2

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
**说明**

翻转区间无效时不做翻转

## 解题思路

1. 读入一个字符串和两个整数`start`和`end`。
2. 如果`start > end`或`len(word) -1`或`end < 0`,则直接输出读入的字符串。
3. 否则，通过交换字符串中的`word`列表的元素来反转该字符串中的单词

## 解题代码

```python
def solve_method(line, start, end):
    words = line.split()
    # 检查索引是否有效，如果无效则直接打印原始行
    if 0 <= start < end < len(words):
        # 交换start和end之间的单词
        while start < end:
            words[start], words[end] = words[end], words[start]
            start += 1
            end -= 1
    print(" ".join(words))


def main():
    line = input().strip()
    start, end = map(int, input().strip().split())
    solve_method(line, start, end)


if __name__ == '__main__':
    main()
```

