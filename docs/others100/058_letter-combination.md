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

**基本思路：**

深度优先搜索，把所有组合都找出来，然后排除掉包含所有屏蔽字符的组合

## 解题代码

```python
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

# 结果列表
res = []


# 主解决方法
def solve_method():
    num_str = input("请输入数字字符串：")
    no_contain = input("请输入不包含的字符：")
    method(0, num_str, no_contain, "")
    print(",".join(res))


def method(index, num_str, no_contain, temp):
    # 检查临时字符串的长度是否与数字字符串的长度相同
    if len(temp) == len(num_str):
        # 如果长度相同，则检查临时字符串是否不包含指定的字符
        if is_true(no_contain, temp):
            # 如果临时字符串通过检查，则将其添加到结果列表中
            res.append(temp)
    else:
        # 如果临时字符串的长度与数字字符串的长度不相同，则继续构建临时字符串

        # 从数字字符串中获取当前索引的数字，将其转换为digits_mapping列表的索引
        digits_index = int(num_str(index))

        # 使用上一行中计算的索引从digits_mapping列表中获取字符列表
        chars = digits_mapping[digits_index]

        # 对于字符列表中的每个字符，执行以下操作
        for i in range(len(chars)):
            # 递归调用method函数，增加索引并将当前字符添加到临时字符串中
            # 这将继续构建临时字符串，直到其长度与数字字符串的长度相同
            method(index + 1, num_str, no_contain, temp)


# 检查生成的字符串是否不包含指定的字符
def is_true(no_contain, s):
    for c in no_contain:
        if c not in s:
            return True
    return False


# 主程序入口
if __name__ == "__main__":
    solve_method()
```



