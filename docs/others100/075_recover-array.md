# 075 恢复数字序列

## 题目描述

对于一个连续正整数组成的序列，可以将其拼接成一个字符串，再将字符串里的部分字符打乱顺序。如序列`8 9 10 11 12`，拼接成的字符串为`89101112`，打乱一部分字符后得到`90811211`。注意打乱后原来的正整数可能被拆开，比如在`90811211`中，原来的正整数`10`就被拆成了`0`和`1`。

现给定一个按如上规则得到的打乱了字符的字符串，请将其还原成连续正整数序列，并输出序列中最小的数字。

## 输入描述

输入一行，为打乱字符的字符串和正整数序列的长度，两者间用空格分隔，字符串长度不超过200，正整数不超过1000，保证输入可以还原成唯一序列。

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

还原出的序列为`8 9 10 11 12`，故输出8。

### 示例二

**输入：**
```text
432111111111 5
```

**输出：**
```text
5
```

**说明：**

还原出的序列为`111 112 113 114`，故输出111。

## 解题思路

1. 将字符串构造成`Counter`类的字典，用于统计每个数字的个数。
2. 初始化`0~n`组成的字典，用于统计还原之后序列的每个数字的个数。
3. 遍历每个数字：
    - 如果两个字典相等，则返回序列中最小的数。
    - 如果不相等，则删除序列第一个数，添加该数字作为序列的最后一个数。
4. 如果无法还原序列，则返回-1。    

## 解题代码

```python
from collections import Counter


def solve_method(s, n):
    counter = Counter(s)
    candidate = [val for val in range(n)]
    candidate_counter = Counter(''.join(map(str, candidate)))
    for new in range(n, 1001):
        if candidate_counter == counter:
            return candidate[0]
        else:
            prev = candidate.pop(0)
            candidate_counter -= Counter(str(prev))

            candidate.append(new)
            candidate_counter += Counter(str(new))
    return -1


if __name__ == '__main__':
    assert solve_method("19801211", 5) == 8
    assert solve_method("432111111111", 4) == 111
```

