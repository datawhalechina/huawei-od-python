# 149 求有多少种K个数的组合使和等于目标

## 题目描述

给定一个整数数组`nums`，一个数字`K`，一个整数目标值`target`，求`nums`种存在多少个元组满足：

1. 元组长度为`K`（元组有`K`个元素）
2. 元素之和为`target`

输出所有符合条件且不重复的`K元组的个数`

## 输入描述

第一行是`nums取值`，以' '空格分隔，如`2 7 11 15`

第二行是`K的取值`

第三行是`target取值`

数据范围：
$$
2 \le  nums.length \le 200,
\\
-10^9\le nums[i] \le 10^9,
\\
-10^9\le target \le 10^9,
\\
2\le K \le 100
$$




## 输出描述

输出所有符合条件且不重复的K元组的个数



## 示例描述

### 示例一

**输入：**

```text
-1 0 1 2 -1 -4
3 
0
```

**输出：**

```text
2
```

**说明：**  

(-1,0,1)和(-1,2,-1)满足条件




### 示例二

**输入：**

```text
2 7 11 15
2
9
```

**输出：**

```text
1
```

**说明：**  

二元组(2,7)满足条件






### 示例三

**输入：**

```text
10 10 10 1 1
4
31
```

**输出：**

```text
1
```

**说明：**  

虽然有重复数字，但其实只有四元组(10，10，10，1)满足条件




## 解题思路

**基本思路：** 

通过带回溯的dfs找出数组中满足要求的k元组，并且统计其个数。

我们可以先排序数组，便于dfs过程中剪枝（筛选淘汰那些不可能的分支）。



- 同时有个关键点需要我们注意，那就是输出的K元组不能有重复。

比如示例三，在分析”10 10 10 1 1“时，我们先遍历该序列，取第一个10，然后后面的子序列"10 10 1 1" 找三个数等于21是可以找到的，四元组是(10,10,10,1)；

但在遍历的下一轮，我们不能再分析10了，我们得让索引指向不等于10的下一个数1.



- 在定义递归的方法时，注意终止条件的设置

1. 终止条件1: 子序列不够 k个数; 升序子序列最小的数都比 t大——这个分支下不可能找到
2. 终止条件2：k==1, 只有一个要找的数时，可以使用`in谓词`查找 target是否在子序列里



## 解题代码

```python
from typing import List

def solve_method(nums: List[int], K: int, T: int) -> int:
    # 1. 检查输入是否有效
    assert nums and (2 <= len(nums) <= 200) and (2 <= K <= 100) and (-10 ** 9 <= T <= 10 ** 9) \
           and (-10 ** 9 <= all(nums) <= 10 ** 9)

    # 2. 排序 nums,方便剪枝
    nums = sorted(nums)

    # 3. combination(array,k,t)= 在序列array中找k个数的组合等于t,返回组合的个数
    def combination(array: List[int], k: int, t: int) -> int:
        # 终止条件1: 不够 k个数; 序列最小的数都比 t大
        if len(array) < k or array[0] > t:
            return 0

        # 终止条件2: 只有一个要寻找的数
        if k == 1:
            return 1 if t in array else 0

        cnt = 0
        for i in range(len(array)):
            cnt += combination(array[i + 1:], k - 1, t - array[i])
        return cnt

    # 4. 因为数列里有相同的数字,为避免重复,不能直接调用 combination(nums,K,T)
    count = 0
    i = 0
    while i < len(nums):
        num = nums[i]
        count += combination(nums[i + 1:], K - 1, T - num)

        # 获取数字num能形成多少个组合后，让索引i指向下一个值不同的数字,这是避免重复的关键
        while i < len(nums) and num == nums[i]:
            i += 1

    return count

```