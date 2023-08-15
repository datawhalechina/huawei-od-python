# 148 求字符串中所有整数的最小和

## 题目描述

1. 输入一个字符串`s`，它只包含`a-z`、`A-Z`、`+`、`-`以及合法的整数
2. 合法的整数包括：
- 正整数由一个或者多个0-9组成，如0、2、3、002、102。
- 负整数以负号`-`开头，数字部分由一个或者多个0-9组成，如-0、-1、-123、-12345。

## 输入描述

包含数字的字符串。

## 输出描述

字符串中所有合法整数的最小和。

## 示例描述

### 示例一

**输入：**

```text
bb1234aa
```

**输出：**

```text
10
```

**说明：**  

1+2+3+4=10

### 示例二

**输入：**

```text
bb12-34aa
```

**输出：**

```text
-31
```

**说明：**  

1+2+(-34)=-31 

## 解题思路

1. 检查输入的字符串是否合法。
2. 初始化整数和`sum_val`。   
3. 遍历字符串中的每一个字符：
  - 如果是`-`，则一直往后读取数字，直到遇到非数字字符，将`sum_val`减去该数字。
  - 如果是单一数字，则直接加上这个数字。
4. 返回整数和的值。

## 解题代码

```python
def solve_method(string: str) -> int:
    # 检查输入是否有效
    Legal_chars = ['+', '-']
    Legal_chars.extend(list(range(10)))
    Legal_chars.extend([chr(i) for i in range(65, 65 + 26)])
    Legal_chars.extend([chr(i) for i in range(97, 97 + 26)])
    if all(set(string)) not in Legal_chars:
        return -1

    i = 0
    sum_val = 0
    chars = list(string)
    # 遍历字符串中的每一个字符
    while i < len(chars):
        c = chars[i]

        # 遇到"-"，则一直往后读取数字，直到遇到非数字字符时，让和减去该数字。
        if c == '-':
            num = 0
            while i < len(chars):
                i += 1
                if chars[i].isdigit():
                    num = num * 10 + int(chars[i])
                else:
                    sum_val += -1 * num
                    break
        elif c.isdigit():
            sum_val += int(c)
        i += 1

    return sum_val


if __name__ == '__main__':
    assert solve_method("bb1234aa") == 10
    assert solve_method("bb12-34aa") == -31
```