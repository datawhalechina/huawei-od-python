# 134 最长连续子串

## 题目描述

给定一个字符串，只包括字母和数字，按要求找出字符串中的最长连续子串的长度，字符串本身就是其最长的子串。

子串要求：
1. 只包含一个字母（a\~z、A\~Z），其余必须是数字
2. 字母可以在子串中的任意位置

如果找不到满足要求的子串，比如说，全是字母或数字，则返回-1

## 输入描述

字符串只包含字母和数字。

## 输出描述

符合要求的子串的长度。

## 示例描述

### 示例一

**输入：**
```text
abC124ACb
```

**输出：**
```text
4
```

**说明：**  
满足条件的最长子串是`C124`或者`124A`，长度都是4。

### 示例二

**输入：**
```text
a5
```

**输出：**
```text
2
```

**说明：**  
自身就是满足条件的子串，长度是2。

### 示例三

**输入：**
```text
aBB9
```

**输出：**
```text
2
```

**说明：**  
满足条件的子串为`B9`，长度是2。

### 示例四

**输入：**
```text
abcdef
```

**输出：**
```text
-1
```

**说明：**  
没有满足条件的子串，返回-1。

## 解题思路

**基本思路：** 使用双指针，逐个判断子串是否满足要求
1. 设置双指针`start`和`end`
2. 设置正则表达式，用来判断子串中是否只有一个字母
3. 循环获取子串
    - 使用正则表达式判断子串中是否只有一个字母。
    - 如果符合，则计算长度
    - 如果不符合，尾指针加1，扩大子串
4. 返回最大连续子串的长度。

## 解题代码

```python
import re


def solve_method(line):
    # 使用双指针
    start = 0
    end = 1
    max_length = -1
    # 设置正则表达式
    p = re.compile("[a-zA-Z]")
    while start < len(line) and end < len(line):
        end += 1
        sub_str = line[start:end]
        # 判断子串中是否只有一个字母
        if len(p.findall(sub_str)) == 1:
            max_length = max(max_length, len(sub_str))
        else:
            # 扩大范围
            start += 1

    return max_length


if __name__ == '__main__':
    assert solve_method("abC124ACb") == 4
    assert solve_method("a5") == 2
    assert solve_method("aBB9") == 2
    assert solve_method("abcdef") == -1
    assert solve_method("a12b234g1234") == 8
```