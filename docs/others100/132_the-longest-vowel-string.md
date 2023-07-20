# 132 最长的元音字符串

## 题目描述

定义当一个字符串只有元音字母（a、e、i、o、u、A、E、I、O、U）组成，称为元音字符串。现给定一个字符串，请找出其中最长的元音字符串，并返回其长度，如果找不到，请返回0。

注：字符串中任意一个连续字符串组成的子序列成为该字符串的子串。

## 输入描述

一个字符串，长度`length > 0`，字符串仅由字符a-z或A-Z组成。

## 输出描述

一个整数，表示最长的元音字符子串的长度

## 示例描述

### 示例一

**输入：**
```text
asdbuiodevauufgh
```

**输出：**
```text
3
```

**说明：**  
最长的元音字符子串为`uio`和`auu`，长度都为3，因此输出3。

## 解题思路

1. 设置正则表达式`[aeiouAEIOU]+`。
2. 使用`findall`方法，找到所有符合正则的字符串。
3. 按照字符串长度从大到小排序。
4. 如果找到了，返回第一个字符串的长度，即为最长的元音字符串，如果没有找到，返回0。

## 解题代码

```python
import re


def solve_method(string):
    p = re.compile("[aeiouAEIOU]+")
    result = p.findall(string)
    result.sort(key=lambda x: len(x), reverse=True)
    return len(result[0]) if len(result) != 0 else 0


if __name__ == '__main__':
    assert solve_method("asdbuiodevauufgh") == 3
    assert solve_method("fgh") == 0
```