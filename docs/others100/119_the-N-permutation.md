## 119 第N个排列

## 题目描述

给定参数`n`，从1到n有n个整数`1,2,3,...n`，这n个数字共有`n!`种排列，按大小顺序升序列出所有排列情况，并一一标记。

当`n = 3`时，所有排列如下：

`123, 132, 213, 231, 312, 321`

给定`n`和`k`，返回第`k`个排列。

## 输入描述

第一行是`n`，表示整数的范围。

第二行是`k`，表示需要获取的第`k`个位置上的数。取值范围是`1 ~ n!`。

## 输出描述

输出排序为第`k`位置的数字。

## 示例描述

### 示例一

**输入：**

```text
3
3
```

**输出：**

```text
213
```

### 示例二

**输入：**

```text
2
2
```

**输出：**

```text
21
```

## 解题思路

**基本思路：** 使用`itertools`的`permutations`函数，来生成排列。

1. 生成从1~n的数列`arr`。
2. 使用`itertools`的`permutations`函数生成`arr`的全排列。
3. 获取全排列中第`k`个位置的排列。
4. 将该排列表示成整数，并返回结果。

## 解题代码

```python
import itertools


def solve_method(n, k):
    arr = [i + 1 for i in range(n)]
    perms = list(itertools.permutations(arr))
    result = int("".join(str(x) for x in perms[k - 1]))
    return result


if __name__ == '__main__':
    assert solve_method(3, 3) == 213
    assert solve_method(2, 2) == 21
```

