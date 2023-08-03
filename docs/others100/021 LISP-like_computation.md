# 021 仿 LISP 运算

## 题目描述

LISP 语言唯一的语法就是括号要配对。形如(OP P1 P2 ...)，括号内元素由单个空格分。其中第一个元素 OP 为操作符，后续元素均为其参数，参数个数取决于操作符类型

注意：P1、P2也有可能是另外

一个嵌的(OP P1 P2 ...)当前 OP 类型为 add / sub / mul/ div (全小写)，分别代表整数的加减乘除法简单起见，所有 OP 参数个数均为 2

举例

输入:  (mul 3 -7)输出: -21
输入:  (add 1 2)输出: 3
输入:  (sub(mul 2 4) (div 9 3))输出: 5
输入:  (div 1 0)输出: error 题目涉及数字均为整数，可能为负
不考虑 32 位溢出翻转，计算过程中也不会发生 32 位溢出翻转 除零错误时，输出“erro”，除法遇除不尽，向下取整，即 3/2 = 1

## 输入描述

输入为长度不超过 512 的字符串，用例保证了无语法错误

## 输出描述

输出计算结果或者“error"

## 示例描述

### 示例一

**输入：**

```Plain Text
( div 12 ( sub 45 45 ) )
```

**输出：**

```Plain Text
error
```

### 示例二

**输入：**

```Plain Text
( add 1 ( div -7 3 ) )
```

**输出：**

```Plain Text
-1
```

## 解题思路

**基本思路：** 实际上是四则运算，将add/sub/mul/div一一对应四则运算中的加减乘除，并用栈的方式进行运算

1. 首先用`split()`将输入的表达式根据空格进行分割

2. 依次入栈

    3. 如果是`"("` 或者是 字母 ，则入栈

    4. 如果是数字，也是直接入栈，并将数字转换为整数类型

    5. 如果是右括号，则取出栈顶的两个数和操作符进行运算

    6. 如果是除法运算，出现分母为`0`，即`num2==0`，则返回`error`，其它结果入栈

7. 返回结果。

注意：输入时要用空格隔开字符 例如：( add 1 ( div -7 3 ) )

## 解题代码

```Python
from math import floor

def solve(s):
    
    # 分割表达式中的操作符和操作数
    ops = s.split()
    
    stack = list()  # 用于存储操作数和操作符的栈
    res = 0
    
    for ch in ops:
        if ch == "(" or ch.isalpha():
            # 如果是左括号或字母，直接压入栈中
            stack.append(ch)
        elif ch == ")":
            # 如果是右括号，取出栈顶的两个数和操作符进行计算，并将结果压入栈中
            num2 = stack.pop()
            num1 = stack.pop()
            op = stack.pop()
            stack.pop()
            
            if op == "add":
                res = num1 + num2
            elif op == "sub":
                res = num1 - num2
            elif op == "mul":
                res = num1 * num2
            elif op == "div":
                if num2 == 0:
                    # 如果除法操作的除数为0，返回error
                    return "error"
                res = floor(num1 / num2)
            
            # 将计算结果压入栈中
            stack.append(res)
        else:
            # 如果是数字，直接压入栈中
            stack.append(int(ch))

    return stack[0]

if __name__ == "__main__":
    expression = input("请输入表达式，用空格隔开字符: ")
    result = solve(expression)
    print(result)
```

