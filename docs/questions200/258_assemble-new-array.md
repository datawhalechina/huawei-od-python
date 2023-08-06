# 258 组装新的数组

## 题目描述

给你一个整数M和数组N，N中的元素为连续整数，要求根据N中的元素组装成新的数组R，组装规则：

1. R中元素总和加起来等于M
2. R中的元素可以从N中重复选取
3. R中的元素最多只能有1个不在N中，且比N中的数字都要小（不能为负数）

请输出：数组R一共有多少组装办法

## 输入描述

第一行输入是连续数组N，采用空格分隔

第二行输入数字M

## 输出描述

输出的是组装办法数量，`int`类型

## 备注
1≤N.length≤30
1≤N.length≤1000

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
只有1种组装办法，就是［2，2，1］

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
一共2种组装办法，分别是
[2,2,1],[2,3]

## 解题思路

**基本思路：**
DFS

**代码思路：**
1. 对数组N进行遍历，筛选出不大于m的数组 -> 组成新数组
2. DFS尝试遍历所有可能的组合
    - 截止条件：总和-M小于0 -> 仍未找到 -> 直接返回；总和-M刚好为0，或比N最小值小 -> 找到一处 -> 返回count+1
    - 核心功能：元素可从数组中重复选取，所以在递归时的起始索引不-1

## 解题代码
```python
def solve_method(nums, m):
    nums = [num for num in nums if num <= m]
    return dfs(nums, m, 0, nums[0], 0)

def dfs(nums, m, index, min_val, count):
    # 截止条件
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
    N = list(map(int, input().strip().split()))
    M = int(input().strip())
    print(solve_method(N, M))

    assert solve_method([2], 5) == 1
    assert solve_method([2, 3], 5) == 2
```