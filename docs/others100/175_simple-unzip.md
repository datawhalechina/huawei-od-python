# 175 简易压缩算法

## 题目描述

有一种简易压缩算法：针对全部为小写英文字母组成的字符串，将其中连续超过两个相同字母的部分压缩为连续个数加该字母，其他部分保持原样不变，例如字符串`aaabbccccd`经过压缩变成字符串`3abb4cd`。

请您编写解压函数，根据输入的字符串：
- 判断其是否为合法压缩过的字符串。
- 若输入合法，则输出解压缩后的字符串。
- 否则输出字符串`!error`来报告错误。

## 输入描述

输入一行是一个ASCII字符串，长度不超过100个字符，用例保证输出的字符串长度也不会超过100个字符。

## 输出描述

若判断输入为合法的经过压缩后的字符串，则输出压缩前的字符串，若输入不合法，则输出字符串`!error`。

## 示例描述

### 示例一

**输入：**

```text
4dff
```

**输出：**

```text
ddddff
```

**说明：**

`4d`扩展为4个`d`，故解压后的字符串为`ddddff`。

### 示例二

**输入：**

```text
2dff
```

**输出：**

```text
!error
```

**说明：**

2个`d`不需要压缩，故输入不合法。

### 示例三

**输入：**

```text
4d@A
```

**输出：**

```text
!error
```

**说明：**

全部由小写英文字母做成的字符串，压缩后不会出现特殊字符`@`和大写字母`A`，故输入不合法。

## 解题思路

**基本思路：**

1. 检查字符串是否合法，判断是否是数字和小写字母，如果最后一个字符是数字，则不合法。
2. 遍历字符串中的所有字符：
   - 如果为数字，则加入到数字字符串中。
   - 如果为字母，并且数字字符串不为空：
        - 如果数字大于2，则进行解压操作，存入结果字符串中。
        - 如果数字小于等于2，则返回错误。
   - 如果为字母，则存入结果字符串。
3. 返回结果字符串。    

## 解题代码

```python
def solve_method(s):
    if s[-1].isdigit():
        return "!error"

    # 检查字符串是否合法，判断是否是数字和小写字母
    for i in s:
        if i.isdigit() or (i.isalpha() and i.islower()):
            continue
        else:
            return '!error'

    num_str = ""
    result = ""
    for ch in s:
        if ch.isdigit():
            # 如果为数字，则加入到数字字符串中
            num_str += ch
        elif num_str and ch.isalpha():
            # 如果为字母，并且数字字符串不为空
            if int(num_str) > 2:
                # 如果数字大于2，则进行解压操作，存入结果字符串中。
                result += ch * int(num_str)
                num_str = ""
            else:
                # 如果数字小于等于2，则返回错误
                return '!error'
        else:
            # 如果为字母，则存入结果字符串
            result += ch

    return result


if __name__ == '__main__':
    assert solve_method("4dff") == 'ddddff'
    assert solve_method("2dff") == '!error'
    assert solve_method("4d@A") == '!error'
```



