# 044 获取最大软件版本号

## 题目描述

Maven版本号定义，`<主版本>.<次版本>.<增量版本>-<里程碑版本>`。

举例`3.1.4-beta`，其中主版本和次版本都是必须的，主版本、次版本、增量版本由多位数字组成，可能包含前导零，里程碑版本由字符串组成。

按照以下规则进行比较：
- `<主版本>.<次版本>.<增量版本>`：基于数字比较。
- `里程碑版本`：基于字符串比较，采用字典序。
- 比较版本号时，按从左到右的顺序依次比较。
- 基于数字比较，只需比较忽略任何前导零后的整数值。

输入2个版本号，输出最大版本号。

## 输入描述

输入2个版本号，换行分隔，每个版本的最大长度小于50。  

主版本、次版本、增量版本：基于数字比较，比如`1.5 > 1.4 > 1.3.11 > 1.3.9`。

里程碑版本：基于字符串比较，比如`1.2-beta-3 > 1.2-beta-11`。

## 输出描述

版本号相同时，输出第一个输入版本号。

## 示例描述

### 示例一

**输入：**
```text
2.5.1-C
1.4.2-D
```

**输出：**
```text
2.5.1-C
```

**说明：**  

主版本，数字2大于1。

### 示例二

**输入：**
```text
1.3.11-S2
1.3.11-S13
```

**输出：**
```text
1.3.11-S2
```

**说明：**  

里程碑版本，`S2`大于`S13`。

### 示例三
**输入：**
```text
1.05.1
1.5.01
```

**输出：**
```text
1.05.1
```

**说明：**  

版本号相同，输出第一个版本号。

### 示例四
**输入：**
```text
1.5
1.5.0
```

**输出：**
```text
1.5.0
```

**说明：**  

主次相同，存在增量版本大于不存在。

### 示例五

**输入：**
```text
1.5.1-A
1.5.1-a
```

**输出：**
```text
1.5.1-a
```

**说明：**  

里程碑版本号，字符串比较`a`大于`A`。

## 解题思路

1. 使用正则表达式，获取主版本、次版本、增量版本、里程碑版本。
2. 按数值比较主版本。
3. 按数值比较次版本。   
4. 按数值比较增量版本。   
5. 按字典序比较里程碑版本。   
6. 如果上述条件都相等，则输出第一个版本。

## 解题代码

```python
import re


def solve_method(version1: str, version2: str) -> str:
    pattern = r"^(\d+)(?:\.(\d+))(?:\.(\d+))?(?:\-(.+))?$"

    major1, minor1, patch1, mile1 = re.findall(pattern, version1)[0]
    major2, minor2, patch2, mile2 = re.findall(pattern, version2)[0]

    # 比较主版本，按照数值比较
    if major1 != major2:
        return version1 if int(major1) > int(major2) else version2

    # 比较次版本，按照数值比较
    if int(minor1) != int(minor2):
        return version1 if int(minor1) > int(minor2) else version2

    # 比较增量版本，按照数值比较
    if patch1 != "" and patch2 != "":
        if int(patch1) > int(patch2):
            return version1
        elif int(patch1) < int(patch2):
            return version2
    elif patch1 != "" and patch2 == "":
        return version1
    elif patch1 == "" and patch2 != "":
        return version2

    # 比较里程碑，按照字典序比较
    if mile1 != "" and mile2 != "":
        if mile1 > mile2:
            return version1
        elif mile1 < mile2:
            return version2
    elif mile1 != "" and mile2 == "":
        return version1
    elif mile1 == "" and mile2 != "":
        return version2

    return version1


if __name__ == '__main__':
    assert solve_method("2.5.1-C", "1.4.2-D") == "2.5.1-C"
    assert solve_method("1.3.11-S2", "1.3.11-S13") == "1.3.11-S2"
    assert solve_method("1.05.1", "1.5.01") == "1.05.1"
    assert solve_method("1.5", "1.5.0") == "1.5.0"
    assert solve_method("1.5.1-A", "1.5.1-a") == "1.5.1-a"
```