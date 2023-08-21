# 236 寻找相似单词

## 题目描述

给定一个可存储若干单词的字典，找出指定单词的所有相似单词，并且按照单词名称从小到大排序输出。单词仅包括字母，但可能大小写并存（大写不一定只出现在首字母）。相似单词说明：给定一个单词`X`，如果通过任意交换单词中字母的位置得到不同的单词`Y`，那么定义Y是X的相似单词，如`abc`、`bca`即为相似单词（大小写是不同的字母，如`a`和`A`算两个不同字母）。字典序排序： `大写字母 < 小写字母`。同样大小写的字母，遵循26字母顺序大小关系。即`A < B < C < ... < X < Y < Z < a < b < c < ... < x < y < z`. 如 `Bac < aBc < acB < cBa`.

## 输入描述

第一行为给定的单词个数 $N$（ $N$ 为非负整数）
从第二行到地 $N+1$ 行是具体的单词（每行一个单词）

最后一行是指定的待检测单词（用于检测上面给定的单词中哪些是与该指定单词是相似单词，该单词可以不是上面给定的单词）

## 输出描述

从给定的单词组中，找出指定单词的相似单词，并且按照从小到大字典序排列输出，中间以空格隔开

如果不存在，则输出`null`（字符串`null`）

## 示例描述

### 示例一

**输入：**
```
4
abc
dasd
tad
bca
abc
```

**输出：**
```
abc bca
```

**说明：**  
在给定的输入中，与`abc`是兄弟单词的是`abc` `bca`，且输出按照字典序大小排序，输出的所有单词以空格隔开

### 示例二

**输入：**
```
4
abc
dasd
tad
bca
abd
```

**输出：**
```
null
```

**说明：**  
给定单词组中，没有与给定单词`abd`是兄弟单词，输出为`null`（字符串`null`）

## 解题思路
**简单提示**
使用一个计数数组来计算每个字符在两个单词中出现的次数。单词长度不等一定不相似；如果所有字符的计数在两个单词中相等(一增一减相互抵消)，则这两个单词是相似的。

## 解题代码
``` python
def is_similar(word1, word2):
    if len(word1) != len(word2):
        return False

    count = [0] * 52
    for c1, c2 in zip(word1, word2):
        if 'A' <= c1 <= 'Z':
            count[ord(c1) - ord('A')] += 1
        else:
            count[ord(c1) - ord('a') + 26] += 1

        if 'A' <= c2 <= 'Z':
            count[ord(c2) - ord('A')] -= 1
        else:
            count[ord(c2) - ord('a') + 26] -= 1

    for c in count:
        if c != 0:
            return False

    return True

def solve_method(words, target_word):
    result = []
    for word in words:
        if is_similar(word, target_word):
            result.append(word)

    return result

if __name__ == '__main__':
    words = ["abc", "dasd", "tad", "bca"]
    assert solve_method(words, "abc") == ["abc", "bca"]

    assert solve_method(words, "abd") == []
```