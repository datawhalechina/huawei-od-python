# 059 字母计数

## 题目描述

给出一个只包含字母的字符串，不包含空格，统计字符串中各个子字母（区分大小写）出现的次数，并按照字母出现次数从大到小的顺序，输出各个字母及其出现次数，如果次数相同，按照自然顺序排序，且小写字母在大写字母之前。

## 输入描述

输入一行仅包含字母的字符串。

## 输出描述

按照字母出现次数从大到小的顺序，输出各个字母和字母次数，用英文分号分隔，注意末尾的分号，字母和次数中间用英文冒号分隔。

## 示例描述

### 示例一

**输入：**

```text
xyxyXX
```

**输出：**

```text
x:2;y:2;X:2;
```

**说明：**

每个字符出现的次数为2，故`x`排在`y`之前，而小写字母`x`在大写字母`X`之前。

### 示例二

**输入：**

```text
abababb
```

**输出：**

```text
b:4;a:3;
```

**说明：**

`b`的出现个数比`a`多，故排在`a`前。

## 解题思路

1. 使用`Counter`建立字符频次字典`char_counter`，`key`为字符，`value`为出现次数。
2. 将字符频次字典按字母出现次数从大到小，如果相等，按照自然顺序排序，小写字母在前，大写字母在后
3. 得到每个字符及其出现次数，存入结果列表中。
4. 返回结果列表。

## 解题代码

```python
from collections import Counter


def solve_method(line):
    # 使用Counter计算每个字符的出现次数
    char_counter = Counter(line)

    # 按字母出现次数从大到小，如果相等，按照自然顺序排序，小写字母在前，大写字母在后
    char_count_pairs = sorted(char_counter.items(), key=lambda x: (-x[1], x[0].isupper()))

    
    result = ""
    for char, count in char_count_pairs:
        # 每个字符及其出现次数
        result += f"{char}:{count};"

    return result


if __name__ == "__main__":
    assert solve_method("xyxyXX") == "x:2;y:2;X:2;"
    assert solve_method("abababb") == "b:4;a:3;"
```



