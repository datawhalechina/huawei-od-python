# 021 仿LISP运算

## 题目描述

LISP语言唯一的语法就是括号要配对。形如`(OP P1 P2 ...)`，括号内元素由单个空格分。其中第一个元素`OP`为操作符，后续元素均为其参数，参数个数取决于操作符类型。

注意：`P1`、`P2`也有可能是另外一个嵌套的`(OP P1 P2 ...)`，当前`OP`类型为`add`、`sub`、`mul`、`div`（全小写），分别代表整数的加减乘除法。简单起见，所有`OP`参数个数均为2。

举例：

- 输入：`(mul 3 -7)`，输出：-21
- 输入：`(add 1 2)`，输出: 3
- 输入：`(sub(mul 2 4) (div 9 3))`，输出: 5
- 输入：`(div 1 0)`，输出: `error`
  
题目涉及数字均为整数，可能为负；不考虑32位溢出翻转，计算过程中也不会发生32位溢出翻转；除零错误时，输出`error`，除法遇除不尽时，向下取整，即3/2 = 1。

## 输入描述

输入为长度不超过512的字符串，用例保证无语法错误。

## 输出描述

输出计算结果或者`error`。

## 示例描述

### 示例一

**输入：**

```text
(div 12 (sub 45 45))
```

**输出：**

```text
error
```

### 示例二

**输入：**

```text
(add 1 (div -7 3))
```

**输出：**

```text
-2
```

## 解题思路

**基本思路：** 实际上是四则运算，将`add/sub/mul/div`一一对应四则运算中的加减乘除，并用栈的方式进行运算。

1. 初始化用于存储操作数和操作符的栈`stack`。
2. 遍历运算表达式字符串：
   - 如果是左括号，直接压入栈中。
   - 如果是字母，则存入操作符字符串`op_word`。
   - 如果是数字、小数点、负号，则存入数字字符串`num_str`。
   - 如果是右括号或者空格，则将操作符字符串`op_word`或数字字符串`num_str`入栈。
   - 如果是右括号，则取出栈顶的两个数和操作符进行运算，如果是除法运算，出现分母为`0`，即`num2==0`，则返回`error`，其它结果入栈
3. 返回`stack`栈顶元素，即为运算结果。    

## 解题代码

```Python
import math


def solve_method(ops):
    # 用于存储操作数和操作符的栈
    stack = list()
    res = 0
    num_str, op_word = "", ""

    for ch in ops:
        if ch == "(":
            # 如果是左括号，直接压入栈中
            stack.append(ch)
        elif ch.isalpha():
            op_word += ch
        elif ch.isnumeric() or ch in ["-", "."]:
            num_str += ch
        elif ch.isspace() or ch == ")":
            if num_str != "":
                stack.append(int(num_str))
                num_str = ""
            if op_word != "":
                stack.append(op_word)
                op_word = ""

        if ch == ")":
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
                res = math.floor(num1 / num2)

            # 将计算结果压入栈中
            stack.append(res)

    return stack[0]


if __name__ == '__main__':
    assert solve_method("(div 12 (sub 45 45))") == "error"
    assert solve_method("(add 1 (div -7 3))") == -2
```

