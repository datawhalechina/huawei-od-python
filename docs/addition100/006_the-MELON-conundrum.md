# 006 MELON的难题

## 题目描述

`MELON`有一堆精美的雨花石（数量为`n`，重量各异），准备送给`S`和`W`。`MELON`希望送给俩人的雨花石重量一致，请你设计一个程序，帮`MELON`确认是否能将雨花石平均分配。

## 输入描述

第1行是雨花石个数`n`，取值范围是0 < n < 31。

第2行是空格分隔的各雨花石重量：`m[0] m[1] ... m[n-1]`，其中0 < m[k] < 1001。

不需要考虑异常输入的情况。

## 输出描述

如果可以均分，从当前雨花石中最少拿出几块，可以使两堆的重量相等；如果不能均分，则输出-1。

## 示例描述

### 示例一

**输入：**
```text
4
1 1 2 2
```

**输出：**
```text
2
```

**说明：**  

一共有4颗雨花石，4颗雨花石重量分别为1、1、2、2。

均分时，只能分别为1、2，需要拿出重量为1和2的两块雨花石，所以输出2。

### 示例二

**输入：**
```text
10
1 1 1 1 1 9 8 3 7 10
```

**输出：**
```text
3
```

**说明：**  

一共有10颗雨花石，10颗雨花石重量分别为1、1、1、1、1、9、8、3、7、10。

均分时可以1、1、1、1、1、9、7和10、8、3，也可以1、1、1、1、9、8和10、7、3、1，或者其他均分方式，但第一种只需要拿出重量为10、8、3的3块雨花石，第二种需要拿出4块，所以输出3（块数最少）。

## 解题思路

**基本思路：** 使用回溯法求解。

1. 如果数组之和不能整除2，说明不能均分，返回-1。
2. 使用回溯法，找到子序列的和等于数组之和的一半`target_sum`：
    - 确定参数：索引`index`、子序列之和`curr_sum`。
    - 终止条件：
        - 如果子序列之和等于数组之和的一半，并且另一个子序列也同样满足，则将当前子序列存入结果列表中。
        - 如果子序列之和超过数组之和的一半，或已经遍历完，则直接返回。
    - 递归处理，遍历所有索引：
        - 将当前元素加入子序列中。
        - 递归索引值，并将子序列之和累加当前元素值。
        - 回溯，在子序列中删除当前元素。
3. 返回结果列表中子序列最短的长度值。

## 解题代码

```python
def remove_elements(arr, sub_arr):
    result_array = arr.copy()

    for elem in sub_arr:
        if elem in result_array:
            result_array.remove(elem)

    return result_array


def solve_method(n, nums):
    total = sum(nums)
    if total % 2 != 0:
        return -1

    target_sum = total // 2
    sub_lst = []
    result = []

    def backtrack(index, curr_sum):
        if curr_sum == target_sum:
            # 得到另一个子序列
            other_lst = remove_elements(nums, sub_lst[:])
            # 如果另一个子序列之和也等于数组之和的一半，则存入结果列表中
            if target_sum == sum(other_lst) and sub_lst[:] not in result:
                result.append(sub_lst[:])
                return
        if curr_sum > target_sum or index >= n:
            return

        for i in range(index, n):
            sub_lst.append(nums[i])
            backtrack(i + 1, curr_sum + nums[i])
            sub_lst.pop()

    nums.sort()
    backtrack(0, 0)

    if not result:
        return -1

    return min(len(x) for x in result)


if __name__ == '__main__':
    assert solve_method(4, [1, 1, 2, 2]) == 2
    assert solve_method(10, [1, 1, 1, 1, 1, 9, 8, 3, 7, 10]) == 3
    assert solve_method(4, [1, 5, 5, 8]) == -1
```