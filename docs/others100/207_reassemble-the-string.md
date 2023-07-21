# 207 重组字符串

## 题目描述

给定一个非空字符串`S`，其被`N`个`-`分隔成`N+1`个字符串，给定正整数`K`，要求除第一个子串外，其余的子串每`K`个字符组成新的子串，并用`-`分隔。对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；当大小写字母的数量相等时，不做转换。

## 输入描述

输入为两行，第1行为参数`K`，第二行为字符串`S`。

## 输出描述

输出转换后的字符串。

## 示例描述

### 示例一

**输入：**
```text
3
12abc-abCABc-4aB@
```

**输出：**
```text
12abc-abc-ABC-4aB-@
```

## 解题思路

**基本思路：**
1. 用`-`分隔输入的字符串。
2. 将第一个子串直接转换并保存结果列表中。
3. 使用`while`循环，遍历新字符串：   
    - 每隔k个字符组成新的子串。
    - 对子串进行转换，保存到结果列表中。
4. 转换方法：用正则表达式匹配大写和小写字母，然后比较个数：
    - 如果大写字母比小写字母个数多，转换为大写字母。
    - 如果小写字母比大写字母个数多，转换为小写字母。
    - 如果一样多，不做转换。
5. 用`-`拼接，返回结果列表。

## 解题代码
```python
import re


def convert(substring):
    upper = re.compile("[A-Z]")
    lower = re.compile("[a-z]")

    upper_count = len(upper.findall(substring))
    lower_count = len(lower.findall(substring))
    if lower_count > upper_count:
        return substring.lower()
    elif upper_count > lower_count:
        return substring.upper()

    return substring


def solve_method(k, line):
    strings = line.split("-")
    # 第一个子串直接转换并保存
    result = [convert(strings[0])]
    strings = "".join(strings[1:])
    # 每隔k个字符组成新的子串
    while len(strings):
        if len(strings) >= k:
            # 对子串进行转换
            result.append(convert(strings[:k]))
            strings = strings[k:]
        else:
            result.append(convert(strings))
            strings = ""
    # 用-拼接
    return "-".join(result)


if __name__ == '__main__':
    assert solve_method(3, "12abc-abCABc-4aB@") == "12abc-abc-ABC-4aB-@"
```
