# 014 五键键盘

## 题目描述

有一个特殊的五键键盘，上面有`A`、`Ctrl-C`、`Ctrl-X`、`Ctrl-V`、`Ctrl-A`。
- `A`键在屏幕上输出一个字母`A`。
- `Ctrl-C`将当前所选的字母复制到剪贴板。
- `Ctrl-X`将当前选择的字母复制到剪贴板并清空所选择的字母。
- `Ctrl-V`将当前剪贴板的字母输出到屏幕。
- `Ctrl-A`选择当前屏幕中所有字母。

注意：
1. 剪贴板初始为空。
2. 新的内容复制到剪贴板会覆盖原有内容。
3. 当屏幕中没有字母时，`Ctrl-A`无效。
4. 当没有选择字母时，`Ctrl-C`、`Ctrl-X`无效。
5. 当有字母被选择时，`A`和`Ctrl-V`这两个输出功能的键，会先清空所选的字母再进行输出。

给定一系列键盘输入，输出最终屏幕上字母的数量。

## 输入描述

输入为一行，为简化解析用数字`12345`分别代替`A`、`Ctrl-C`、`Ctrl-X`、`Ctrl-V`、`Ctrl-A`的输入，数字用空格分隔。

## 输出描述

输出一个数字为屏幕上字母的总数量。

## 示例描述

### 示例一

**输入：**
```
1 1 1
```

**输出：**
```
3
```

### 示例二

**输入：**
```
1 1 5 1 5 2 4 4
```

**输出：**
```
2
```

## 解题思路

1. 初始化结果字符串`result`、选择字符串`select`、拷贝在剪贴板的字符串`copy`。
2. 遍历键盘输入：
    - 当操作为1时，当有字母被选择时，清空选择的字母，将`A`存入结果字符串中。
    - 当操作为2时，将当前所选的字母`select`复制到剪贴板的字符串`copy`中。
    - 当操作为3时，将当前选择的字母`select`复制到剪贴板`copy`，使用`replace`方法清空所选择的字母。
    - 当操作为4时，将当前剪贴板的字母`copy`存入到结果字符串中。
    - 当操作为5时，选择当前屏幕中所有字母，将`select`设置为结果字符串。
3. 返回结果字符串的长度。

## 解题代码

```python
def clear(result, select):
    if select != "":
        result = result.replace(select, "")
        select = ""
    return select, result


def solve_method(ops):
    result = ""
    select = ""
    copy = ""
    for op in ops:
        if op == 1:
            select, result = clear(result, select)
            result += "A"
        elif op == 2:
            if select != "":
                copy = select
        elif op == 3:
            if select != "":
                copy = select
                result = result.replace(select, "")
                select = ""
        elif op == 4:
            select, result = clear(result, select)
            result += copy
        elif op == 5:
            if result != "":
                select = result

    return len(result)


if __name__ == '__main__':
    assert solve_method([1, 1, 1]) == 3
    assert solve_method([1, 1, 5, 1, 5, 2, 4, 4]) == 2
```

