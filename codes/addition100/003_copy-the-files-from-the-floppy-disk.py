#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 003_copy-the-files-from-the-floppy-disk.py
@time: 2023/9/4 11:11
@project: huawei-od-python
@desc: 
"""
import math

# 读取文件的数量
n = int(input())

# 使用列表推导式来读取每个文件的大小
nums = [int(input()) for _ in range(n)]

# 计算背包的容量（以512字节块为单位）
W = 1474560 // 512

# 初始化动态规划数组，其中dp[i][j]存储前i个文件在容量为j的背包中可以达到的最大文件大小
dp = [[0] * (W + 1) for _ in range(n + 1)]

# 循环通过所有文件
for i in range(1, n + 1):

    # 计算当前文件的大小（以512字节块为单位）和实际大小（字节）
    size, value = math.ceil(nums[i - 1] / 512), nums[i - 1]

    # 遍历所有可能的背包容量
    for j in range(W + 1):

        # 如果当前文件可以放入背包（即其大小小于或等于当前背包容量），我们可以选择放入或不放入文件
        if size <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - size] + value)
        else:
            # 如果当前文件太大而无法放入背包，我们只能选择不放入文件
            dp[i][j] = dp[i - 1][j]

# 打印结果：在给定容量限制下，可以存储的最大文件大小
print(dp[n][W])
