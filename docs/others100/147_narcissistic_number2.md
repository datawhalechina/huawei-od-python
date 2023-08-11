# 147 水仙花数2

## 题目描述

给定非空字符串s，将该字符串分割成一些子串，使每个子串的ASCII码值的和均为水仙花数（即3位的自幂数）。

1．若分割不成功则返回0；（包括本身满足条件，却无法正确分割的字符串）

2．若分割成功且分割结果不唯一则返回-1；

3．若分割成功且分割结果唯一则返回分割后子串的数目输入



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

分割不成功




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

分割成功但分割结果不唯一，可以分割为两组，一组f3(153)和＠d5a8，另一组 f3＠d5 (370)和a8 (153)，说明分割不成功 



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

成功分割且分割结果唯一

可以分割为AX（153）、dddF（370）两个子串





### 示例四

**输入：**

```text
f3
```

**输出：**

```text
0
```

**说明：**  

`f3`本身是一个满足条件的字符串，但是无法分割，分割不成功返回0。




## 解题思路

**基本思路：** 

- 本题的目标是查找一个字符串中是否存在一个子字符串，使得该子字符串的每一位的ASCII码值的立方和等于一个水仙花数。
- 代码通过不断地将一个字符串分割为两个部分，并判断每个部分是否满足条件，从而实现查找的逻辑。如果存在满足条件的子字符串，则将它的长度加入结果数组；如果结果数组的大小大于1，则返回—1；否则，如果结果数组的大小为1，则返回该数组中的唯一数值。



**核心知识点：**
ASCII码和 ordQ函数：ASCII码是计算机内码的一种，每个字符对应一个ASCII码。Python中的ord函数可以返回一个字符的ASCII码。



**注：**

常见自幂数包括以下：

> [自幂数_百度百科 (baidu.com)](https://baike.baidu.com/item/自幂数?fromModule=lemma_inlink)
>
> 独身数（1位）共有9个: 1，2，3，4，5，6，7，8，9；
>
> 水仙花数（3位）共有4个：153，370，371，407；
>
> 四叶玫瑰数（4位）共有3个：1634，8208，9474；
>
> ...



## 解题代码

```python
from typing import List


def solve_method(line: str) -> int:
    # 1. 确保输入有效
    assert len(line) <= 200

    # 2. 使用 lambda表达式定义一个匿名函数，用于计算字符串的ascii码之和
    ascii_sum = lambda string: sum(map(ord, string))

    # 3. 定义一个匿名函数，用于判断一个数是不是水仙花数,返回bool类型
    # is_narcissistic = lambda num: num in [153, 370, 371, 407] # 这里已经知道3位数的水仙花数只有4个，算是取巧的写法
    is_narcissistic = lambda num: num == (num % 10) ** 3 + (num // 10 % 10) ** 3 + (num // 100) ** 3

    # 4. 定义一个可以递归的方法,判断某个字符串能否成功分割
    # 返回结果格式为List[List(str)] 如: f3d5a8 -> [["f3","@d5a8"],["f3@d5","a8"]]
    def my_split(string: str) -> List[List[str]]:
        res = []
        # 注意range的左右端点; 用 [:len(string)]才能获取整个字符串
        for i in range(1, len(string) + 1):
            sub1 = string[:i]
            sub2 = string[i:]
            if is_narcissistic(ascii_sum(sub1)):
                # sub2为空串(整个字符串是一个水仙花数
                if sub2 == '':
                    return [[sub1,]]

                # sub2不为空串,递归调用split去分割sub2
                else:
                    tmp = my_split(sub2)
                    # tmp是一个string的二维列表,我们在sub2的每种分割(每一行)前面插入sub1,表示一次完整分割
                    for row in tmp:
                        row.insert(0,sub1)
                        res.append(row)
        return res

    ret = my_split(line)

    # 5. 若分割成功且结果不唯一,返回-1;分割不成功则返回0; 否则返回分割后子串的数目(ret[0]的长度)
    if len(ret) > 1:
        return -1
    elif len(ret) == 0 or len(ret[0]) == 1:
        return 0
    else:
        return len(ret[0])
```