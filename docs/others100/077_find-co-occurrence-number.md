# 077 找出两个整数数组中同时出现的整数

## 题目描述
现有两个整数数组，需要你找出两个数组中同时出现的整数，并按照如
下要求输出：
1. 有同时出现的整数时，先按照同时出现次数
(整数在两个数组中都出现并且按照出现次数较少的那个次数进行归类)，然后按照出现次数从小到大依次按行输出。
2. 没有同时出现的整数时，输出NULL。


## 输入描述
第一行为第一个整数数组，第二行为第二个整数数组，
每行数据中整数与整数之间以英文逗号分隔，
整数的取值范围为[-200,200]，数组长度的范围为[1,10000]之间的整数。
## 输出描述
按照出现次数从小到大依次按行输出，每行输出的格式为:出现次数:该出现次数下的整数升序排序的结果。
格式中的":"为英文冒号，整数间以英文逗号分隔。

## 示例描述

### 示例一

**输入：**
```text
5,3,6,-8,0,11
2,8,8,8,-1,15
```

**输出：**
```text
NULL
```
**说明**
两个整数数组没有同时出现的整数，输出NULL。

### 示例二

**输入：**
```text
5,8,11,3,6,8,8,-1,11,2,11,11
11,2,11,8,6,8,8,-1,8,15,3,-9,11
```
**输出：**
```text
1:-1,2,3,6
3:8,11
```
**说明：**
两个整数数组中同时出现的整数为-1、2、3、6、8、11，
其中同时出现次数为1的整数为-1,2,3,6(升序排序)，
同时出现次数为3的整数为8,11(升序排序)，
先升序输出出现次数为1的整数，再升序输出出现次数为3的整数。

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 077_find-co-occurrence-number
@time:  23/8/2023 下午 8:25
@project:  huawei-od-python 
"""
from collections import Counter


def solve_method(nums1, nums2):
    c1 = dict(Counter(nums1))
    c2 = dict(Counter(nums2))
    common = set(c1.keys()) & set(c2.keys())
    record = dict()
    for number in common:
        freq = min(c1[number], c2[number])
        if freq not in record:
            record[freq] = [number]
        else:
            record[freq].append(number)
    items = sorted(record.items())
    items = [[item[0], sorted(item[1])] for item in items]
    output = []
    for item in items:
        output.append(f'{item[0]}:' + ','.join(map(str, item[1])))

    return '\n'.join(output)


if __name__ == '__main__':
    nums1 = list(map(int, input().strip().split(',')))
    nums2 = list(map(int, input().strip().split(',')))
    res = solve_method(nums1, nums2)
    print(res)

```

