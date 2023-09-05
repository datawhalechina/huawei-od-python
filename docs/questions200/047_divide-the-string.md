# 047 划分字符串

## 题目描述

给定一个小写字母组成的字符串`s`，请找出字符串中两个不同位置的字符作为分割点，使得字符串分成的三个连续子串且子串权重相等，注意子串不包含分割点。

若能找到满足条件的两个分割点，请输出这两个分割点在字符串中的位置下标，若不能找到满足条件的分割点请返回`0,0`。

子串权重计算方式为：子串所有字符的`ASCII`码数值之和。

## 输入描述

输入为一个字符串，字符串由`a~z`，26个小写字符组成，字符串长度的取值范围是5 <= 字符串长度 <= 200。

## 输出描述

输出为两个分割点在字符串中的位置下标，以逗号分隔。

**补充说明：**

只考虑唯一解，不存在一个输入多种输出解的情况。

## 示例描述

### 示例一

**输入：**
```text
acdbbbca
```

**输出：**
```text
2,5
```

**说明：**  

以位置2和5作为分割点，将字符串分割为`ac`、`bb`、`ca`三个子串，每一个的子串权重都为196，输出为：`2,5`。

### 示例二

**输入：**
```text
abcabc
```

**输出：**
```text
0,0
```

**说明：**  

找不到符合条件的分割点，输出为`0,0`。

## 解题思路

**基本思路：** 使用双指针求解。
1. 初始化两个指针`left`和`right`分别指向字符串的第二个字符和倒数第二个字符（字符串长度至少为5，说明子串权重需要大于0，所以`left`和`right`初始化时指向正数和倒数第二个字符）。
2. 初始化被分隔的子串权重：左边子串`sum_left`、右边子串`sum_right`。
3. 使用`while`循环，遍历字符串：
   - 计算中间子串的权重`sum_middle`。
   - 若权重相等，找到满足条件的分割点。
   - 若左子串的权重大于右子串的权重，右指针向左移动。
   - 若左子串的权重小于右子串的权重，左指针向右移动。
   - 如果左右子串的权重相等，同时移动左右指针。  
4. 如果遍历完整个字符串，仍未找到满足条件的两个分割点，那么输出`0,0`。

## 解题代码
```python
def solve_method(s):
    n = len(s)
    left, right = 1, n - 2
    sum_total = sum(ord(c) for c in s)
    sum_left = ord(s[0])
    sum_right = ord(s[n - 1])
    while left < right:
        sum_middle = sum_total - sum_left - sum_right - ord(s[left]) - ord(s[right])
        if sum_left == sum_middle == sum_right:
            return f"{left},{right}"
        if sum_left > sum_right:
            sum_right += ord(s[right])
            right -= 1
        elif sum_left < sum_right:
            sum_left += ord(s[left])
            left += 1
        else:
            sum_left += ord(s[left])
            sum_right += ord(s[right])
            left += 1
            right -= 1
    return "0,0"


if __name__ == '__main__':
    assert solve_method("acdbbbca") == "2,5"
    assert solve_method("abcabc") == "0,0"
```