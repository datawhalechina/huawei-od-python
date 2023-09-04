# 049 增强的strstr

## 题目描述

C语言有一个库函数：`char *strstr(const char *haystack, const char *needle)`，实现在字符串`haystack`中查找第一次出现字符串`needle`的位置，如果未找到则返回`null`。

现要求实现一个`strstr`的增强函数，可以使用带可选段的字符串来模糊查询，与`strstr`一样返回首次查找到的字符串位置。

可选段使用`[]`标识，表示该位置是可选段中任意一个字符即可满足匹配条件。比如`a[bc]`表示可以匹配`ab`或`ac`。

**注意：** 目标字符串中可选段可能出现多次。

## 输入描述

与`strstr`函数一样，输入参数是两个字符串指针，分别是源字符串和目标字符串。

## 输出描述

与`strstr`函数不同，返回的是源字符串中，匹配子字符串相对于源字符串地址的偏移（从0开始算），如果没有匹配返回-1。

**补充说明：**

源字符串中必定不包含`[]`，目标字符串中`[]`必定成对出现，且不会出现嵌套。

## 示例描述

### 示例一

**输入：**
```text
abcd
b[cd]
```

**输出：**
```text
1
```

**说明：**  

相当于是在源字符串中查找`bc`或者`bd`，`bc`子字符串相对于`abcd`的偏移是1。

### 示例二

**输入：**
```text
aabcdefg
b[cd]d[eg]
```

**输出：**
```text
2
```

**说明：**  

## 解题思路

**基本思路：** 使用`re`包的`search`函数解题。

1. 使用`re.search`在`haystack`中查找`needle`。
2. 如果找到，则使用`start()`方法，返回首次查到的字符串位置。
3. 如果没有找到，则返回-1。

## 解题代码
```python
import re


def solve_method(haystack, needle):
    match = re.search(needle, haystack)
    return match.start() if match else -1


if __name__ == '__main__':
    assert solve_method("abcd", "b[cd]") == 1
    assert solve_method("aabcdefg", "b[cd]d[eg]") == 2
```