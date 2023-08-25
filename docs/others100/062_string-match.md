# 062 字符匹配

## 题目描述

给你一个字符串数组和一个字符规律：
- 字符串数组中每个字符串均由小写字母组成。
- 字符规律由小写字母以及`.`和`*`组成。

识别字符串数组中哪些字符串可以匹配到字符规律上。`.`匹配任意单个字符，`*`匹配0个或多个任意字符，判断字符串是否匹配，是要涵盖整个字符串的而不是部分字符串。

## 输入描述

第一行是空格分隔的多个字符串，取值范围是1 < 单个字符串长度 < 100、1 <= 字符串个数 < 100。
  
第二行为字符规律，取值范围是1 <= 字符规律长度 <= 50，不需要考虑异常场景。

## 输出描述

匹配的字符串在数组中的下标（从0开始）。多个匹配时，下标升序，并用`,`分隔，若均不匹配，则输出-1。

## 示例描述

### 示例一

**输入：**
```text
ab aab abacd
.*
```

**输出：**
```text
0,1,2
```

### 示例二

**输入：**
```text
ab aab
a.b
```

**输出：**
```text
1
```

## 解题思路
遍历字符串，如果当前字符与后一个字符相同，统计连续重复字符个数，如果不相同，
统计从下一个字符开始的子字符串中当前字符出现的次数。将字符与对应次数加入到排序列表中进行排序
   

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 062_string-match
@time:  14/8/2023 下午 11:39
@project:  huawei-od-python 
"""


def match_string(nums, pattern):
    def dfs(index1, index2, s, pattern, m, n):
        if index1 == m and index2 == n:
            return True
        elif index1 == m or index2 == n:
            return False
        if pattern[index2] == '.' or s[index1] == pattern[index2]:
            return dfs(index1 + 1, index2 + 1, s, pattern, m, n)
        elif pattern[index2] == '*':
            return dfs(index1 + 1, index2, s, pattern, m, n) or dfs(index1 + 1, index2 + 1, s, pattern, m, n)
        else:
            return False

    n = len(pattern)
    ans = []
    for i, s in enumerate(nums):
        m = len(s)
        if dfs(0, 0, s, pattern, m, n):
            ans.append(str(i))
    return ' '.join(ans)


if __name__ == '__main__':
    nums = input().strip().split(' ')
    pattern = input().strip()
    res = match_string(nums, pattern)
    print(res)


```

