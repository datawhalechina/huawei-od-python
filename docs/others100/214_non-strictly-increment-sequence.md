# 214 非严格递增连续数字序列

## 题目描述

输入一个字符串，仅包含大小写字母和数字。求字符串中包含的最长的非严格递增连续数字序列长度。

比如：12234，属于非严格递增数字序列。

## 输入描述

输入一个字符串，仅包含大小写字母和数字。

## 输出描述

输出字符串中包含的最长的非严格递增连续数字序列长度。

## 示例描述

### 示例一

**输入：**
```text
abc2234019A334bc
```

**输出：**
```text
4
```

**说明：**  
`2234`为最长的非严格递增连续数字序列，所有长度为4。

## 解题思路

1. 初始化前一个数字`pre_num`。
2. 遍历字符串：
   - 如果是数字：
        - 如果当前数字大于等于前一个数字，则继续保持非严格递增。
        - 如果没有，则长度回到1。
        - 保存前一个数字。
   - 如果不是数字，则直接保存当前长度。 
3. 返回非严格递增连续数字序列的最大长度。

## 解题代码

```python
import math


def solve_method(string):
    # 设置前一个数字
    pre_num = math.inf
    # 满足条件的最大长度
    max_len = 0
    cur_len = 0
    for ch in string:
        if ch.isdigit():
            ch = int(ch)
            # 如果当前数字大于等于前一个数字，则继续保持非严格递增
            if cur_len == 0 or ch >= pre_num:
                cur_len += 1
            else:
                # 如果没有，则长度回到1
                max_len = max(max_len, cur_len)
                cur_len = 1
            # 保存前一个数字
            pre_num = ch
        else:
            # 如果不是数字，则直接保存当前长度
            max_len = max(max_len, cur_len)
            cur_len = 0
            pre_num = math.inf

    return max(cur_len, max_len)


if __name__ == '__main__':
    assert solve_method("abc2234019A334bc") == 4
```