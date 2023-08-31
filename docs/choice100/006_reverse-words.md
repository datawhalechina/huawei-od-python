# 006 单词倒序

## 题目描述

输入单词英文句子，里面包含英文字母、空格以及`,``.``?`三种标点符号，请将句子内每个单词进行倒序，并输出倒序后的语句。

## 输入描述

输入字符串`S`，`S`的长度`1 <= N <=100`

## 输出描述

输出逆序后的字符串。

**备注：**  
标点符号左右的空格个数大于0，单词间的空格个数大于0。

## 示例描述

### 示例一

**输入：**
```text
yM eman si boB.
```

**输出：**
```text
My name is Bob.
```

### 示例二

**输入：**
```text
woh era uoy ? I ma enif.
```

**输出：**
```text
how are you ? I am fine.
```

## 解题思路

1. 遍历单词英文句子中的每一个字符，判断是否为字母。
2. 如果是字母，则用临时`words`字符串存储起来。
3. 如果不是字母，则先将单词逆序存放到结果字符串`result`中，然后再拼接非字母的字符。
4. 遍历结束后，返回结果字符串`result`。

## 解题代码

```python
def solve_method(line):
    result = ""
    # 使用临时字符串存储单词
    words = ""
    for char in line:
        if char.isalpha():
            words += char
        else:
            # 将单词逆序
            result += words[::-1]
            words = ""
            result += char

    return result

if __name__ == '__main__':
    s = "yM eman si boB."
    assert solve_method(s) == "My name is Bob."

    s = "woh era uoy ? I ma enif."
    assert solve_method(s) == "how are you ? I am fine."
```