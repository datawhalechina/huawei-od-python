# 291 最多提取子串数目

## 题目描述

给定由26个英文小写字母[a-z]组成的字符串`A`和`B`，其中`A`中可能存在重复字母，`B`中不会存在重复字母。现从字符串`A`中按规则挑选一些字母，可以组成字符串`B`。

挑选规则如下：
1. 同一个位置的字母只能被挑选一次。
2. 被挑选字母的相对先后顺序不能改变。

求最多可以同时从`A`中挑选多少组能组成`B`的字符串。

## 输入描述

输入为2行，第1行输入字符串`A`，第2行输入字符串`B`，行首行尾无多余空格。其中`A`、`B`均由26个英文小写字母[a-z]组成。

- 字符串`A`满足`0 < A.length < 100`，`A`中可能包含重复字母。
- 字符串`B`满足`0 < B.length < 10`，`B`中不会出现重复字母。

## 输出描述

输出1行，包含1个数字，表示最多可以同时从`A`中挑选多少组能组成`B`的字符串，行末无多余空格。

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

**说明：**  

从字符串`A`(`badc`)中可以按字母相对先后顺序取出字符串`B`(`bac`)。

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
**说明：**  

从字符串`A`(`badc`)中无法按字母相对先后顺序取出字符串`B`(`abc`)。

### 示例三

**输入：**
```text
aabbcxd
abcd
```

**输出：**
```text
1
```

**说明：**  

从字符串`A`(`aabbcxd`)中挑选一组`B`(`abcd`)后，`A`中剩余字符串为`abx`，无法再挑出`abcd`。

### 示例四

**输入：**
```text
ababcecfdc
abc
```

**输出：**
```text
2
```

**说明：** 

按如下步骤（步骤不唯一），可以同时从字符串`A`(`ababcecfdc`)中最多取出两个`B`(`abc`)，其中粗体标注的是每步提取的字母：

**ab**ab**c**ecfdc -> **ab**e**c**fdc

剩余的`efdc`无法继续提取`abc`，结果为2。

### 示例五
**输入：**
```text
aaa
a
```

**输出：**
```text
3
```

**说明：**

从字符串`A`(`aaa`)中可以挑选3个字符串`B`(`a`)。

## 解题思路

1. 初始化标记A的字母是否被使用的数组`exist`。
2. 初始化一个标记，表示是否已经找到了一个字符串B。
3. 循环获取字符串B：
    - 如果A中的字母没有被使用，与B中的字母匹配。
    - 如果已经匹配上，则标记A中的字母已经被使用。
    - 如果找到了一个字符串B，统计次数加1。
4. 返回统计结果。

## 解题代码

```python
def solve_method(A: str, B: str) -> int:
    result = 0
    # 标记A的字母是否被使用
    exist = [True for _ in range(len(A))]
    # 是否已经找到了一个字符串B
    flag = True
    while flag:
        flag = False
        ib = 0
        for ia in range(len(A)):
            if exist[ia]:
                # 如果A中的字母没有被使用，与B中的字母匹配
                if A[ia] == B[ib]:
                    ib += 1
                    # 标记A中的字母已经被使用
                    exist[ia] = False
                ia += 1

            if ib == len(B):
                # 如果找到了一个字符串B，统计次数
                result += 1
                flag = True
                break
    return result


if __name__ == '__main__':
    assert solve_method("badc", "bac") == 1
    assert solve_method("badc", "abc") == 0
    assert solve_method("aabbcxd", "abcd") == 1
    assert solve_method("ababcecfdc", "abc") == 2
    assert solve_method("aaa", "a") == 3
```