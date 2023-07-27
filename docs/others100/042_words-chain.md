# 042 单词接龙

## 题目描述

单词接龙的规则是：
- 可用于接龙的单词，首字母必须要与前一个单词的尾字母相同。
- 当存在多个首字母相同的单词时，取长度最长的单词。
- 如果长度也相等，则取字典序最小的单词。
- 已经参与接龙的单词不能重复使用。

现给定一组全部由小写字母组成的单词数组，并指定其中一个单词为起始单词，进行单词接龙，请输出最长的单词串。

单词串是单词拼接而成的，中间没有空格。单词个数1 < N < 20，单个单词的长度1\~30。

## 输入描述

输入第一行是一个非负整数，表示起始单词在数组中的索引`k`，取值范围是0 <= k < N。
输入的第二行为非负整数`N`，接下来的`N`行分别表示单词数组中的单词。

## 输出描述

输出一个字符串表示最终拼接的单词串。

## 示例描述

### 示例一

**输入：**
```text
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
```text
worddwordda
```

### 示例二

**输入：**

```text
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

```text
dwordda
```

## 解题思路

1. 根据索引`k`获取起始单词，存入结果字符串中。
2. 排除起始单词，对字符串数组按长度从大到小、字典序从小到大排序。
3. 遍历字符串数组：
    - 判断是否为前一个单词的尾字母：
        - 如果符合，则添加到结果字符串中，并将遍历索引重置为0。
        - 如果不符合，则继续遍历字符串数组。
4. 返回结果字符串。    

## 解题代码

```python
def solve_method(words, k):
    result = words[k]
    words.pop(k)
    words = sorted(words, key=lambda x: (-len(x), x))
    index = 0
    while words and index < len(words):
        # 判断是否为前一个单词的尾字母
        if words[index].startswith(result[-1]):
            result += words[index]
            words.pop(index)
            # 遍历的时候，确保从第一个单词开始遍历
            index = 0
        else:
            # 继续遍历
            index += 1
    return result


if __name__ == '__main__':
    words = ["word", "dd", "da", "dc", "dword", "d"]
    assert solve_method(words, 0) == "worddwordda"

    words = ["word", "dd", "da", "dc", "dword", "d"]
    assert solve_method(words, 4) == "dwordda"
```

