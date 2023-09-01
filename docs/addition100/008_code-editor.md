# 008 代码编辑器

## 题目描述

某公司为了更高效的编写代码，邀请你开发一款代码编辑器程序。程序的输入为已有的代码文本和指令序列，程序需输出编辑后的最终文本。指针初始位置位于文本的开头。

支持的指令（`X`为大于等于0的整数，`word`为无空格的字符串）：

- `FORWARD X`：指针向前（右）移动`X`，如果指针移动位置超过了文本末尾，则将指针移动到文本末尾。
- `BACKWARD X`：指针向后（左）移动`X`，如果指针移动位置超过了文本开头，则将指针移动到文本开头。
- `SEARCH-FORWARD word`：从指针当前位置向前查找`word`，并将指针移动到`word`的起始位置，如果未找到则保持不变。
- `SEARCH-BACKWARD word`：在文本中向后查找`word`，并将指针移动到`word`的起始位置，如果未找到则保持不变。
- `INSERT word`：在指针当前位置前插入`word`，并将指针移动到`word`的结尾。
- `REPLACE word`：在指针当前位置替换并插入字符（删除原有字符，并增加新的字符）。
- `DELETE X`：在指针位置删除`X`个字符。

## 输入描述

输入的第一行是命令列表的长度`K`。

输入的第二行是文件中的原始文本。

接下来的`K`行，每行是一个指令。

## 输出描述

编辑后的最终结果。

**说明：**

文本最长长度不超过256K。

## 示例描述

### 示例一

**输入：**
```text
1
ello
INSERT h
```

**输出：**
```text
hello
```

**说明：**  

在文本开头插入。

### 示例二

**输入：**
```text
2
hllo
FORWARD 1
INSERT e
```

**输出：**
```text
hello
```

**说明：**  

在文本的第一个位置插入。

### 示例三

**输入：**
```text
2
hell
FORWARD 1000
INSERT o
```

**输出：**
```text
hello
```

**说明：** 

在文本的结尾插入。

### 示例四

**输入：**
```text
1
hello
REPLACE HELLO
```

**输出：**
```text
HELLO
```

**说明：** 

进行替换操作。

### 示例五

**输入：**
```text
1
hello
REPLACE HELLO_WORLD
```

**输出：**
```text
HELLO_WORLD
```

**说明：**

超过文本长度替换。

### 示例六

**输入：**
```text
2
hell
FORWARD 10000
REPLACE O
```

**输出：**
```text
hellO
```

**说明：**

超出文本长度替换。

## 解题思路

1. 将字符串转换为列表形式`result`。
2. 遍历所有操作指令：
    - 如果是`FORWARD X`指令，指针向前（右）移动`X`，如果指针移动位置超过了文本末尾，则将指针移动到文本末尾。
    - 如果是`BACKWARD X`指令，指针向后（左）移动`X`，如果指针移动位置超过了文本开头，则将指针移动到文本开头。
    - 如果是`SEARCH-FORWARD word`指令，从指针当前位置向前查找`word`，并将指针移动到`word`的起始位置，如果未找到则保持不变。
    - 如果是`SEARCH-BACKWARD word`指令，在文本中向后查找`word`，并将指针移动到`word`的起始位置，如果未找到则保持不变。
    - 如果是`INSERT word`指令，在指针当前位置前插入`word`，并将指针移动到`word`的结尾。
    - 如果是`REPLACE word`指令，在指针当前位置替换并插入字符（删除原有字符，并增加新的字符）。
    - 如果是`DELETE X`指令，在指针位置删除`X`个字符。
3. 返回结果，拼接`result`列表，得到字符串。

## 解题代码

```python
def solve_method(code, ops):
    result = list(code)

    index = 0
    for op in ops:
        operation, value = op.split()
        if operation == "FORWARD":
            # 指针向前（右）移动X
            index = min(index + int(value), len(result))
        elif operation == "BACKWARD":
            # 指针向后（左）移动X
            index = max(index - int(value), 0)
        elif operation == "SEARCH-FORWARD":
            # 从指针当前位置向前查找word，并将指针移动到word的起始位置
            _index = code.rfind(value, 0, index)
            if _index != -1:
                index = _index
        elif operation == "SEARCH-BACKWARD":
            # 在文本中向后查找word，并将指针移动到word的起始位置
            _index = code.find(value, index)
            if _index != -1:
                index = _index
        elif operation == "INSERT":
            # 在指针当前位置前插入word，并将指针移动到word的结尾
            result.insert(index, value)
            index += len(value)
        elif operation == "REPLACE":
            # 在指针当前位置替换并插入字符
            result[index: index + len(value)] = value
        elif operation == "DELETE":
            del result[index: index + int(value)]

    return "".join(result)


if __name__ == '__main__':
    ops = ["INSERT h"]
    assert solve_method("ello", ops) == "hello"

    ops = ["FORWARD 1", "INSERT e"]
    assert solve_method("hllo", ops) == "hello"

    ops = ["FORWARD 1000", "INSERT o"]
    assert solve_method("hell", ops) == "hello"

    ops = ["REPLACE HELLO"]
    assert solve_method("hello", ops) == "HELLO"

    ops = ["REPLACE HELLO_WORLD"]
    assert solve_method("hello", ops) == "HELLO_WORLD"

    ops = ["FORWARD 10000", "REPLACE O"]
    assert solve_method("hell", ops) == "hellO"
```