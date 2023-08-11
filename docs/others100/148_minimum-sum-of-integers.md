# 148 求字符串中所有整数的最小和

## 题目描述

1．输入一个字符串s，它只包含'a'—'z'，'A'—'Z'，'＋'，'-'，以及合法的整数；

2．合法的整数包括：

- 正整数由一个或者多个`0—9`组成，如`0 2 3 002 102` 。
- 负整数以负号”-“开头，数字部分由一个或者多个`0-9`组成，如`-0、-1、-123、-12345 `。



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

1 1+2+(-34)=31 


## 解题思路

**基本思路：** 

遍历字符串中的每一个字符

- 如果是"-"，则**贪心地**往后读取数字，直到遇到非数字字符。让和减去该数字。
  - 这里可以用一个子循环处理

- 如果是数字，直接让和加上该数字



## 解题代码

```python
def solve_method(string: str) -> int:
    # 检查输入是否有效
    allowed_character = ['+', '-']
    allowed_character.extend(list(range(10)))
    allowed_character.extend([chr(i) for i in range(65, 65 + 26)])
    allowed_character.extend([chr(i) for i in range(97, 97 + 26)])
    assert all(set(string)) in allowed_character

    # 遍历字符串中的每一个字符
    i = 0   # 索引,使用while循环便于我们手动改变i的值
    sum = 0 # 返回的最小和
    chars = list(string)
    while i < len(chars):
        c = chars[i]

        # 遇到"-"，则贪心地往后读取数字，直到遇到非数字字符时，让和减去该数字，出循环。
        if c == '-':
            num = 0
            while i < len(chars):
                i += 1
                if chars[i].isdigit():
                    num = num * 10 + int(chars[i])
                else:
                    sum += -1 * num
                    break

        elif c.isdigit():
            sum += int(c)

        i += 1

    return sum
```