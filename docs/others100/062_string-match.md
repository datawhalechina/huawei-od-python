# 062 字符匹配

## 题目描述

给你一个字符串数组和一个字符规律：
- 字符串数组中每个字符串均由小写字母组成。
- 字符规律由小写字母以及`.`和`*`组成。

识别字符串数组中哪些字符串可以匹配到字符规律上。`.`匹配任意单个字符，`*`匹配0个或多个任意字符，判断字符串是否匹配，是要涵盖整个字符串的而不是部分字符串。

## 输入描述

第一行是空格分隔的多个字符串，取值范围是1 < 单个字符串长度 < 100、1 <= 字符串个数 < 100。
  
第二行为字符规律，取值范围是1 <= 字符规律长度 <= 50，不需要考虑异常场景。

## 输出描述

匹配的字符串在数组中的下标（从0开始）。多个匹配时，下标升序，并用`,`分隔，若均不匹配，则输出-1。

## 示例描述

### 示例一

**输入：**
```text
ab aab abacd
.*
```

**输出：**
```text
0,1,2
```

### 示例二

**输入：**
```text
ab aab
a.b
```

**输出：**
```text
1
```

## 解题思路

1. 遍历字符串列表：
    - 初始化前一个字符`prev`，用于匹配后续字符。
    - 遍历字符规律的表达式的每个字符：
        - 如果字符是`.`，则删除第一个字符，并将`prev`设置为`.`。
        - 如果字符是`*`，使用`while`循环操作字符串：
          - 如果`prev`是`.`，则持续删除字符。
          - 如果`prev`是字母，则连续删除相同的字母，直到不相同时，跳出`while`循环。
        - 如果是单个字符，则保存该字符作为后续字符匹配，如果不匹配，则不添加到结果列表中。
    - 如果全部匹配完，则将该字符串所在的索引添加到结果列表中。
2. 返回结果列表。    

## 解题代码

```python
def solve_method(arr, pattern):
    def check(chars):
        i = 0
        chars = list(chars)
        prev = chars[0]
        while i < len(pattern):
            if len(chars) == 0:
                break
            if pattern[i] == ".":
                chars.pop(0)
                prev = "."
            elif pattern[i] == "*":
                # 如果连续相同字符，或者前一个字符是点号，则一直删除，直到不满足条件
                while len(chars) != 0 and (prev in [chars[0], "."]):
                    chars.pop(0)
            else:
                if chars[0] == pattern[i]:
                    # 如果是单个字符，则保存该字符作为后续字符匹配
                    prev = chars.pop(0)
                else:
                    return False
            i += 1

        if len(chars) == 0 and i == len(pattern):
            return True

        return False

    result = []
    for index, s in enumerate(arr):
        if check(s):
            result.append(index)
    return result


if __name__ == '__main__':
    arr = ["ab", "aab", "abacd"]
    assert solve_method(arr, ".*") == [0, 1, 2]

    arr = ["ab", "aab"]
    assert solve_method(arr, "a.b") == [1]

    arr = ["bab", "baaa"]
    assert solve_method(arr, "ba*") == [1]
```

