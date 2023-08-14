# 075 快递货车

## 题目描述

一辆运送快递的货车，
运送的快递放在大小不等的长方体快递盒中，
为了能够装载更多的快递同时不能让货车超载，需要计算最多能装多少个快递。

注:快递的体积不受限制。
快递数最多1000个，货车载重最大50000。


## 输入描述
第一行输入每个快递的重量用英文逗号隔开
如5,10,2,11
第二行输入货车的载重量如20

## 输出描述
输出最多能装多少个快递如3


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
贪心算法，依次选取重量最小的快递。
将输入的重量按从小到大的顺序排序，然后依次选取重量，如果累加的总重量小于等于货车载重最大值，
就继续选取下一个重量；否则结束选取。最后输出选取的重量数。

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 075_express-truck
@time:  14/8/2023 上午 9:25
@project:  huawei-od-python 
"""
import sys


def solve_method(weight, capacity):
    weight = sorted(weight)
    count, total_weight = 0, 0
    for i in range(len(weight)):
        total_weight += weight[i]
        if total_weight <= capacity:
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    weight = list(map(int, sys.stdin.readline().strip().split(',')))
    capacity = int(sys.stdin.readline().strip())
    res = solve_method(weight, capacity)
    print(res)

```

