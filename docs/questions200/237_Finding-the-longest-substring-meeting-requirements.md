# 237 寻找符合要求的最长子串

## 题目描述
给定一个字符串 `s` ，找出这样一个子串：

1. 该子串中的任意一个字符最多出现 2 次；
2. 该子串不包含指定某个字符；

请你找出满足该条件的最长子串的长度。
## 输入描述
第一行为要求不包含的指定字符，为单个字符，取值范围 `[0-9a-zA-Z]` 
第二行为字符串 s，每个字符范围 `[0-9a-zA-Z]`，长度范围 `[1,10000]`

## 输出描述
一个整数，满足条件的最长子串的长度；
如果不存在满足条件的子串，则返回 `0`

## 示例描述

### 示例一

**输入：**
```
D
ABC123
```

**输出：**
```
6
```

## 解题思路
使用滑动窗口的思想, 按照要求遍历字符串并计算符合要求的最长子串

## 解题代码
``` python
def solve_method(c, s):
    l = 0
    result = 0
    d = {}

    for i in range(len(s)):
        temp = s[i]
        if temp == c:
            d.clear()
            l = i + 1
            continue

        # 记录当前字符的出现次数
        d[temp] = d.get(temp, 0) + 1

        # 当前字符出现次数超出2次, 找到第一个出现的位置的下一个位置作为起点l
        while d[temp] == 3:
            rmChar = s[l]
            l += 1
            d[rmChar] -= 1

        # 更新结果, 记录符合条件的子串长度的最大值
        result = max(result, i - l + 1)

    return result

if __name__ == '__main__':
    assert solve_method('D',"ABC123") == 6
    assert solve_method('D',"ABACD1231") == 4
```