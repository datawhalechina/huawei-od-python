# 276 寻找密码

## 题目描述

小王在进行游戏大闯关，有一个关卡需要输入一个密码才能通过，密码获得的条件如下：

在一个密码本中，每一页都有一个由26个小写字母组成的若干位密码，从它的末尾开始依次去掉一位得到的新密码也在密码本中存在。

请输出符合要求的密码，如果有多个符合要求的密码，则返回字典序最大的密码。如果没有符合要求的密码，则返回空字符串。

**备注：**
1 <= 密码本的页数 <= 105
1 <= 每页密码的长度 <= 105

## 输入描述

密码本由一个字符串数组组成，不同元素之间使用空格隔开，每一个元素代表密码本每一页的密码。

## 输出描述

一个符合要求的密码字符串。

## 示例描述

### 示例一

**输入：**
```
h he hel hell hello
```

**输出：**
```
hello
```

**说明：**  
"hello"从末尾依次去掉一位得到的"hell"、"hel"、"he"、"h"在密码本中都存在。

### 示例二

**输入：**
```
b eredderd bw bww bwwl bwwln bwwlm
```

**输出：**
```
bwwln
```

**说明：**  
"bwwlm"和"bwwln"从末尾依次去掉一位得到的密码在密码本中都存在，但是"bwwln"比"bwwlm"字典序排序大，所以应该返回"bwwln"。

## 解题思路

1. 将输入的字符串序列进行排序，保证字典序
2. 逆向遍历密码本，通过设置标志位`flag`，使用`while`循环判断从末尾开始依次去掉一位的密码是否在密码本中
3. 如果密码都存在，则返回该密码，如果不存在，则跳出`while`循环，继续逆序遍历下一个密码。

## 解题代码

```python
def solve_method(line):
    codebook = line.split()
    # 保证字典序
    codebook.sort()
    # 用于去重判断
    code_set = set(codebook)
    # 逆向遍历密码本
    for i in range(len(codebook) - 1, -1, -1):
        code = codebook[i]
        tmp_code = code[:-1]
        # 是否存在的标识
        flag = True
        # 循环判断从末尾开始依次去掉一位的密码是否在密码本中
        while len(tmp_code) > 0:
            if tmp_code in code_set:
                tmp_code = tmp_code[:-1]
            else:
                flag = False
                break
        if flag:
            return code

    return ""
```