# 195 跳房子（2）

## 题目描述

跳房子，也叫跳飞机，是一种世界性的儿童游戏。游戏参与者需要分多个回合按顺序跳到第1格直到房子的最后一格，然后获得一次选房子的机会，直到所有房子被选完，房子最多的人获胜。在跳房子的过程中，如果有踩线等违规行为会结束当前回合，甚至可能倒退几步。

假设房子的总格数是`count`，小红每回合可能连续跳的步数都放在数组`steps`中，请问数组中是否有一种步数的组合，可以让小红三个回合跳到最后一格？如果有，请输出索引和最小的步数组合（数据保证索引和最小的步数组合是唯一的）。

注意：数组中的步数可以重复，但数组中的元素不能重复使用。

## 输入描述

第一行输入为房子总格数`count`，取值范围是 count <= 10000。

第二行输入为每回合可能连续跳的步数`steps`，数组长度的取值范围是3 <= steps.length <= 10000，每个步数的取值范围是 -100000 <= steps[i] <= 100000。

## 输出描述

返回索引和最小的满足要求的步数组合（顺序保持`steps`中原有顺序）。

## 示例描述

### 示例一

**输入：**

```text
9
[1,4,5,2,0,2]
```

**输出：**

```text
[4,5,0]
```


### 示例二

**输入：**

```text
9
[1,5,2,0,2,4]
```

**输出：**

```text
[5,2,2]
```

### 示例三

**输入：**

```text
12
[-1,2,4,9]
```

**输出：**

```text
[-1,4,9]
```

## 解题思路

**基本思路：** 本题类似于三数之和，使用双指针求解。

1. 将数组按照值和索引的二元组形式重新存储。
2. 按照值从小到大排序。
3. 使用双指针遍历数组：
    - 左指针从当前元素的下一个位置开始。
    - 右指针从数组的最后一个位置开始。
    - 比较左右指针：
        - 如果当前三个步数之和等于房子的总格数，并且索引之和最小，则保存结果。
        - 如果小于总格数，则左指针向右移，增大和数。
        - 如果大于总格数，则右指针向左移，减小和数。
4. 将结果按照索引顺序从小到大排序，并仅返回元素的值。   

## 解题代码

```python
import math


def solve_method(target, nums):
    nums = [(n, i) for i, n in enumerate(nums)]
    # 按照值从小到大排序
    nums = sorted(nums, key=lambda x: x[0])
    result = []
    min_index_sum = math.inf
    for i in range(len(nums) - 2):
        # 左指针从当前元素的下一个位置开始
        left = i + 1
        # 右指针从数组的最后一个位置开始
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i][0] + nums[left][0] + nums[right][0]
            index_sum = nums[i][1] + nums[left][1] + nums[right][1]
            if current_sum == target and index_sum < min_index_sum:
                # 如果当前三个步数之和等于房子的总格数，并且索引之和最小，则返回结果
                result = [nums[i], nums[left], nums[right]]
                min_index_sum = index_sum
            elif current_sum < target:
                # 如果小于总格数，则左指针向右移，增大和数
                left += 1
            else:
                # 如果大于总格数，则右指针向左移，减小和数
                right -= 1

    # 按照索引顺序从小到大排序
    result.sort(key=lambda x: x[1])
    return [x[0] for x in result]


if __name__ == '__main__':
    assert solve_method(9, [1, 4, 5, 2, 0, 2]) == [4, 5, 0]
    assert solve_method(9, [1, 5, 2, 0, 2, 4]) == [5, 2, 2]
    assert solve_method(12, [-1, 2, 4, 9]) == [-1, 4, 9]
```

