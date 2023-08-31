# 029 最多等和不相交连续子序列

## 题目描述

给定一个数组，我们称其中连续的元素为连续子序列，称这些元素的和为连续子序列的和。数组中可能存在几组连续子序列，组内的连续子序列互不相交且有相同的和。

求一组连续子序列，组内子序列的数目最多，输出这个数目。

## 输入描述

第一行输入为数组长度`N`, 取值范围是1 <= N <= 10^3。

第二行是`N`个用空格分开的整数`Ci`，取值范围是-10^5 <= Ci <= 10^5。

## 输出描述

第一行是一个整数`M`，表示满足要求的最多的组内子序列的数目。

## 示例描述

### 示例一

**输入：**
```text
10
8 8 9 1 9 6 3 9 1 0
```

**输出：**
```text
4
```

**说明：**

四个子序列第一个元素和最后一个元素下标分别为：
```
2 2
4 4
5 6
7 7
```

### 示例二

**输入：**
```text
10
-1 0 4 -3 6 5 -6 5 -7 -3
```

**输出：**
```text
3
```

**说明：**

三个子序列第一个元素和最后一个元素下标分别为：
```
3 3
5 8
9 9
```

## 解题思路

1. 初始化子序列和频次字典`sum_count_dict`，`key`为子序列和，`value`为出现次数。
2. 初始化子序列和位置索引字典`sum_pos_dict`，`key`为子序列和，`value`为位置索引列表。
3. 构建dp数组，`dp[i]`表示第i个位置的从后到前的所有数之和。   
4. 遍历子序列：
    - 记录每个和出现的次数，存储在子序列和频次字典`sum_count_dict`中。
    - 记录已使用过的元素索引，存储在子序列和位置索引字典`sum_pos_dict`中。
    - 注意判定若当前和的索引曾经出现过，则不累加和的次数。 
5. 返回子序列中最多次数。   

## 解题代码

```python
def solve_method(N, nums):
    max_count = 0
    # 子序列和频次，key为子序列和，value为出现次数
    sum_count_dict = {}
    # 子序列和位置索引，key为子序列和，value为位置索引列表
    sum_pos_dict = {}
    # dp[i]表示第i个位置的从后到前的所有数之和
    dp = nums[:]
    for i in range(N):  # 枚举子序列的长度
        for j in range(N - i):  # 枚举子序列的起始位置
            if i > 0:
                dp[j] += nums[j + i]
            summ = dp[j]
            # 判断该和是否记录过
            if summ not in sum_count_dict:
                sum_count_dict[summ] = 0
                sum_pos_dict[summ] = set()

            # 判断该索引是否被记录过
            exist = False
            pos = sum_pos_dict[summ]
            for k in range(j, j + i + 1):
                if k in pos:
                    exist = True
                    break
            # 索引没有被记录过
            if not exist:
                sum_count_dict[summ] += 1
                max_count = max(max_count, sum_count_dict[summ])
                # 将索引加入到字典的列表中
                for k in range(j, j + i + 1):
                    pos.add(k)
                sum_pos_dict[summ] = pos
    return max_count


if __name__ == "__main__":
    # 10
    # 8 8 9 1 9 6 3 9 1 0
    # -1 0 4 -3 6 5 -6 5 -7 -3
    # N = int(input())
    # nums = list(map(int, input().split()))
    # print(solve_method(N, nums))

    assert solve_method(10, [8, 8, 9, 1, 9, 6, 3, 9, 1, 0]) == 4
    assert solve_method(10, [-1, 0, 4, -3, 6, 5, -6, 5, -7, -3]) == 3
```