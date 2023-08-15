# 149 求有多少种K个数的组合使和等于目标

## 题目描述

给定一个整数数组`nums`、一个数字`k`、一个整数目标值`target`，请问`nums`是否存在`k`个元素，使其相加结果为`target`，请输出所有符合条件且不重复的`k`元组的个数。

数据范围：
- 2 <= nums.length <= 200
- 10^9 <= nums[i] <= 10^9
- 10^9 <= target <= 10^9
- 2 <= k <= 100

## 输入描述

第一行是`nums`取值，以空格分隔，如`2 7 11 15`

第二行是`k`的取值。

第三行是`target`取值。

## 输出描述

输出所有符合条件的元组个数。

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

(-1,0,1)和(-1,2,-1)满足条件。

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

## 解题思路

**基本思路：** 使用回溯法求解。

1. 检查输入数据是否符合要求。
2. 将数组从小到大排序。   
3. 使用回溯法：
    - 参数：遍历索引`start_index`、当前组合的和`current_sum`。
    - 终止条件：
        - 当和值等于目标值，并且正好有k个元素，则保存该组合。
        - 如果该组合的和超过了目标值，或个数超过了k个，则返回。
    - 回溯处理：
        - 将该元素加入到组合列表中。
        - 继续下一个元素，遍历索引累加1，当前组合的和值累加该元素的值
        - 将该元素从组合列表中删除（回溯）。
4. 去重列表中的元素组合，并返回该结果列表的长度，即为所有符合条件的元组个数。

## 解题代码

```python
def solve_method(nums, k, target):
    if not (nums and (2 <= len(nums) <= 200)
            and (2 <= k <= 100)
            and (-10 ** 9 <= target <= 10 ** 9)
            and (-10 ** 9 <= all(nums) <= 10 ** 9)):
        return -1

    result = []
    current_combination = []

    def backtracking(start_index, current_sum):
        if len(current_combination) == k and current_sum == target:
            # 当和值等于目标值，并且正好有k个元素，则保存该组合
            result.append(list(current_combination))
            return

        if len(current_combination) > k or current_sum > target:
            # 如果该组合的和超过了目标值，或个数超过了k个，则返回
            return

        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                # 避免重复取值
                continue
            current_combination.append(nums[i])
            backtracking(i + 1, current_sum + nums[i])
            current_combination.pop()

    nums.sort()
    backtracking(0, 0)
    # 去重处理
    result = list(set(tuple(comb) for comb in result))
    result = [list(comb) for comb in result]
    return len(result)


if __name__ == '__main__':
    assert solve_method([-1, 0, 1, 2, -1, -4], 3, 0) == 2
    assert solve_method([2, 7, 11, 15], 2, 9) == 1
    assert solve_method([10, 10, 10, 1, 1], 4, 31) == 1
```