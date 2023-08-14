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

常见的错误思路如下
```
1. 找到A最后一次出现的位置`A_last_index`，计算`A_last_index`前的B出现的次数
2. 找到B第一次出现的位置`B_first_index`，计算`B_first_index`后的A出现的次数
3. 取较小值
```
该思路未考虑如下情况：
- 遇到第一个B后，改为A
- 遇到第二个B后不改动，把它后面出现的A全部换为B
- 例如"BAABBABBAB" -> "AAABBBBBBB" -> 3
___________________
题目要求"最小修改次数"，看到**最小**思考是否可用动态规划（最优子结构？）-> 考虑最终的结果以i为分界点，i前全是A，i后全是B
- 假设字符串位置[0, i]存在`count_A`个A
    - 将区间[0, i]全部转成A，需要修改的次数？即求该区间内B的个数：`i+1-count_A`
    - 将区间[i+1, end]全部转为B，需要的修改次数? 即求该区间内A的个数：`total_A-count_A`
- 将i从0到s.length遍历即可，记录每层的最小修改次数

**代码思路：**
1. 记录A出现的总次数total_A
2. `最小修改次数`可以把把所有的A都转成B实现，所以`最小修改次数`可初始化为total_A
3. 外层循环i从0到s.length遍历
    - 内层求"将区间[0, i]全部转成A"+"将区间[i+1, end]全部转为B"的总次数
    - "将区间[0, i]全部转成A" = i+1-countA
    - "将区间[i+1, end]全部转成B" = i+1-countA
4. `最小修改次数`取各层计算后的最小修改次数

## 解题代码
```python
def solve_method(str):
    total_A = str.count("A")
    res = total_A
    count_A = 0
    for i in range(len(str)):
        if str[i] == "A":
            count_A += 1
        res = min(res, i + 1 - count_A + total_A - count_A)
    return res

if __name__ == "__main__":
    # AABBA
    str = input().strip()
    print(solve_method(str))

    assert solve_method("AABBA") == 1
    assert solve_method("BAABBABBAB") == 3
```