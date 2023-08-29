# 061 字符串摘要

## 题目描述

给定一个字符串的摘要算法，请输出给定字符串的摘要值。规则如下：

1. 去除字符串中非字母的符号。
2. 如果出现连续字符（不区分大小写），则输出：该字符（小写） + 连续出现的次数。
3. 如果是非连续的字符（不区分大小写），则输出：该字符（小写） + 该字母之后字符串中出现的该字符的次数。
4. 对按照以上方式表示后的字符串进行排序：字母和紧随的数字作为一组进行排序，数字大的在前，数字相同的，则按字母进行排序，字母小的在前。

## 输入描述

一行字符串，长度为[1,200]。

## 输出描述

摘要字符串。

## 示例描述

### 示例一

**输入：**
```text
aabbcc
```

**输出：**
```text
a2b2c2
```

### 示例二

**输入：**
```text
bAaAcBb
```

**输出：**
```text
a3b2b2c0
```

**说明：**

根据输入`bAaAcBb`：

- 第一个`b`非连续字母，该字母之后字符串中还出现了2次（最后的两个`bb`），所以输出`b2`。
- `a`连续出现3次，输出`a3`。
- `c`非连续，该字母之后字符串再没有出现过c，输出`c0`。
- `Bb`连续2次，输出`b2`。

对`b2a3c0b2`进行排序，最终输出`a3b2b2c0`。

## 解题思路

1. 初始化结果列表`result`。
2. 遍历字符串：
    - 如果只剩一个字符，则将该字符+0存入结果列表中。
    - 如果是连续字符，统计相同字符出现次数，将该字符+出现次数存入结果列表中。
    - 如果是非连续字符，统计后续字符出现次数，将该字符+出现次数存入结果列表中。
3. 将结果列表按照数字从大到小、字符按字典序排序。
4. 返回结果列表。

## 解题代码

```python
def solve_method(s):
    n = len(s)
    index = 0
    result = []
    s = s.lower()

    while index < n:
        if index == n - 1:
            result.append(s[index] + "0")
        if s[index] == s[index + 1]:
            # 如果是连续字符
            start, index = index, index + 1
            # 统计相同字符出现次数
            while index < n - 1 and s[index] == s[index + 1]:
                index += 1
            freq = index - start + 1
            result.append(s[start] + str(freq))
            index += 1
        else:
            # 如果是非连续字符
            freq = s.count(s[index], index + 1, n)
            result.append(s[index] + str(freq))
            index += 1
    # 将结果列表按照数字从大到小、字符按字典序排序
    result.sort(key=lambda x: (-int(x[1]), x[0]))
    return "".join(result)


if __name__ == '__main__':
    assert solve_method("aabbcc") == "a2b2c2"
    assert solve_method("bAaAcBb") == "a3b2b2c0"
```

