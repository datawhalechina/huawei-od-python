# 158 猜密码

## 题目描述

小杨申请了一个保密柜，但是他忘记了密码，只记得密码都是数字，而且所有数字都是不重复的。请你根据他记住的数字范围和密码的最小数字数量，帮他算下有哪能可能的组合。

规则如下：
1. 输出的组合都是从可选的数字范围中选取的，且不能重复。 
2. 输出的密码数字要按照从小到大的顺序排列，密码组合需要按照字母的顺序，从小到大的顺序排序。 
3. 输出的每一个组合的数字的数量要大于等于密码最小数字数量。 
4. 如果可能的组合为空，则返回`None`。

## 输入描述

第一行是可能的密码数字列表，数字间以`,`分隔。

第二行是密码最小数字数量。 

## 输出描述

可能的密码组合，每种组合展示成一行，每个组合内部的数字以`,`分隔，从小到大的顺序排列。输出的组合间需要按照字典序排序。

## 示例描述

### 示例一

**输入：**

```text
2,3,4
2
```

**输出：**

```text
2,3
2,3,4
2,4
3,4
```

**说明：**

最小密码数量是两个，可能有三种组合：`2,3`、`2,4`、`3,4`。

三个密码有一种：`2,3,4`。

## 解题思路

1. 遍历k的取值`[k, 数组长度]`：
    - 使用`itertools`包的`combinations`方法，生成所有可能的组合，存入列表`combinations_list`。
2. 将列表`combinations_list`按照字典序从小到大排序。
3. 返回结果列表。

## 解题代码

```python
from itertools import combinations


def solve_method(nums, k):
    # 生成所有可能的组合
    combinations_list = []
    for length in range(k, len(nums) + 1):
        combinations_list.extend(combinations(nums, length))

    # 按照要求进行排序
    combinations_list.sort()

    return [list(x) for x in combinations_list ]


if __name__ == '__main__':
    assert solve_method([2, 3, 4], 2) == [[2, 3], [2, 3, 4], [2, 4], [3, 4]]
```

