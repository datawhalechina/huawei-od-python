# 153滑动窗口

## 题目描述

有一个`N`个整数的数组，和一个长度为`N`的窗口。 窗口从数组内的第一个数开始滑动，直到窗口不能滑动为止。 每次滑动产生一个窗口，和窗口内所有数的和， 求窗口滑动产生的所有窗口和的最大值

## 输入描述

第一行输入一个正整数`N`，表示整数个数`0<N<100000` 

第二行输入`N`个整数，整数取值范围`[-100,100]`

 第三行输入正整数`N`，`N`代表窗口的大小，`M<=N<=100000`

## 输出描述

窗口滑动产生所有窗口和的最大值

## 示例描述

### 示例一

**输入：**

```text
6
12 10 20 30 15 23
```

**输出：**

```text
68
```

## 解题思路

首先计算初始窗口的和，并将其作为当前的最大和。然后通过一个循环，依次将窗口向右移动，每次减去窗口左边的数，加上窗口右边的数，并更新最大和。最后输出最大和。

请注意，该代码没有对输入进行严格的合法性检查，如输入的范围是否满足要求等。在实际应用中，需要根据具体情况进行适当的输入验证和错误处理。

## 解题代码

```python
def max_sliding_window_sum(N, nums):
    if window_size > N:
        return 0

    max_sum = float('-inf')  # 初始化最大和为负无穷大

    # 计算初始窗口的和
    window_sum = sum(nums[:window_size])
    max_sum = max(max_sum, window_sum)

    # 滑动窗口
    for i in range(window_size, N):
        # 窗口向右移动，减去窗口左边的数，加上窗口右边的数
        window_sum = window_sum - nums[i - window_size] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# 读取输入
N = int(input())
nums = list(map(int, input().split()))

# 调用函数计算最大窗口和
max_sum = max_sliding_window_sum(N, nums)

# 输出结果
print(max_sum)
```

