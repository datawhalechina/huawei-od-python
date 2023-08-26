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