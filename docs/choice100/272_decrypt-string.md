# 272 字符串解密加扰字符串

## 题目描述

给定两个字符串`string1`和`string2`。
- `string1`是一个被加扰的字符串，由小写英文字母（a-z）和数字字符（0-9）组成，而加扰字符串由0-9和a-f组成，`string1`里面可能包含0个或多个加扰子串，剩下可能有0个或多个有效子串，这些有效子串被加扰子串隔开。
- `string2`是一个参考字符串，仅由小写英文字母（a-z）组成。

你需要在`string1`字符串里找到一个有效子串，这个有效子串要同时满足下面两个条件：
1. 这个有效子串里不同字母的数量不超过且最接近于`string2`里不同字母的数量，即小于或等于`string2`里不同字母的数量的同时且最大。
2. 这个有效子串是满足条件（1）里的所有子串（如果有多个的话）里字典序最大的一个。

如果没有找到合适条件的子串，请输出"Not Found"

**示例：**

输入字符串`string1`为"thisisanewday111forme"，输入字符串`string2`为"good"。

`string1`里有效子串和加扰子串分割后，可表示为："thisis"+"a"+"n"+"e"+"w"+"da"+"y"+"111f"+"orm"+"e"，去除加扰子串（"a"、"e"、"da"、"111f"、"e"）后的有效子串候选为"thisis"、"n"、"w"、"y"、"orm"。

输入字符串`string2`里不同字母的数量为3个，分别是"g"、"o"、"d"，从有效子串候选里可以找出"orm"子串满足要求，其不同字母的数量为3，最接近`string2`不同字母的数量。

## 输入描述

```
input_string1
input_string2
```

**说明：**
- 输入为两个字符串，第1行表示`string1`（被加扰的字符串），第2行表示`string2`（参考字符串）。
- 输入字符串`string1`长度在1\~100000之间，字符串`string2`长度在1\~500之间。

## 输出描述

输出一个符合要求的有效字符串。

## 示例描述

### 示例一

**输入：**
```
123admyffc79pt
ssyy
```

**输出：**
```
pt
```

**说明：**  
将输入字符串`string1`里的加扰子串"123ad"、"ffc79"去除后得到有效子串序列["my","pt"]，其中"my"里面不同字母的数量为2（有m和y两个不同字母），"pt"里面不同字母的数量为2（有p和t两个不同字母）

输入字符串`string2`里面不同字母的数量为2（有`s`和`y`两个不同字母）

最终输出结果为"pt"，其不同字母的数量最接近于"ssyy"里不同字母的数量，同时字典序最大。

### 示例二

**输入：**
```
123admyffc79ptaagghi2222smeersst88mnrt
ssyyfgh
```

**输出：**
```
mnrt
```

**说明：**  
将输入字符串`string1`里的加扰子串"123ad"、"ffc79"、"aa"、"2222"、"ee"、"88"去除后得到有效子串序列["my","pt","gghi","sm","rsst","mnrt"]；输入字符串`string2`里不同字母的数量为5。

最终输出结果为"mnrt"，其不同字母的数量为4，最接近于"ssyyfgh"里不同字母的数量，其他有效子串不同字母的数量都小于"mnrt"。

### 示例三

**输入：**
```
abcmnq
rt
```

**输出：**
```
Not Found
```

**说明：**  
将输入字符串`string1`里的加扰子串"abc"去除后得到有效子串序列["mnq"]，输入字符串`string2`里不同字母的数量为2。

最终输出结果为"Not Found"，没有符合要求的有效子串，由于有效子串里面不同字母的数量为3，大于输入字符串`string2`里面不同字母的数量。

## 解题思路

1. 获取有效子串：使用临时字符串`tmp_string`保存有效子串，然后保存到有效子串序列`avail_strings`中。
2. 使用`set`去重，得到参考字符串`string2`的长度
3. 遍历有效子串序列，进行判断：
    - 如果有效子串的长度小于参考字符串的长度
    - 如果满足条件，则用`result`保存有效子串
    - 如果有效子串的长度相等，取字典序大的有效子串，并用`result`保存有效子串
4. 返回最终有效子串。

## 解题代码

```python
def solve_method(string1, string2):
    # 获取有效子串
    avail_strings = get_available_strings(string1)

    # 参考字符串的长度
    string2_len = len(set(string2))

    result = ""
    for ava_str in avail_strings:
        if len(ava_str) > 0:
            # 有效子串的长度
            ava_str_len = len(set(ava_str))

            # 如果有效子串的长度小于参考字符串的长度
            if ava_str_len <= string2_len:
                result_len = len(set(result))
                # 如果满足条件
                if ava_str_len > result_len:
                    result = ava_str
                # 如果长度相等，取字典序大的那个
                elif ava_str_len == result_len and ava_str > result:
                    result = ava_str

    return result if len(result) > 0 else "Not Found"


def get_available_strings(string1):
    scrambled_sub = "1234567890abcdef"

    avail_strings = []
    tmp_string = ""
    for c in string1:
        if c not in scrambled_sub:
            tmp_string += c
        else:
            if tmp_string != "":
                avail_strings.append(tmp_string)
                tmp_string = ""

    if tmp_string != "":
        avail_strings.append(tmp_string)

    return avail_strings
```