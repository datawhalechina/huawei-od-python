# 065-去重求和

## 题目描述

给定一个数组，编写一个函数，
计算他的最大N个数和最小N个数的和,需要对数组进行去重。

## 输入描述
第一行输入M，M表示数组大小，第二行输入M个数，表示数组内容，
第三行输入N表示需要计算的最大最小N的个数

## 输出描述

输出最大N个数和最小N个数的和

## 示例描述

### 示例一

**输入：**
```
5
95 88 83 64 100
2
```

**输出：**
```
392
```
**说明**

最大2个数[100,95]，最小2个数[83,64]。输出342

### 示例二

**输入：**

```
5
3 2 3 4 2
2
```

**输出：**

```
-1
```
**说明**

最大2个数是[4,3]，最小2个数是[3,2]，有重叠输出为-1

## 解题思路

本题是一个求和问题，对于输入的一行数字，选取最小的n个数与最大n个数求和，
若n个最大数与n个最小数有重合，则返回-1
可以使用Python的set()数据类型，对输入的数字去重。
然后将其排序，并依次加入结果中，当处理到的数字下标小于n或大于等于len(list)-n时，
我们就将该数字加入结果中。
在遍历结束后,我们将结果输出即可。



```python
def addNumber(nums, n):
    sorted_number = sorted(list(set(nums)))
    if len(sorted_number) < 2 * n:
        return -1
    return sum(sorted_number[:n]) + sum(sorted_number[-n:])


if __name__ == '__main__':
    m = int(input().strip())
    nums = list(map(int, input().strip().split(' ')))
    n = int(input().strip())
    res = addNumber(nums, n)
    print(res)

```

