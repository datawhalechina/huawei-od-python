# 131 最长合法表达式

## 题目描述

提前字符串中的最长合法简单数学表达式，获取字符串长度最长的表达式，并计算表达式的值。如果没有，则返回0。

简单数学表达式只能包含：`0-9`数字、符号`+-*/`。

说明：
1. 所有数字，计算结果都不会超过`long`类型的数值。
2. 如果有多个长度一样的，请返回第一个表达式的结果。
3. 数学表达式，必须是最长的、合法的。
4. 操作符不能连续出现，如`+==+1`是不合法的。

## 输入描述

输入为字符串。

## 输出描述

输出为简单数学表达式的值

## 示例描述

### 示例一

**输入：**
```text
1-2abcd
```

**输出：**
```text
-1
```

## 解题思路

1. 按字符遍历字符串
    - 确定满足简单数学表达式的连续字符。
    - 使用正则表达式，验证字符串是否为合法数学表达式。
2. 按照表达式长度进行排序。
3. 计算第一个表达式的结果。

## 解题代码

```python
import re


def check_valid(expression):
    p = re.compile("^([0-9]+([+\\-*/][0-9]+)+)$")
    return p.match(expression)


def solve_method(line):
    SAMPLE_OPS = "0123456789+-*/"

    nums = []
    for i in range(len(line)):
        if line[i].isdigit():
            start = i
            # 确定满足简单数学表达式的连续字符
            while i + 1 < len(line) and line[i + 1] in SAMPLE_OPS:
                i += 1

            expression = line[start: i + 1]
            # 验证字符串是否为合法数学表达式
            if check_valid(expression):
                nums.append(expression)

    # 按照表达式长度进行排序
    nums.sort(key=lambda x: len(x), reverse=True)
    if nums:
        # 计算表达式的值
        return eval(nums[0])
    else:
        return 0


if __name__ == '__main__':
    assert solve_method("1-2abcd") == -1
```