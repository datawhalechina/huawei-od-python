# 182 考古学家

## 题目描述

有一个考古学家发现一个石碑，但是很可惜发现时其已经断成多段，原地发现`N`个断口整齐的石碑碎片，为了破解石碑内容，考古学家希望有程序能帮忙计算复原后的石碑文字组合数，你能帮忙吗？

## 输入描述

第一行输入`N`，`N`表示石碑碎片的个数。

第二行依次输入石碑碎片上的文字内容`S`，共有`N`组。

## 输出描述

输出石碑文字的组合（按照升序排列一），行尾无多余空格。

## 示例描述

### 示例一

**输入：**
```text
3
a b c
```

**输出：**
```text
abc
acb
bac
bca
cab
cba
```

### 示例二

**输入：**
```text
3
a b a
```

**输出：**
```text
aab
aba
baa
```

### 示例三

**输入：**
```text
3
a b ab
```

**输出：**
```text
aabb
abab
abba
baab
baba
```

## 解题思路

1. 使用`itertools`包的`permutations`进行排列组合。
2. 将每个元素组合成字符串。
3. 将列表按照字典序排序。
4. 返回结果列表。

## 解题代码

```python
import itertools


def solve_method(fragments):
    fragments = list(itertools.permutations(fragments))
    fragments = list(set(["".join(i) for i in fragments]))
    fragments.sort()
    return fragments


if __name__ == '__main__':
    assert solve_method(["a", "b", "c"]) == ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert solve_method(["a", "b", "a"]) == ["aab", "aba", "baa"]
    assert solve_method(["a", "b", "ab"]) == ["aabb", "abab", "abba", "baab", "baba"]
```

