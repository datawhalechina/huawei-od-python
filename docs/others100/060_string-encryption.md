# 060 字符串加密

## 题目描述

给你一串未加密的字符串`str`，通过对字符串的每一个字母进行改变来实现加密，加密方式是在每一个字母`str[i]`偏移特定数组元素`a[i]`的量，数组`a`前三位已经赋值：`a[0]=1, a[1]=2, a[2]=4`。

当`i >= 3`时，数组元素`a[i]=a[i-1]+a[i-2]+a[i-3]`。

例如：原文`abcde`加密后是`bdgkr`，其中偏移量分别是`1,2,4,7,13`。

## 输入描述

第一行是一个整数`n`，表示有`n`组测试数据，其中1 <= n <= 1000，每组数据包含一行。

原文`str`只含有小写字母，长度范围是0 < 长度 <= 50。

## 输出描述

每组测试数据输出一行，表示字符串的密文。

## 示例描述

### 示例一

**输入：**
```text
1
xy
```

**输出：**
```text
ya
```

## 解题思路

该题的解题逻辑是：
1. 定义一个列表a，包含数字1，2，4。
2. 定义一个长度为50的列表offsets，初始值全部为0。
3. 遍历offsets列表，如果i小于3，将a[i]赋值给offsets[i]；
如果i>=3，则将offsets[i-1]+offsets[i-2]+offsets[i-3]的结果赋值给offsets [i]。
4. 遍历strings列表，将每一个字符串转化为字符列表，并将其遍历，对于每一个字符，将其转化为ASCII码，再将其加上
offsets[i]，模26，再加97，最后再将该ASCII码转化为字符。将每一次转换的字符拼接成字符串并输出。
5. 输入字符串的数量n，再输入n个字符串，并将它们存入strings 列表中。最后调用solve _method()函数，
传入strings列表作为参数。
   
## 解题代码

```python
def solve_method(strings):
    a = [1, 2, 4]
    offsets = [0] * 50
    for i in range(50):
        if i < 3:
            offsets[i] = a[i]
        else:
            offsets[i] = offsets[i - 1] + offsets[i - 2] + offsets[i - 3]
    chars = list(strings)
    for i in range(len(chars)):
        c = chars[i]
        chars[i] = chr((ord(c) - 97 + offsets[i]) % 26 + 97)
    return ''.join(chars)


if __name__ == '__main__':
    n = int(input().strip())
    for i in range(n):
        strings = input().strip()
        res = solve_method(strings)
        print(res)
```

