#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 162_copy-the-files-from-the-floppy-disk.py
@time: 2023/9/4 11:11
@project: huawei-od-python
@desc: 003 通过软盘拷贝文件
"""
import math

# 计算背包的容量（以512字节块为单位）
W = 1474560 // 512


def solve_method(files):
    n = len(files)

    # 初始化dp数组，dp[i][j]表示存储前i个文件在容量为j的背包中可以达到的最大文件大小
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        # 计算当前文件的大小（以512字节块为单位）和实际大小（字节）
        size, value = math.ceil(files[i - 1] / 512), files[i - 1]

        # 遍历所有可能的背包容量
        for j in range(W + 1):
            # 如果当前文件可以放入背包（即小于或等于当前背包容量），可以选择放入或不放入文件
            if size <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - size] + value)
            else:
                # 如果当前文件太大而无法放入背包，只能选择不放入文件
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


if __name__ == '__main__':
    files = [737270, 737272, 737288]
    assert solve_method(files) == 1474542

    files = [400000, 200000, 200000, 200000, 400000, 400000]
    assert solve_method(files) == 1400000
