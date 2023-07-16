# 060-单词反转

## 题目描述

输入一个英文文章片段，翻转指定区域的单词顺序，标点符号和普通字母一样处理

## 输入描述

使用换行隔开3个参数，第一个参数为文章内容即英文字符串，第二个参数为翻转起始单词下标，下标从0开始，第三个参数为结束单词下标

## 输出描述

翻转后英文文章片段每个单词之间以一个半角空格分割输出

## 示例描述

### 示例一

**输入：**
```
I am a developer.
0
3
```

**输出：**
```
developer. a am I
```

### 示例二

**输入：**

```
hello world!
0
3
```

**输出：**

```
world! hello
```

## 解题思路

该题的目标是编写一个字符串反转一的功能。

+ 通过input()函数读入字符串line和两个整数I和r。
+ 使用split() 函数将字符串line按照空格分割成一个字符串数组 words
+ 对于字符串数组words，如果r 大于数组长度减1，则将r的值设为数组长度减1。如果字符串数组长度为0，或者l小于0，或者r-1小于等于0，则输出“EMPTY”并退出函数。

```python
def reverseWords(line, l, r):
    words = line.strip().split(" ")
    end = len(words) - 1
    if r > end:
        r = end
    if len(words) == 0 or l < 0 or r - l <= 0:
        print('EMPTY')
        return
    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1
    print(' '.join(words))


if __name__ == '__main__':
    line = input("请输入文章片段：")
    l = input("请输入左边界：")
    r = input("请输入右边界：")
    l, r = int(l), int(r)
    reverseWords(line, l, r)

```

