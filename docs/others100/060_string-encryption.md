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

1. 按照题目中的公式初始化一个长度为50的列表`offsets`，用于表示偏移量。
2. 遍历每一组测试数据：
    - 遍历字符串中的每一个字母：
      - 将字母按照顺序偏移相对应的`offsets`里面的偏移量，公式：`chars[i] = chr((ord(c) - 97 + offsets[i]) % 26 + 97)`。
3. 返回结果列表。    
   
## 解题代码

```python
def solve_method(strings):
    offsets = [0] * 50
    offsets[0:2] = [1, 2, 4]
    for i in range(3, 50):
        offsets[i] = offsets[i - 1] + offsets[i - 2] + offsets[i - 3]

    result = []
    for chars in strings:
        chars = list(chars)
        for i in range(len(chars)):
            c = chars[i]
            chars[i] = chr((ord(c) - 97 + offsets[i]) % 26 + 97)
        result.append("".join(chars))
    return result


if __name__ == '__main__':
    assert solve_method(["xy"]) == ["ya"]
    assert solve_method(["xyabcdef", "abcdefghijk"]) == ["yaeipbwi", "bdgkrdykbxu"]
```

