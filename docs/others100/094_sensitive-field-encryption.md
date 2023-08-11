# 094 敏感字段加密

## 题目描述

给定一个由多个命令字组成的命令字符串：

1. 字符串长度小于等于127字节，只包含大小写字母、数字、下划线和偶数个双引号。
2. 命令字之间以一个或多个下划线_进行分割。
3. 可以通过两个双引号`""`来标识包含下划线`_`的命令字或空命令字（仅包含两个双引号的命令字），双引号不会在命令字内部出现。

请对指定索引的敏感字段进行加密，替换为`******`(6个`*`)，并删除命令字前后多余的下划线_。如果无法找到指定索引的命令字，输出字符串`ERROR`。

## 输入描述

输入为两行，第一行是命令字索引`K`(从0开始)，第二行是命令字符串`S`。

## 输出描述

输出处理后的命令字符串，如果无法找到指定索引的命令字，输出字符串`ERROR`。

## 示例描述

### 示例一

**输入：**
```text
1
password__a12345678_timeout_100
```

**输出：**
```text
password_******_timeout_100
```

### 示例二

**输入：**
```text
2
aaa_password_"al2_45678"_timeout__100_""_
```

**输出：**
```text
aaa_password_"******"_timeout_100_""
```

## 解题思路

1. 初始化双引号计数器`quote_count`，用于判断是否在双引号内部
2. 遍历字符串：
   - 遇到第一个双引号，双引号计数器加1。
   - 遇到第二个双引号，将命令字存入列表中，并将当前命令字清空。
   - 遇到下划线、且当前命令字不为空、且不在双引号内部，判断双引号计数器，如果为2则还原成0，将命令字存入列表中，并将当前命令字清空。
   - 遇到非下划线字符，或当前命令字为空且字符不为下划线，或当前命令中包含一个双引号，将当前字符添加到当前命令字中。
3. 将最后一个命令字添加到命令列表。
4. 对第`k`个命令字进行替换，用`_`拼接，返回结果。

## 解题代码

```python
def solve_method(k, string):
    commands = []
    command = ""
    # 双引号计数器，用于判断是否在双引号内部
    quote_count = 0
    for ch in string:
        if ch == '"' and quote_count != 1:
            # 遇到第一个双引号
            command += ch
            quote_count += 1
        elif ch == '"' and quote_count == 1:
            # 遇到第二个双引号
            quote_count += 1
            command += ch
            commands.append(command)
            command = ""
        elif ch == '_' and command != "" and quote_count != 1:
            #  遇到下划线，当前命令字不为空，不在双引号内部
            if quote_count == 2:
                quote_count = 0
            commands.append(command)
            command = ""
        elif (command == "" and ch != "_") or ('"' in command) or ch != "_":
            # 遇到非下划线字符，或当前命令字为空且字符不为下划线，或当前命令中包含一个双引号
            command += ch

    if command != "":
        # 将最后一个命令字添加到命令列表
        commands.append(command)

    if k < len(commands):
        commands[k] = "******" if '"' not in commands[k] else '"******"'
        return "_".join(commands)
    else:
        return "ERROR"


if __name__ == '__main__':
    assert solve_method(1, "password__a12345678_timeout_100") == "password_******_timeout_100"
    assert solve_method(2, 'aaa_password_"al2_45678"_timeout__100_""_') == 'aaa_password_"******"_timeout_100_""'
```