# 258 组装新的数组

## 题目描述

给你一个整数`M`和数组`N`，`N`中的元素为连续整数，要求根据`N`中的元素组装成新的数组`R`，组装规则：

1. `R`中元素总和加起来等于`M`。
2. `R`中的元素可以从`N`中重复选取。
3. `R`中的元素最多只能有1个不在`N`中，且比`N`中的数字都要小（不能为负数）。

请输出：数组`R`一共有多少组装办法。

## 输入描述

第一行输入是连续数组`N`，采用空格分隔。

第二行输入数字`M`。

## 输出描述

输出的是组装办法数量。

**备注：**

- 1 <= M <= 30
- 1 <= N.length <= 1000

## 示例描述

### 示例一

**输入：**
```text
2
5
```

**输出：**
```text
1
```

**说明：**  

只有1种组装办法，就是[2,2,1]。

### 示例二

**输入：**
```text
2 3
5
```

**输出：**
```text
2
```

**说明：**

一共2种组装办法，分别是[2,2,1]、[2,3]。
   
## 解题思路

**基本思路：** 使用深度优先搜索DFS求解。

1. 对数组`nums`进行遍历，筛选出不大于`m`的元素组成新数组。
2. 进行深度优先搜索：
   - 确定参数：数组`nums`、总和`m`、遍历索引`index`、数组中元素的最小值`min_val`、组装的数量`count`。
   - 终止条件：
       - 当总和`m`小于0时，返回结果。
       - 当恰好总和为0或总和小于数组中元素的最小值，表示找到了一组，返回的结果累加1。
   - 递归处理：遍历所有元素，进行深度搜索时，总和减去当前元素。
3. 返回组装的数量`count`。

## 解题代码
```python
def solve_method(nums, m):
    min_val = nums[0]
    nums = [num for num in nums if num <= m]
    return dfs(nums, m, 0, min_val, 0)


def dfs(nums, m, index, min_val, count):
    if m < 0:
        return count
    if m == 0 or m < min_val:
        return count + 1

    for i in range(index, len(nums)):
        count = dfs(nums, m - nums[i], i, min_val, count)
    return count


if __name__ == "__main__":
    # 2
    # 5
    # N = list(map(int, input().strip().split()))
    # M = int(input().strip())
    # print(solve_method(N, M))

    assert solve_method([2], 5) == 1
    assert solve_method([2, 3], 5) == 2
    assert solve_method([3, 4], 2) == 1
```