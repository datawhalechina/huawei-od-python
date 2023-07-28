# 106 整数对最小和

## 题目描述

给定两个整数数组`array1`和`array2`，数组元素按升序排列。假设从`array1`和`array2`中分别取出一个元素可构成一对元素。现在需要取出`K`个元素，并对取出的所有元素求和。计算和的最小值

**注意：** 两对元素如果对应于`array1`和`array2`中的两个下标均相同，则视为同一个元素。

## 输入描述

输入两行数组`array1`和`array2`。每行首个数字为数组大小`size`。

取值范围：
- 0 < size <= 100
- 0 < array1[i] <= 1000
- 0 < array2[i] <= 1000

接下来一行为正整数`k`，取值范围是0 < k <= array1.size() * array2.size()。

## 输出描述

满足要求的最小和。

## 示例描述

### 示例一

**输入：**

```text
3 1 1 2
3 1 2 3
2
```

**输出：**

```text
4
```

**说明：** 

用例中，需要取两个元素，
- 取第一个数组第0个元素与第二个数组第0个元素，组成一对元素`[1,1]`
- 取第一个数组第1个元素与第二个数组第0个元素，组成一对元素`[1,1]`

求和为`1+1+1+1=4`为满足要求的最小和。

## 解题思路

**基本思路：** `heapq.heappush()`是往堆中添加新值，此时自动建立了小根堆。

1. 先判断是否存在长度为1的数组，如果存在，直接取该数组元素和另一个数组前k个元素的相加返回为结果。
2. 如果没有长度为1的数组 则将两个数组遍历，计算两个数组中的元素和，并加入到堆`sums`中。
3. 调用`nsmallest`函数，得到前k个值最小值，求和之后，返回结果。

## 解题代码

```python
import heapq


def solve_method(arr1, arr2, k):
    # 如果含有长度为1的数组，则返回该数组元素和另一个数组前k个元素的相加
    if len(arr1) == 1:
        return arr1[0] * k + sum(arr2[:k])
    elif len(arr2) == 1:
        return arr2[0] * k + sum(arr1[:k])
    sums = []
    for x in arr1:
        for y in arr2:
            heapq.heappush(sums, x + y)

    return sum(heapq.nsmallest(k, sums))


if __name__ == "__main__":
    assert solve_method([1, 1, 2], [1, 2, 3], 2) == 4
    assert solve_method([1], [1, 2, 3], 2) == 5
    assert solve_method([1, 1, 2], [1, 2, 3], 2) == 4
    assert solve_method([1, 1, 1], [1, 2, 3], 3) == 6
    assert solve_method([1, 1], [1, 2, 3], 5) == 14
    assert solve_method([1, 1], [1, 2, 3], 6) == 18
    assert solve_method([1, 2, 3, 4], [1, 2, 3], 2) == 5
```
