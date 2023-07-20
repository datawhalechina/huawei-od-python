# 007-TLV编码

## 题目描述

TLV编码是按Tag Length Value格式进行编码的。
一段码流中的信元用**tag**标识，tag在码流中唯一不重复，**length**表示信元value的长度，value表示信元的值，
码流以某信元的tag开头，tag固定占一个字节，length固定占两个字节，字节序Q为小端序。
现给定tLv格式编码的码流以及需要解码的信元tag,请输出该信元的value。

输入码流的16进制字符中，不包括小写字母：
且要求输出的16进制字符串中也不要包含小写字母：
码流字符串的最大长度不超过50000个字节。

## 输入描述

* 第一行为第一个字符串，表示待解码信元的tag:
* 输入第二行为一个字符串，表示待解码的16进制码流；
* 字节之间用空格分割。

## 输出描述

输出一个字符串，表示待解码信元以16进制表示的value。

## 示例描述

### 示例一

**输入：**
```shell
31
32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC 
```

**输出：**
```shell
32 33
```

**说明：**  

```
32 01 00 AE 
90 02 00 01 02 
30 03 00 AB 32 31 
31 02 00 32 33 
33 01 00 CC
```



* 需要解析的信源的tag是31；
* 从码流的起始处开始匹配，tag为32的信元长度为1(0100，小端序表示为1)：
* 第二个信元的tag为90其长度为2；
* 第三个信元的tag为30其长度为3；
* 第四个信元的tag为31其长度为2(0200)：
* 所以返回长度后面的两个字节即可为32 33。

## 解题思路

本题是一个解析二进制数据的方法，输入包含两行字符串

* 第一行字符串tag是两个字符长，表示要提取的数据类型
* 第二行字符串source包含多个二进制数据项，每个数据项包含一个双字符的tag、一个双字符的数据长度的十六进制字符串、数据内容。
* 该方法从source中解析所有与tag匹配的数据项，并输出其数据内容。

###核心知识点

该方法通过迭代扫描二进制数据源source,每次取出一个数据项，若tag与当前数据项的tag相同，则获取该数据项的长度lenDEC,进
而提取数据内容value并输出。数据项长度以两个字符的十六进制字符串形式给出，需要转换为十进制整数lenDEC后计算数据内容长
度。

## 解题代码

```python
# coding:utf-8

# def solveMethod(tag:str,source:str)->None:
#     p=0
#     # 迭代扫描
#     while p < len (source):
#         # 取字符串的0~1位置上的
#         curTag = source[p:p + 2]
#         # 因为是小端序所以要逆过来拼接
#         lenHEX = source[p + 6:p + 8] + source[p + 3:p + 5]
#         # 转换为十进制
#         lenDEC = int(lenHEX,16)
#         # 判断匹配tag
#         if tag == curTag:
#             # 取出往后lenDEC个位置的字符
#             value = source[p +9: p +9 + lenDEC * 3]
#             print(value)
#         p += 9 + lenDEC * 3

# if __name__ == '__main__':
#     tag = input()
#     source = input()
#     solveMethod(tag,source)

# 改进版
def solveMethod(tag:str,source:str)->None:
    p=0
    # 迭代扫描
    while p < len (source):
        # 取字符串的0~1位置上的
        curTag = source[p]
        # 因为是小端序所以要逆过来拼接
        lenHEX = source[p+2] + source[p+1]
        # 转换为十进制
        lenDEC = int(lenHEX,16)
        # 判断匹配tag
        if tag == curTag:
            # 取出往后lenDEC个位置的字符
            value = source[p +3: p +3 + lenDEC]
            print(' '.join(value))
        p += 3 + lenDEC

if __name__ == '__main__':
    tag = input()
    source = input().split(" ")
    solveMethod(tag,source)
```

