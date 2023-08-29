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

**基本思路：**

1. 使用Counter函数对每个字符进行计数，生成新对象字典cnt，每个字典key为字母，value为出现次数。

2. 对cnt进行排序，先按照value出现次数从打大小排序，在按照字母在原字符串s中的循序排序。
3. 最后进行拼接

## 解题代码

```python
from collections import Counter


def solve_method(line: str) -> None:
    # 使用Counter计算每个字符的出现次数
    char_counter = Counter(line)

    # 对字符进行排序，首先按出现次数降序，然后按ASCII值升序
    char_count_pairs = sorted(char_counter.items(), key=lambda item: (-item[1], item[0]))

    # 打印每个字符及其出现次数
    for char, count in char_count_pairs:
        print(f"{char}:{count};", end="")
    print()


def main() -> None:
    line = input().strip()  # 读取输入的字符串
    solve_method(line)  # 调用solve_method处理字符串


if __name__ == "__main__":
    main()  # 如果是主程序，则调用main函数
```



