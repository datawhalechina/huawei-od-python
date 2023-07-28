#  111-新工号系统

## 题目描述

3020 年空间通信集团的员工突破 20 亿人，即将遇到现有工号不够的窘境现在你负责调研新工号系统，继承历史传统新的工号系统由小写英文字母 `a-z` 和数字 `0-9` 两部分构成。
新工号由一段英文字母开头。之后跟随一段数字，比如
`aaahw0001` , `a12345` , `abcd1` , `a00` .
注意:新工号不能全为字母或数字，允许数字部分有 `前导0`或者全为 `0`。
但是过长的工号会增加同事们的记忆成本，
现在给出新工号 至少需要分派的人数 `x`
和新工号中字母的长度 `y`，
求新工号中数字的最短长度 `z`.

## 输入描述

行两个非负整数 `x y`,数字用单个空格分隔。
`0 <x <= 2^50-1`
`0< y <= 5`

## 输出描述

输出新工号中数字的最短长度 `z` 

## 示例描述

### 示例一

**输入：**

```text
260 1
```

**输出：**

```text
1
```

### 示例二

**输入：**

```text
26 1
```

**输出：**

```text
1
```



### 示例三

**输入：**

```text
2600 1
```

**输出：**

```text
2
```

## 解题思路

1. 先判断分派人数 `Y`是不是小于给定字母长度`x`加一个数字构成的工号数，如果是返回结果1.
2. 根据公式$z \geq log(\frac{Y}{26^x})$(`z`为字母长度  `Y`分派人数，给定字母长度`x`)可以得到z的最小值。直接利用上述公式求解然后对结果向上取整。

## 解题代码

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-28 11:33:18
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os
import math


def solve_method(x,y):

	cb = math.pow(26, y)

	if cb >= x:
		return 1
	else:
		return math.ceil(math.log(x/cb,10))

if __name__ == "__main__":
	
	assert solve_method(260,1) == 1
	assert solve_method(26,1) == 1
	assert solve_method(2600,1) == 2
	assert solve_method(27,1) == 1
	assert solve_method(2601,1) == 3

```



