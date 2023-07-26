# 003 IPv4地址转换成整数

## 题目描述

存在一种虚拟IPv4地址，由4小节组成，每节的范围为0\~255，以`#`号间隔，虚拟IPv4地址可以转换为一个32位的整数，例如：
- `128#0#255#255`：转换为32位整数的结果为`2147549183`(0×80 00 FF FF)
- `1#0#0#0`：转换为32位整数的结果为`16777216`(0x 01 00 00 00)

现以字符串形式给出一个虚拟IPv4地址，限制第1小节的范围为1\~128，即每一节范围分别为(1\~128)#(0\~255)#(0\~255)#(0\~255)，要求每个IPv4地址只能对应到唯一的整数上。如果是非法IPv4，返回`invalid IP`。

**备注：** 输入不能确保是合法的IPv4地址，需要对非法IPv4（空串、含有IP地址中不存在的字符、非合法的`#`分十进制、十进制整数不在合法区间内）进行识别，返回特定错误。

## 输入描述

输入一行，虚拟IPv4地址格式字符串。

## 输出描述

输出以上按照要求输出整型或者特定字符。

## 示例描述

### 示例一

**输入：**
```
100#101#1#5
```

**输出：**
```
1684340997
```

### 示例二

**输入：**
```
1#2#3
```

**输出：**
```
invalid IP
```


## 解题思路

1. 验证IPv4是否合法
    - 验证是否包含`#`字符。
    - 是否能分隔成4段。
    - 是否每段都符合要求。
2. 遍历每一个分隔之后的字符串，将其转换为整数之后，每次遍历都左移4位，最后一次不左移。
3. 返回结果：
   - 如果合法，返回32位整数的结果。
   - 如果不合法，返回`invalid IP`。

## 解题代码

```python
def check_ip(ip):
    is_valid = False
    if "#" in ip:
        ip_strings = ip.split("#")
        length = len(ip_strings)
        if length == 4 \
                and 1 <= int(ip_strings[0]) <= 128 \
                and 0 <= int(ip_strings[1]) <= 255 \
                and 0 <= int(ip_strings[2]) <= 255 \
                and 0 <= int(ip_strings[3]) <= 255:
            is_valid = True

    return is_valid


def solve_method(ip):
    if check_ip(ip):
        ip_strings = ip.split("#")
        num = 0
        for ip_string in ip_strings:
            num += int(ip_string)
            num = num << 8

        num = num >> 8
        return num
    else:
        return "invalid IP"


if __name__ == '__main__':
    assert solve_method("100#101#1#5") == 1684340997
    assert solve_method("1#2#3") == "invalid IP"
```

