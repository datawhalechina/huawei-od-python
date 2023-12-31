# 045 去重求和

## 题目描述

给定一个数组，编写一个函数，计算他的最大`N`个数和最小`N`个数的和，需要对数组进行去重。

## 输入描述

第一行输入`M`，表示数组大小。

第二行输入`M`个数，表示数组内容。

第三行输入`N`，表示需要计算的最大最小`N`的个数。

## 输出描述

输出最大N个数和最小N个数的和。

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
342
```
**说明**

最大2个数是100和95，最小2个数是83和64，求和之后输出342。

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

最大2个数是4和3，最小2个数是3和2，有重叠输出为-1。

## 解题思路

1. 对数组使用`set`和`sorted`进行去重排序。
2. 如果数组长度足够分成最大的前n个数和最小的前n个数据，返回求和的值。否则，返回-1。

## 解题代码

```python
def solve_method(nums, n):
    nums = sorted(set(nums))
    result = -1
    if len(nums) >= 2 * n:
        result = sum(nums[:n]) + sum(nums[-n:])

    return result


if __name__ == '__main__':
    assert solve_method([95, 88, 83, 64, 100], 2) == 342
    assert solve_method([3, 2, 3, 4, 2], 2) == -1
```

