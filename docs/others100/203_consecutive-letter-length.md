# 203 连续字母长度、求第K长的字符串长度

## 题目描述

给定一个字符串，只包含大写字母，求在包含同一个字母的子串中，长度第`k`长的子串的长度，相同字母只取最长的那个子串。

## 输入描述

第1行是一个子串（1 < 子串长度 <= 100），只包含大写字母。

第2行是`k`的值。

## 输出描述

输出连续出现次数排序中，第`k`多的字母的次数。

## 示例描述

### 示例一

**输入：**
```text
AAAAHHHBBCDHHHH
3
```

**输出：**
```text
2
```

**说明：**  
同一字母连续出现的最多次数的是`A`和`H`，有4次；第2多的是`H`，有3次；但是已经存在4个连续的，故不考虑；下个最长子串的是`BB`，所以最终答案应该是2。

### 示例二

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
同一字母连续出现的最多次数的是`A`，有3次；第2多的是`A`，有2次；但是已经存在最大连续次数3次，故不考虑；下个最长子串的是`B`，所以最终答案应该是1。

### 示例三

**输入：**
```text
ABC
4
```

**输出：**
```text
-1
```

**说明：**  
只含有3个包含同一个字母的子串，小于k，则输出-1。

## 解题思路

1. 初始化字母字典`ch_freq`，key为字母，value为同一字母连续出现的最大次数。
2. 遍历字符串：
    - 如果字母连续出现，记录出现次数。
    - 如果不是同一个字母，则将字母和连续出现的最大次数保存到字母字典`ch_freq`中。
3. 将字母字典`ch_freq`的`value`值按照出现次数排序。    
4. 返回第k个字母的连续出现的次数。

## 解题代码

```python
from collections import defaultdict


def solve_method(strings, k):
    pre_char = strings[0]
    # 字符字典，key为字母，value为同一字母连续出现的最大次数
    ch_freq = defaultdict(int)

    count = 0
    for ch in strings:
        if pre_char == ch:
            count += 1
        else:
            if pre_char in ch_freq:
                ch_freq[pre_char] = max(ch_freq[pre_char], count)
            else:
                ch_freq[pre_char] = count
            pre_char = ch
            count = 1
    
    # 按照出现次数排序
    ch_list = sorted(ch_freq.values(), reverse=True)
    if k > len(ch_list):
        return -1
    else:
        # 取出第k个字母的连续出现的次数
        return ch_list[k - 1]


if __name__ == '__main__':
    assert solve_method("AAAAHHHBBCDHHHH", 3) == 2
    assert solve_method("AABAAA", 2) == 1
    assert solve_method("ABC", 4) == -1
```