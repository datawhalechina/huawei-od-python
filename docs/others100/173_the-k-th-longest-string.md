# 173 第k长子串

## 题目描述

给定一个字符串只包含大写字母，求在包含同一字母的子串中，长度第`k`长的子串，相同字母只取最长的子串。

## 输入描述

第一行是一个子串，子串长度是1 < len <= 100，只包含大写字母。

第二行是`k`的值。

## 输出描述

输出连续出现次数第`k`多的字母的次数，如果子串中只包含同一字母的子串数小于`k`，则输出-1。

## 示例描述

### 示例一

**输入：**

```text
AABAAA
2
```

**输出：**

```text
1
```

**说明：**

同一字母连续出现最多的`A`，一共有3次，第二多也是A，有2次，但A出现连续3次，只保留最高的，那么第二多为字母`B`，有1次。

### 示例二

**输入：**

```text
AAAAHHHBBCDHHHH
3
```

**输出：**

```text
2
```

## 解题思路

1. 初始化字符频次字典`dic_len`，`key`为字符，`value`为连续字母的最大出现次数。
2. 遍历字符串中的所有字符：
   - 如果与前一个字母相同，则加入到单词列表中。
   - 如果与前一个字母不同，则更新前一个连续字符的最大出现次数，保存当前字符串，更新单词列表。 
3. 将字符频次字典按照字符出现次数从大到小进行排序。
4. 返回连续出现次数第`k`多的字母的次数，不存在则返回-1。

## 解题代码

```python
from collections import defaultdict


def solve_method(s, k):
    # 字符频次字典，key为字符，value为连续字母的最大出现次数
    dic_len = defaultdict(int)

    pre_ch = s[0]
    word = []
    for ch in s:
        if ch == pre_ch:
            # 如果与前一个字母相同，则加入到单词列表中
            word.append(ch)
        else:
            # 如果与前一个字母不同，则更新前一个连续字符的最大出现次数
            dic_len[pre_ch] = max(dic_len[pre_ch], len(word))
            # 保存当前字符串
            pre_ch = ch
            # 更新单词列表
            word = [ch]

    if word and pre_ch:
        dic_len[pre_ch] = max(dic_len[pre_ch], len(word))

    # 将字符频次字典按照字符出现次数从大到小进行排序
    tuple_len = sorted(dic_len.items(), key=lambda x: -x[1])
    # 子串数小于k，找不到返回-1
    if k - 1 >= len(tuple_len):
        return -1
    else:
        return tuple_len[k - 1][1]


if __name__ == '__main__':
    assert solve_method("AABAAA", 2) == 1
    assert solve_method("AAAAHHHBBCDHHHH", 3) == 2
```



