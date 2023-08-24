# 072 快递货车

## 题目描述

一辆运送快递的货车，
运送的快递放在大小不等的长方体快递盒中，
为了能够装载更多的快递同时不能让货车超载，需要计算最多能装多少个快递。

注:快递的体积不受限制。

快递数最多1000个，货车载重最大50000。




## 输入描述
第一行输入每个快递的重量用英文逗号隔开，
如5,10,2,11。
第二行输入货车的载重量如20


## 输出描述
输出最多能装多少个快递，如3


## 示例描述

### 示例一

**输入：**
```text
5,10,2,11
20
```

**输出：**
```text
3
```

## 解题思路
将输入的重量按从小到大的顺序排序，然后依次选取重量，
如果累加的总重量小于等于容量，就继续选取下一个重量；否则结束选取。最后输出选取的重量数。
## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 072_express-truck
@time:  24/8/2023 上午 11:58
@project:  huawei-od-python 
"""


def solve_method(nums, weight):
    nums = sorted(nums)
    ans = 0
    sum_weight = 0
    for i in range(len(nums)):
        sum_weight += nums[i]
        if sum_weight > weight:
            return ans
        else:
            ans += 1
    return ans


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(',')))
    weight = int(input().strip())
    res = solve_method(nums, weight)
    print(res)


```

