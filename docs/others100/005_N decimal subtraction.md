# 005-N进制减法

## 题目描述

实现一个基于字符串的N进制减法。
需要对输入的两个字符串按照给定的N进制进行减法操作，输出正负符号和表示结果的字符串

## 输入描述

三个参数。
第一个参数是整数形式的进制N值，2<=N<=35,
第二个参数为被减数字符串；
第三个参数为减数字符串。
有效的字符包括0-9以及小写字母a~z,字符串有效字符个数最大为100个字符，另外还有结尾的\0。

* 限制：
  输入的被减数和减数，除了单独的0以外，不能是以0开头的字符串。
  如果输入有异常或者计算过程中有异常此时应当输出-1表示错误。

## 输出描述

输出：2个。
其一为减法计算的结果，-1表示出错，0表示结果为整数，1表示结果为负数。
其二为表示结果的字符串。

## 示例描述

### 示例一

**输入：**
```shell
2 11 1
```

**输出：**
```shell
0 10
```

**说明：**  
按二进制计算11-1，计算正常，0表示符号为正数，结果为10

## 解题思路

该题最难的其实是进制转换Q,也就是将任意输入转换为预定进制的数字，例如输入11转换为3进制，然后还需要将其转换为10进制
进行计算，并将输出结果进行还原。

## 解题代码

```python
import string

# x进制转换n
def f35(n,x):
    # 检查非法
    if x < 2 or x > 35 or x > n:
        return 'ERROR'
    
    # 0-9的数字
    lil = [i for i in range(10)]
    # 定义所有ASCII字母
    li2 = list(string.ascii_letters)
    li3=['@','_']

    # 全拼在一起
    li = lil + li2 + li3
    result =''
    # 一个无限循环
    while True:
        # 计算在x进制下的商
        m = n //x
        # 计算余数
        r = n % x 
        # 说明转换已经结束，只剩下一个个位数了
        if n < x:
            # 取出li数组中索引为n的元素与结果result拼接后跳出循环
            result = str(li[n]) + result
            break
        # 不断拼接
        result = str(li[r])+result
        # 更新
        n = m
    return result

# 将num这个n进制的字符数组转换为十进制数
def any_to_decimal(num,n):
    # 定义字典：每个字符对应的十进制数
    baseStr = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
                "a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19}
    new_num = 0
    # num长度减一做最高位的幂次方
    nNum = len(num)-1
    for i in num:
        # 乘以n的nNum次方
        new_num = new_num + baseStr[i] * pow(n,nNum)
        # 幂减一
        nNum = nNum-1
    return new_num

def solve_method(line):
    split = line.split(" ")
    # 检查第二第三个元素
    if check(split[1]):return
    if check(split[2]):return
    # 将列表第一个转换为整数（进制）
    radix = int(split[0])
    # 被减数按radix进制转换为十进制
    minuend = any_to_decimal(split[1],radix)
    # 减数
    subtrahend = any_to_decimal(split[2],radix)

    diff = int(minuend)-int(subtrahend)
    # 输出正负
    sign = 0 if diff >=0 else 1
    # 计算绝对值
    value = abs(diff)

    print("%d %s"%(sign,f35(value,radix)))

def check(str):
    # 字符串长度大于1且以0开头时
    if len(str)>1 and str.startswith("0"):
        print(-1)
        return True
    # 出现其他异常
    return False

line = input().strip()
solve_method(line)
```

