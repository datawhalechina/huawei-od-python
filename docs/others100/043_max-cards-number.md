# 043 卡片组成的最大数字

## 题目描述

小组中每位都有一张卡片，卡片是6位以内的正整数，将卡片连起来可以组成多种数字，计算组成的最大数字。

## 输入描述

英文逗号分隔的多个正整数字符串，不需要考虑非数字这种异常情况，小组种最多25个人。

## 输出描述

最大数字字符串。

## 示例描述

### 示例一

**输入：**
```text
22,221
```

**输出：**
```text
22221
```
 
### 示例二

**输入：**

```text
4589,101,41425,9999
```

**输出：**

```text
999945894125101
```

## 解题思路

1. 遍历字符串数组。 
2. 再次遍历后面的字符串数组：
    - 比较交换前组成的数字和交换后组成的数字，如果交换后的较大，则交换两个字符串的位置。
3. 将排列好的字符串拼接成结果字符串，并返回。    

## 解题代码

```python
def solve_method(strings):
    length = len(strings)

    for i in range(length):
        for j in range(i + 1, length):
            if int(strings[i] + strings[j]) < int(strings[j] + strings[i]):
                strings[i], strings[j] = strings[j], strings[i]

    return "".join(strings)


if __name__ == '__main__':
    assert solve_method(["22", "221"]) == "22221"
    assert solve_method(["4589", "101", "41425", "9999"]) == "9999458941425101"
```

