# 147 水仙花数2

## 题目描述

给定非空字符串`s`，将该字符串分割成一些子串，使每个子串的ASCII码值的和均为水仙花数（即3位的自幂数）。

1．若分割不成功则返回0（包括本身满足条件，却无法正确分割的字符串）。
2．若分割成功且分割结果不唯一，则返回-1。
3．若分割成功且分割结果唯一，则返回分割后子串的数目。

## 输入描述

输入一个字符串，其最大长度为200。

## 输出描述

根据题目中的情况输出响应结果

## 示例描述

### 示例一

**输入：**

```text
abc
```

**输出：**

```text
0
```

**说明：**  

分割不成功。

### 示例二

**输入：**

```text
f3@d5a8
```

**输出：**

```text
-1
```

**说明：**  

分割成功但分割结果不唯一，可以分割为两组，一组`f3`(153)和`＠d5a8`，另一组`f3＠d5`(370)和`a8`(153)，说明分割不成功。 

### 示例三

**输入：**

```text
AXdddF 
```

**输出：**

```text
2
```

**说明：**  

成功分割且分割结果唯一。

可以分割为`AX`(153)、`dddF`(370)两个子串。

## 解题思路

1. 遍历所有字符串的分割点：
    - 将字符串分割成两个子串。
    - 将两个子串都转换为ASCII码值。  
    - 判断子串是否都为水仙花数：如果符合，则存入列表`res`中，如果不符合，则继续分割字符串。
2. 判断列表`res`的长度：
    - 如果长度大于1，表示分割成功且结果不唯一，返回-1。
    - 如果长度等于0，表示分割不成功，返回0。
    - 如果长度等于1，表示分割成功，结果唯一，返回第1个元素的长度，即为分割后子串的数目。

## 解题代码

```python
def check_narcissistic(num):
    bit = num
    sum_val = 0
    n = len(str(num))
    while bit != 0:
        sum_val += (bit % 10) ** n
        bit //= 10
    return sum_val == num


def split_string(string, res):
    for i in range(1, len(string) + 1):
        sub1 = string[:i]
        sub2 = string[i:]

        sub1_num = sum(map(ord, sub1))
        sub2_num = sum(map(ord, sub2))

        if check_narcissistic(sub1_num):
            if check_narcissistic(sub2_num):
                if sub1_num != 0 and sub2_num != 0:
                    if sub1_num < sub2_num:
                        res.append([sub1, sub2])
                    else:
                        res.append([sub2, sub1])
            else:
                split_string(sub2, res)


def solve_method(line: str) -> int:
    # 确保输入有效
    if len(line) > 200:
        return -1

    res = []
    split_string(line, res)

    if len(res) > 1:
        # 若分割成功且结果不唯一，返回-1
        return -1
    elif len(res) == 0 or len(res[0]) == 1:
        return 0
    else:
        # 返回分割后子串的数目
        return len(res[0])


if __name__ == '__main__':
    assert solve_method("abc") == 0
    assert solve_method("f3@d5a8") == -1
    assert solve_method("AXdddF") == 2
    assert solve_method("f3") == 0
```