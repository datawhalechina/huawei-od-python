# 044 压缩报文还原

## 题目描述

为了提升数据传输的效率，会对传输的报文进行压缩处理。输入一个压缩后的报文，请返回它解压后的原始报文。
压缩规则: `n[str]`，表示方括号内部的`str`正好重复`n`次。注意`n`为正整数，取值范围是0 < n <= 100，`str`只包含小写英文字母，不考虑异常情况。

**注：** 原始报文长度不会超过1000，不考虑异常的情况。

## 输入描述

输入压缩后的报文：
1. 不考虑无效的输入，报文没有额外的空格，方括号总是符合格式要求的。
2. 原始报文不包含数字，所有的数字只表示重复的次数`n`，例如不会出现像`5b`或`3[81`的输入。

## 输出描述

解压后的原始报文。

## 示例描述

### 示例一

**输入：**
```text
3[k]2[mn]
```

**输出：**
```text
kkkmnmn
```

### 示例二

**输入：**
```text
3[m2[c]]
```

**输出：**
```text
mccmccmcc
```

## 解题思路

**基本思路：** 使用堆栈方式解题。
1. 遍历字符串的每个元素：
    - 如果遇到一个数字，通过`isdigit()`函数来判断，则按照十进制数字进行组合。
    - 如果遇到一个字符时，将它添加到当前的字符串中。
    - 如果遇到'\['时，意味着这是一个新子字符串的开头，将当前的字符串和数字入栈，并将当前字符串重置为空字符串，数字重置为0。
    - 如果遇到'\]'时，意味着已经到达了子字符串的结束位置，在堆栈顶部弹出一个数字，然后与之前的字符串进行组合，并重复字符串。并将所有内容在计算后存储在当前字符串中。
2. 将当前字符串将作为结果返回。

## 解题代码

```python
def solve_method(string):
    prev, current = "", ""
    stack = []
    num = 0
    for i in range(len(string)):
        if string[i].isdigit():
            num = num * 10 + int(string[i])
        elif string[i] == "[":
            stack.append(current)
            stack.append(num)
            current = ""
            num = 0
        elif string[i] == "]":
            curr_num = stack.pop()
            prev = stack.pop()
            current = prev + curr_num * current
        else:
            current += string[i]

    return current


if __name__ == '__main__':
    assert solve_method("3[k]2[mn]") == "kkkmnmn"
    assert solve_method("3[m2[c]]") == "mccmccmcc"
```

