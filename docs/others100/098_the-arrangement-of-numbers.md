# 098 数字的排列

## 题目描述

小华是一个对数字很敏感的小朋友，他觉得数字的不同排列方式有特殊的美感。某天，小华突发奇想：

如果数字多行排列，第一行1个数，第二行2个，第三行3个，第`n`行`n`个数字，并且奇数行正序排列，偶数行逆序排列，数字依次累加。 

这样排列的数字一定很有意思，请帮小华实现。

规则总结如下：
1. 每个数字占据4个位置，不足四位用`*`补位，如1打印为`1***`。
2. 数字之间相邻4空格。
3. 数字的打印顺序按照正序逆序交替打印，奇数行正序，偶数行逆序。
4. 最后一行数字顶格，第`n-1`行相对第`n`行缩进四个空格。

## 输入描述

第一行输入为`N`，表示打印多少行，取值范围是1 <= N <= 30。

## 输出描述

```
XXXX1***
3***XXXX2***
```

## 示例描述

### 示例一

**输入：**
```text
2
```

**输出：**
```text
    1***
3***    2***
```

**说明：**  
xxxxx

## 解题思路

1. 计算每一行的数字及数字的排序列表`nums_list`。当奇数行正序排列，当偶数行逆序排列。
2. 遍历数字排序列表`nums_list`，得到每一个数的展现样式，及每一行的字符串结果列表。
3. 逆序输出结果列表。

## 解题代码

```python
from collections import deque


def solve_method(n):
    asc_order = True
    nums_list = deque()
    x = 1
    # 计算每一行的数字及数字的排序
    for i in range(1, n + 1):
        arr = [0] * i
        if asc_order:
            for j in range(i):
                arr[j] = x
                x += 1
        else:
            for j in range(i - 1, -1, -1):
                arr[j] = x
                x += 1
        nums_list.appendleft(arr)
        asc_order = not asc_order

    # 得到每一个数的展现样式，及每一行的字符串
    result = []
    head = ""
    for nums in nums_list:
        content = head
        num_strs = []
        for j in range(len(nums)):
            num = nums[j]
            num_str = str(num) + "*" * (4 - len(str(num)))
            num_strs.append(num_str)

        result.append(content + "    ".join(num_strs))
        head += "    "

    # 逆序输出结果
    return result[::-1]


if __name__ == '__main__':
    assert solve_method(2) == ["    1***", "3***    2***"]
```