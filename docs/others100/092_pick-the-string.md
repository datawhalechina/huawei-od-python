# 092 挑选字符串

## 题目描述

给定`a-z`26个英文字母小写字符串组成的字符串`A`和`B`，其中`A`可能存在重复字母，`B`不会存在重复字母，现从字符串`A`中按规则挑选一些字母可以组成字符串`B`。

挑选规则如下：

同一个位置的字母只能挑选一次，被挑选字母的相对先后顺序不能被改变，求最多可以同时从`A`中挑选多少组能组成`B`的字符串。

## 输入描述

输入为2行，第一行输入字符串`A`，第二行输入字符串`B`，行首行尾没有多余空格。

## 输出描述

输出一行，包含一个数字，表示最多可以同时从`A`中挑选多少组能组成`B`的字符串，行末没有多余空格。

## 示例描述

### 示例一

**输入：**
```text
badc
bac
```

**输出：**
```text
1
```

### 示例二

**输入：**
```text
badc
abc
```

**输出：**
```text
0
```

## 解题思路

1. 初始化统计值`count`。
2. 使用`while`循环匹配字符串：
   - 设置遍历索引`pos`。
   - 遍历字符串b：
        - 如果找到了字符串b中的一个字符，那就用`_`替换掉，并把找到的位置设置给索引。
        - 如果没有找到，返回`count`。
   - 找到一个，累计加1，继续循环匹配。 

## 解题代码

```python
def solve_method(a, b):
    count = 0
    while True:
        chars = list(b)
        # 设置遍历索引
        pos = 0
        for ch in chars:
            # 找到了字符串b中的一个字符
            index = a.find(ch, pos)
            if index != -1:
                # 如果找到了，那就用`_`替换掉
                a = a.replace(ch, "_", 1)
                # 把找到的位置设置给索引
                pos = index
            else:
                return count
        # 找到一个，累计加1
        count += 1


if __name__ == '__main__':
    assert solve_method("badc", "bac") == 1
    assert solve_method("badc", "abc") == 0
    assert solve_method("abacc", "abc") == 1
    assert solve_method("abcabc", "abc") == 2
```