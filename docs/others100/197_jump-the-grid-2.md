# 197跳格子（2）

## 题目描述

小明和朋友玩跳格子游戏，有`n`个连续格子组成的圆圈，每个格子有不同的分数，小朋友可以选择从任意格子起跳，但是不能跳连续的格子，不能回头跳，也不能超过一圈。

给定一个代表每个格子得分的非负整数数组，计算能够得到的最高分数。

## 输入描述

给定一个数组`nums`，第一个格子和最后一个格子收尾相连，如：`2 3 2`。其中数组长度范围是1 <= nums.length <= 100、0 <= nums[i] <= 1000。

## 输出描述

输出能够得到的最高分，如: 3。

## 示例描述

### 示例一

**输入：**

```text
2 3 2
```

**输出：**

```text
3 
```

**说明：**

只能跳3这个格子，因为第一个格子和第三个格子收尾相连。

### 示例二

**输入：**

```text
1 2 3 1
```

**输出：**

```text
4 
```

**说明：**

可以跳第一个格子和第三个格子，1+3=4。

## 解题思路

1. `def dpfunc(nums):`: 定义一个函数 `dpfunc`，该函数接受一个数字列表 `nums` 作为参数。

2. `dp = [0] * len(nums)`: 创建一个名为 `dp` 的列表，用于存储每个位置的最大和方案。

3. `dp[0] = nums[0]`: 初始化 `dp` 列表的第一个元素为 `nums` 列表的第一个元素，因为只有一个数字时最大和即为该数字本身。

4. 在接下来的循环中，遍历从索引 1 到列表末尾的范围，表示每个位置的状态转移：

   a. `if i == 1:`: 如果当前位置是索引 1，即第二个数字。

   - `dp[i] = max(nums[i], dp[i - 1])`: 在这种情况下，我们选择当前数字或者前一个位置的最大和，取两者中较大的一个作为当前位置的最大和。

   b. 否则（对于索引大于等于 2 的情况）。

   - `dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])`: 在这种情况下，我们可以选择当前数字或者选择前两个位置的数字和加上当前数字，取两者中较大的一个作为当前位置的最大和。

5. `return dp[len(nums) - 1]`: 返回 `dp` 列表的最后一个元素，即最终的最大和方案。

6. `def main():`: 定义主函数 `main`。

7. `strings = input().split()`: 从标准输入读取一行字符串，并将其按空格分割为字符串列表。

8. `if len(strings) == 1:`: 如果输入只包含一个数字。

   - `print(int(strings[0]))`: 直接输出这个数字并将其转换为整数。

9. 否则，当输入包含多个数字时。

   - `numsStart = [int(x) for x in strings[:-1]]`: 将输入的字符串列表转换为整数列表，不包含最后一个数字。
   - `numsEnd = [int(x) for x in strings[1:]]`: 将输入的字符串列表转换为整数列表，不包含第一个数字。
   - `res = max(dpfunc(numsStart), dpfunc(numsEnd))`: 分别计算以第一个数字开头和以最后一个数字结尾的情况下的最大和方案，并取两者中较大的一个作为结果。
   - `print(res)`: 输出最终的结果。

## 解题代码

```python
def dpfunc(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        if i == 1:
            dp[i] = max(nums[i], dp[i - 1])
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[len(nums) - 1]


def main():
    strings = input().split()
    if len(strings) == 1:
        print(int(strings[0]))
        return

    numsStart = [int(x) for x in strings[:-1]]
    numsEnd = [int(x) for x in strings[1:]]

    res = max(dpfunc(numsStart), dpfunc(numsEnd))
    print(res)

main()
```

