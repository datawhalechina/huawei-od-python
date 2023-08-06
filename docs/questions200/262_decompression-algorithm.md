# 262 解压缩算法

## 题目描述

现需要实现一种算法，能将一组压缩字符串还原成原始字符串，还原规则如下：

1．字符后面加数字N，表示重复字符N次。例如：压缩内容为A3，表示原始字符串为AAA。

2．花括号中的字符串加数字N，表示花括号中的字符串重复N次。例如：压缩内容为{AB}3，表示原始字符串为ABABAB。

3．字符加N和花括号后面加N，支持任意的嵌套，包括互相嵌套。例如：压缩内容可以{A3B1{C}3}3。

## 输入描述

输入一行压缩后的字符串

## 输出描述

输出压缩前的字符串

## 说明
输入输出字符串区分大小写

输入的字符串长度为范围[1,10000]

输出的字符串长度为范围[1,100000]

数字N范围[1,10000]

## 示例描述

### 示例一

**输入：**
```text
A3
```

**输出：**
```text
AAA
```
**说明：**
```text
A3代表A字符重复3次
```

### 示例二

**输入：**
```text
{A3B1{C}3}3
```

**输出：**
```text
AAABCCCAAABCCCAAABCCC
```
**说明：**
```text
{A3B1{C}3}3代表A字符重复3次，B字符重复1次，花括号中的C字符重复3次，最外层花括号中的AAABCCC重复3次
```

## 解题思路

**基本思路：**

栈 - 数字不进栈，数字的结束作为计算的标志
1. 若当前元素为数字，需要单独存储数字（因为数字可能是多位数）
2. 若当前元素不为数字（进行计算） 
	- 若当前数字域不为空 → 判断栈顶元素
		- 若栈顶元素为字母：将字母累计次数后，重新存入栈顶
		- 若栈顶元素为}：寻找最近的{，将期间的字母域合并并累计次数后，重新存入栈顶
	- 将当前元素压入栈顶
3. 原始字符串末尾添加结束符#，确保最后一个数字得到计算

**代码思路：**
1. 原始字符串末尾添加结束符#，确保最后一个数字得到计算
2. 数字域和字母域初始化
3. 若当前元素为数字，单独存储数字到数字域`nums`（因为数字可能是多位数）
4. 若当前元素不为数字，若数字域不为空，需要进行计算（计算方式如下），然后将当前元素存入栈中
    > 计算方式：判断栈顶元素，栈顶元素只可能为字母或`}`
    > - 若栈顶为字母，直接字母重复N次，重新存入栈顶；
    > - 若栈顶为`}`，寻找最近的`{`，将其间字母域重复N次，重新存入栈顶；
    > 数字域和字母域重置
5. 拼接栈内元素（记得排除结束符#）

## 解题代码
```python
def solve_method(string):
    string += "#"
    stack = []
    num, temp = 0, ""
    for c in string:
        if c.isdigit():
            num = num * 10 + int(c)
            continue
        if num != 0:  # 数字统计结束，进行计算 - 此时栈肯定非空，且栈顶元素为字母或}
            if stack[-1].isalpha():
                stack[-1] = stack[-1] * num
            elif stack[-1] == "}":
                stack.pop() # 弹出}
                while stack[-1] != "{":
                    temp = stack.pop() + temp
                stack[-1] = temp * num # 弹出{
            num, temp = 0, ""
        stack.append(c)
    return "".join(stack[:-1])

if __name__ == "__main__":
    # {A3B1{C}3}3
    string = input().strip()
    print(solve_method(string))

    assert solve_method("{A3B1{C}3}3") == "AAABCCCAAABCCCAAABCCC"
    assert solve_method("A3") == "AAA"
    assert solve_method("{AD11B1{CF}3}3") == "ADDDDDDDDDDDBCFCFCFADDDDDDDDDDDBCFCFCFADDDDDDDDDDDBCFCFCF"
```