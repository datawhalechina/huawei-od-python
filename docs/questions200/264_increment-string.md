# 264 递增字符串

## 题目描述

定义字符串完全由'A'和'B'组成，当然也可以全是'A'或全是'B'。如果字符串从前往后都是以字典序排列的，那么我们称之为严格递增字符串。

给出一个字符串s，允许修改字符串中的任意字符，即可以将任何的'A'修改成'B'，也可以将任何的'B'修改成'A'，求可以使s满足严格递增的最小修改次数。`0＜s．length＜100000`。

## 输入描述

输入一个字符串："AABBA"

## 输出描述

输出：1

修改最后一位得到AABBB。

## 示例描述

### 示例一

**输入：**
```text
AABBA
```

**输出：**
```text
1
```

## 解题思路

**基本思路：**
- 如果当前字符为A，需要保证前面的所有B都被修改成A（找到A最后一次出现的位置）
- 如果当前字符为B，需要保证后面的所有A都被修改成B（找到B第一次出现的位置）

**代码思路：**
1. 找到A最后一次出现的位置`A_last_index`，计算`A_last_index`前的B出现的次数
2. 找到B第一次出现的位置`B_first_index`，计算`B_first_index`后的A出现的次数
3. 取较小值

## 解题代码
```python
def solve_method(str):
    count1 = 0
    A_last_index = str.rfind("A")
    for i in range(A_last_index):
        if str[i] == "B":
            count1 += 1

    count2 = 0
    B_first_index = str.find("B")
    for i in range(B_first_index, len(str)):
        if str[i] == "A":
            count2 += 1
    return min(count1, count2)

if __name__ == "__main__":
    # AABBA
    str = input().strip()
    print(solve_method(str))

    assert solve_method("AABBA") == 1
```