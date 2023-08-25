# 074 总最快检测效率

## 题目描述

在系统、网络均正常情况下，组织核酸采样员和志愿者对人群进行核酸检测筛查。每名采样员的效率不同，采样效率为`N人/小时`。

由于外界变化，采样员的效率会以`M人/小时`为粒度发生变化，`M`为采样效率浮动粒度，`M=N*10%`，输入保证`N*10%`的结果为整数。采样员效率浮动规则：

采样员需要一名志愿者协助组织才能发挥正常效率，再此基础上，每增加一名志愿者，效率提升`1M`，最多提升`3M`，如果没有志愿者协助组织，效率下降`2M`。

怎么安排速度最快，求总最快检测效率。（总检查效率为各采样人员效率值相加）

## 输入描述

第一行输入是两个整数，分别是采样员人数和志愿者人数，取值范围：1 <= 采样人数 <= 100、1 <= 志愿者人数 <= 500。

第二行输入是采样员基准效率值（单位人/小时），取值范围[60,600]，保证序列中每项值计算10%为整数。

## 输出描述

输出一个整数，总最快检测效率（单位人/小时）。

## 示例描述

### 示例一

**输入：**
```text
2 2
200 200
```

**输出：**
```text
400
```

## 解题思路

贪心算法，在考虑每一名志愿者时，都要最大化收益,先将数组初始化为1名志愿者都没有的效率，之后每增加一位志愿者，
到要使得效率提升是最大的。

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 074_total-fastest-detection-efficiency
@time:  24/8/2023 下午 4:42
@project:  huawei-od-python 
"""


def solve_method(nums, num_volunteer):
    profit = []
    for p in nums:
        profit.extend([p * 0.2, p * 0.1, p * 0.1, p * 0.1])
    nums = [i * 0.8 for i in nums]
    return int(sum(nums) + sum(sorted(profit, reverse=True)[:num_volunteer]))


if __name__ == '__main__':
    n1, n2 = map(int, input().strip().split(' '))
    nums = list(map(int, input().strip().split(' ')))
    res = solve_method(nums, n2)
    print(res)


```

