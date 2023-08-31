# 046 递增字符串

## 题目描述

定义字符串完全由`A`和`B`组成，当然也可以全是`A`或全是`B`。如果字符串从前往后都是以字典序排列的，那么我们称之为严格递增字符串。

给出一个字符串`s`，允许修改字符串中的任意字符，即可以将任何的`A`修改成`B`，也可以将任何的`B`修改成`A`，求可以使`s`满足严格递增的最小修改次数，取值范围是0 < s.length < 100000。

## 输入描述

输入一个字符串如`AABBA`

## 输出描述

输出为1，修改最后一位得到`AABBB`。

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

题目要求`最小修改次数`，考虑最终的结果以`i`为分界点，`i`前全是`A`，`i`后全是`B`。

假设字符串位置`[0, i]`存在`count_A`个`A`。
- 将区间`[0, i]`全部转成`A`，计算需要修改的次数，即求该区间内`B`的个数等于`i+1-count_A`。
- 将区间`[i+1, end]`全部转为`B`，计算需要的修改次数，即求该区间内`A`的个数等于`total_A-count_A`。

**代码思路：**

1. 记录`A`出现的总次数`total_A`。
2. 初始化最小修改次数`res`。
3. 遍历所有字母：
    - 计算`i`前面包含`A`的个数`count_A`。
    - 计算在区间`[0, i]`将`B`全部转成`A`的修改次数`count_before_i`。
    - 计算在区间`[i+1, len(chars)]`将`A`全部转为`B`的修改次数`count_after_i`。
    - 计算`res`和`count_before_i + count_after_i`的最小值。  
4. 返回结果，即最小修改次数。

## 解题代码
```python
def solve_method(chars):
    total_A = chars.count("A")
    res = total_A
    count_A = 0
    for i in range(len(chars)):
        if chars[i] == "A":
            count_A += 1
        # 将区间[0, i]全部转成A的修改次数    
        count_before_i = i + 1 - count_A
        # 将区间[i+1, len(chars)]全部转为B的修改次数
        count_after_i = total_A - count_A
        # 计算最小值
        res = min(res, count_before_i + count_after_i)
    return res


if __name__ == "__main__":
    # AABBA
    # str = input().strip()
    # print(solve_method(str))

    assert solve_method("AABBA") == 1
    assert solve_method("BAABBABBAB") == 3
```