# 061 字符串摘要

## 题目描述

给定一个字符串的摘要算法，请输出给定字符串的摘要值。
1. 去除字符串中非字母的符号。
2. 如果出现连续字符(不区分大小写)，则输出: 该字符(小写) + 连续出现的次数。
3. 如果是非连续的字符(不区分大小写)，则输出: 该字符(小写) ＋ 该字母之后字符串中出现的该字符的次数。
4. 对按照以上方式表示后的字符串进行排序: 字母和紧随的数字作为一组进行排序，
数字大的在前，数字相同的，则按字母进行排序，字母小的在前。


## 输入描述

一行字符串，长度为[1,200]



## 输出描述
摘要字符串

## 示例描述

### 示例一

**输入：**
```text
aabbcc
```

**输出：**
```text
a2b2c2
```

### 示例二

**输入：**
```text
bAaAcBb
```

**输出：**
```text
a3b2b2c0
```
**说明：**

bAaAcBb:

第一个b非连续字母，该字母之后字符串中还出现了2次(最后的两个bb)，所以输出b2，
a连续出现3次，输出a3，
c非连续，该字母之后字符串再没有出现过c，输出c0，
Bb连续2次，输出b2，
对b2a3c0b2进行排序，最终输出a3b2b2c0

## 解题思路
遍历字符串，如果当前字符与后一个字符相同，统计连续重复字符个数，如果不相同，
统计从下一个字符开始的子字符串中当前字符出现的次数。将字符与对应次数加入到排序列表中进行排序
   

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 061_string-abstract
@time:  13/8/2023 下午 5:45
@project:  huawei-od-python 
"""
import re

pattern = r"[^a-zA-Z]+"


def solve_method(s):
    n = len(s)
    index = 0
    item_list = []
    s = re.sub(pattern, '', s)
    s = s.lower()

    def count(s, c, start, end):
        ans = 0
        for i in range(start, end):
            if s[i] == c:
                ans += 1
        return ans

    while index < n:
        if index == n - 1:
            item_list.append(f'{s[index]}0')
        if s[index] == s[index + 1]:
            start, index = index, index + 1
            while index < n - 1 and s[index] == s[index + 1]:
                index += 1
            freq = index - start + 1
            item_list.append(f'{s[start]}{freq}')
            index += 1
        else:
            freq = count(s, s[index], index + 1, n)
            item_list.append(f'{s[index]}{freq}')
            index += 1
    item_list.sort(key=lambda x: (-int(x[1]), ord(x[0])))
    return ''.join(item_list)


if __name__ == '__main__':
    s = input()
    res = solve_method(s)
    print(res)

```

