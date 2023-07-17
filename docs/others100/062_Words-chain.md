# 062-单词接龙

## 题目描述

单词接龙的规则是：可用于接龙的单词，首字母必须要与前一个单词的尾字母相同；
当存在多个首字母相同的单词时，取长度最长的单词；
如果长度也相等，则取字典序最小的单词；
已经参与接龙的单词不能重复使用；
现给定一组全部由小写字母组成的单词数组，
并指定其中一个单词为起始单词，进行单词接龙，请输出最长的单词串。
单词串是单词拼接而成的，中间没有空格。
单词个数1<N<20，
单个单词的长度1~30

## 输入描述

输入第一行为一个非负整数，表示起始单词在数组中的索引k，0<=k<N。
输入的第二行为非负整数N，接下来的N行分别表示单词数组中的单词

## 输出描述

输出一个字符串表示最终拼接的单词串

## 示例描述

### 示例一

**输入：**
```
0
6
word
dd
da
dc
dword
d
```

**输出：**
```
worddwordda
```

### 示例二

**输入：**

```
4
6
word
dd
da
dc
dword
d
```

**输出：**

```
dwordda
```

## 解题思路

该机试题的解题思路是:使用排序和字符串拼接一的方法，对给定的字符串列表进行操作，
从给定的字符串列表中选择一个元素(索引为k的元素)，将它添加至
builder字符串中，然后从列表中删除该元素。
然后，使用sorted函数对字符串列表进行排序，关键字使用lambda表达式定义，该表达式按长度倒序排序，
如果长度相同，则按字典顺序排序。

```python
def wordsChain(words, k):
    builder = words[k]
    del words[k]
    words = sorted(words, key=lambda x: (-len(x), x))
    flag, index = True, 0
    while words and index < len(words):
        if words[index].startswith(builder[-1]):
            builder += words[index]
            del words[index]
            index = 0
        else:
            index += 1
    return builder


if __name__ == '__main__':
    k = int(input("请输入起始单词索引："))
    N = int(input("请输单词数组长度："))
    words = []
    for _ in range(N):
        words.append(input().strip())
    res = wordsChain(words, k)
    print(res)

```

