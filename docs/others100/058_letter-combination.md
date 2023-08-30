# 058 字母组合

## 题目描述

每个数字对应多个字母，对应关系如下:
```text
0: a,b,c
1: d,e,f
2: g,h,i
3: j,k,l
4: m,n,o
5: p,q,r
6: s,t
7: u,v
8: w,x
9: y,z
```

输入一串数字后，通过数字和字母的对应关系可以得到多个字母字符串（要求按照数字的顺序组合字母字符串）。

屏蔽字符：屏蔽字符中的所有字母不能同时在输出的字符串出现，如屏蔽字符是`abc`，则要求字符串中不能同时出现`a,b,c`，但是允许同时出现`a,b`、`a,c`、`b,c`等。

给定一个数字字符串和一个屏蔽字符串，输出所有可能的字符组合。

例如，输入数字字符串`78`和屏蔽字符串`ux`，输出结果为`uw,vw,vx`。数字字符串`78`，可以得到如下字符串：`uw`、`ux`、`vw`、`vx`。由于`ux`是屏蔽字符串，因此排除`ux`，最终的输出是`uw,vw,vx`。

## 输入描述

第一行是一串数字字符串，数字字符串中的数字不允许重复，数字字符串的长度大于0，小于等于5。

第二行是屏蔽字符，屏蔽字符的长度一定小于数字字符串的长度，屏蔽字符串中字符不会重复。

## 输出描述

输出可能的字符串组合。

注：字符串之间使用`,`隔开，最后一个字符串后可携带逗号。

## 示例描述

### 示例一

**输入：**

```text
78
ux
```

**输出：**

```text
uw,vw,vx
```

### 示例二

**输入：**

```text
78
x
```

**输出：**

```text
uw,vw
```

## 解题思路

1. 得到数字与字母的映射列表`words`。
2. 得到各列表之间的笛卡尔积`result`。
3. 使用屏蔽词，过滤结果列表`result`。
4. 返回结果列表。

## 解题代码

```python
import itertools

# 定义数字到字母的映射
digits_mapping = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"],
    ["p", "q", "r"],
    ["s", "t"],
    ["u", "v"],
    ["w", "x"],
    ["y", "z"]
]


def solve_method(nums, block_words):
    nums = list(nums)
    words = [set(digits_mapping[int(num)]) for num in nums]
    # 得到各列表之间的笛卡尔积
    result = list(itertools.product(*words))

    result = ["".join(x) for x in result if block_words not in "".join(x)]
    result.sort()
    return result


if __name__ == "__main__":
    assert solve_method("78", "ux") == ["uw", "vw", "vx"]
    assert solve_method("78", "x") == ["uw", "vw"]
```



