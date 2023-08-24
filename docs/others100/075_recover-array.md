# 075 恢复数字序列

## 题目描述

对于一个连续正整数组成的序列，可以将其拼接成一个字符串，
再将字符串里的部分字符打乱顺序。如序列8 9 10 11 12，拼接成的字符串为89101112，
打乱一部分字符后得到90811211。注意打乱后原来的正整数可能被拆开，比如在90811211中，
原来的正整数10就被拆成了0和1。
现给定一个按如上规则得到的打乱了字符的字符串，请将其还原成连续正整数序列，并输出序列中最小的数字。

## 输入描述
输入一行，为打乱字符的字符串和正整数序列的长度，两者间用空格分隔，字符串长度不超过200，
正整数不超过1000，保证输入可以还原成唯一序列。


## 输出描述
输出一个数字，为序列中最小的数字。

## 示例描述

### 示例一

**输入：**
```text
19801211 5
```

**输出：**
```text
8
```
**说明：**

还原出的序列为8 9 10 11 12，故输出8

## 解题思路
滑动窗口，遍历所有n个连续数字组成的数组，统计字符出现次数是否与目标次数一致

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 075_recover-array
@time:  24/8/2023 下午 5:04
@project:  huawei-od-python 
"""
from collections import Counter


def is_same_dict(d1, d2):
    for key in d1:
        if key not in d2 or d1[key] != d2[key]:
            return False
    for key in d2:
        if key not in d1 or d1[key] != d2[key]:
            return False
    return True


def solve_method(s, n):
    counter = dict(Counter(s))
    candidate = [val for val in range(n)]
    candidate_counter = dict(Counter(''.join(map(str, candidate))))
    for new in range(n, 1001):
        if is_same_dict(candidate_counter, counter):
            return candidate[0]
        else:
            prev = candidate.pop(0)
            for key in str(prev):
                candidate_counter[key] -= 1
                if candidate_counter[key] == 0:
                    candidate_counter.pop(key)
                    
            candidate.append(new)
            for key in str(new):
                if key not in candidate_counter:
                    candidate_counter[key] = 1
                else:
                    candidate_counter[key] += 1
    return -1


if __name__ == '__main__':
    s, n = input().strip().split(' ')
    n = int(n)
    res = solve_method(s, n)
    print(res)


```

