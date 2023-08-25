# 063 密室逃生游戏

## 题目描述

小强在参加《密室逃生》游戏，当前关卡要求找到符合给定密码`K`（升序的不重复小写字母组成）的箱子，并给出箱子编号，箱子编号为1\~N。每个箱子中都有一个字符串`s`，字符串由大写字母、小写字母、数字、标点符号、空格组成，需要在这些字符串中找到所有的字母，忽略大小写后排列出对应的密码串，并返回匹配密码的箱子序号。其中，满足条件的箱子不超过1个。

## 输入描述

第一行是`key`的字符串。

第二行是箱子`boxes`数组，以逗号分隔箱子，数量`N`满足1 <= N <= 10000，箱子中字符串`s`的长度满足0 <= s.length <= 50。

密码为仅包含小写字母的升序字符串，且不存在重复字母，密码`K`长度`K.length`满足1 <= K.length <= 26。

## 输出描述

返回对应箱子编号，如不存在符合要求的密码箱，则返回-1。

## 示例描述

### 示例一

**输入：**
```text
abc
s,sdf134,A2c4b
```

**输出：**
```text
2
```
**说明：**

第2个箱子中的`Abc`，符合密码`abc`。

### 示例二

**输入：**
```text
abc
s,sdf134,A2c4bd,523[]
```

**输出：**
```text
-1
```

**说明：**

第2个箱子中的 Abcd，与密码不完全匹配，不符合要求。

**备注：**

箱子中字符拼出的字符串与密码的匹配忽略大小写，且要求与密码完全匹配，如密码 abc 匹配 aBc，
但是密码 abc 不匹配 abcd

## 解题思路
+ 将每个箱子的字符串剔除非字母字符并全部转换为小写，然后对字符串排序重构字符串。
+ 遍历所有箱子判断字符串是否相等

   

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 063_escape-room-game
@time:  17/8/2023 上午 10:48
@project:  huawei-od-python 
"""
from typing import List
import re


def solve_method(key: str, boxes: List[str]) -> int:
    pattern = r'[^a-zA-Z]+'
    boxes = [''.join(sorted(re.sub(pattern, '', s).lower())) for s in boxes]
    for index, s in enumerate(boxes):
        if s == key:
            return index
    return -1


if __name__ == '__main__':
    key = input().strip()
    boxes = input().strip().split(',')
    res = solve_method(key, boxes)
    print(res)



```

