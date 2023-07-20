# 061-单词反转2

## 题目描述

给定一段英文文章片段，由若干单词组成，单词间以空格间隔，单词下标从0开始。请翻转片段中指定区域的单词顺序并返回翻转后的内容。例如给定的英文文章片段为I am a developer， 
翻转区间为[0,3]，则输出developer a am I 。



## 输入描述

使用换行隔开3个参数，第一个参数为文章内容即英文字符串，第二个参数为翻转起始单词下标，下标从0开始，第三个参数为结束单词下标

## 输出描述

翻转后英文文章片段每个单词之间以一个半角空格分割输出

## 示例描述

### 示例一

**输入：**
```
I am a developer
1
2
```

**输出：**
```
I a am developer
```

### 示例二

**输入：**

```
hello world
-1
1
```

**输出：**

```
world hello
```

### 示例三

**输入：**

```
I a am developer
0
5
```

**输出：**

```
developer am a I
```
**说明**

下标大于实际单词个数则按最大下标算
### 示例四

**输入：**

```
I a am developer
-2
-1
```

**输出：**

```
I a am developer
```
**说明**

翻转区间无效时不做翻转
## 解题思路

该题的目标是编写一个字符串反转一的功能。

+ 读入一个字符串和两个整数start和end。
+ 如果 start > end 或 start > len(words) - 1 或 end < 0，则直接输出读入的字符串。否则，通过交换字符串中words列表的元素来反转该字符串中的单词

```python
def reverseWords(line, l, r):
    words = line.strip().split(" ")
    end = len(words) - 1
    if len(words) == 0 or l > r or l>end or r<0:
        print(line.strip())
        return
    l = max(0,l)
    r = min(end,r)
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

