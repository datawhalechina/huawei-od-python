# 274 对称美学

## 题目描述

对称就是最大的美学，现有一道关于对称字符串的美学。

已知：
- 第1个字符串：R
- 第2个字符串：BR
- 第3个字符串：RBBR
- 第4个字符串：BRRBRBBR
- 第5个字符串：RBBRBRRBBRRBRBBR

相信你已经发现规律了，没错！就是第`i`个字符串=第`i-1`个字符串的取反 + 第`i-1`个字符串，其中取反是R->B、B->R。

现在告诉你`n`和`k`，让你求得第`n`个字符串的第`k`个字符是多少。（`k`的编号从0开始）

## 输入描述

第一行输入一个T，表示有T组用例，接下来输入T行，每行输入两个数字表示`n`和`k`，其中各个输入值满足以下条件：
- 1 <= T <= 100
- 1 <= n <= 64
- 0 <= k < 2^(n-1)

## 输出描述

输出T行对应的答案，输出`blue`表示字符是B，输出`red`表示字符是R。

## 示例描述

### 示例一

**输入：**
```text
5
1 0
2 1
3 2
4 6
5 8
```

**输出：**
```text
red
red
blue
blue
blue
```

**说明：**  
- 第1个字符串：R -> 第0个字符为R 
- 第2个字符串：BR -> 第1个字符为R
- 第3个字符串：RBBR -> 第2个字符串为B
- 第4个字符串：BRRBRBBR -> 第6个字符串为B
- 第5个字符串：RBBRBRRBBRRBRBBR -> 第8个字符串为B

### 示例二

**输入：**
```text
1
64 73709551616
```

**输出：**
```text
red
```

## 解题思路

1. 经过观察，可以采用递归法解题
    - 如果查找的位置`k`在后半段，则对应上一个字符串的位置为本层字符串长度减去该位置，即`prev_pos = k - half_len`。
    - 如果查找的位置`k`在前半段，则对应上一个字符串的位置的取反。
2. 编写递归函数`get_color`，当第1个字符串时，返回R，当第2个字符串时，获取对应位置，如果是第n个字符串，按照递归思路编写代码。
3. 写出字符映射，R->red、B->blue。
4. 根据得到的字符，结合字符映射，返回结果。

## 解题代码

```python
def get_color(n, k):
    if n == 1:
        return "R"
    elif n == 2:
        return "B" if k == 0 else "R"

    half_len = 2 ** (n - 1)
    if k >= half_len:
        # 在后半段，要查找的位置等于上一个字符串的相应位置
        prev_pos = k - half_len
        return get_color(n - 1, prev_pos)
    else:
        # 在前半段，要查找的位置等于上一个字符串的相应位置取反
        return "B" if get_color(n - 1, k) == "R" else "R"


def solve_method(T):
    color_map = {"R": "red", "B": "blue"}
    result = []
    for t in T:
        n, k = t[0], t[1]
        # 将R转换成red，将B转换成blue
        result.append(color_map[get_color(n, k)])

    return result
```