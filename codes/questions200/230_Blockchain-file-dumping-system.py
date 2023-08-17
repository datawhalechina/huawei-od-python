#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 230_Blockchain-file-dumping-system.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 230 区块链文件转储系统
"""
import sys

def solve_method(M, files):
    l, r = 0, 0
    sum_, max_ = 0, 0
    while r < len(files):
        # 计算新的 子文件集 大小之和
        new_sum = sum_ + files[r]
        # 当前 子文件集的 大小之和 > 容量，则将 子文件集 中 第一个文件 删除
        while new_sum > M and l < r:
            if new_sum > M:
                sum_ -= files[l]
                new_sum -= files[l]
                l += 1

        # 当前 子文件集的 大小之和 < 容量，则添加 当前文件 到 子文件集中
        if new_sum < M:
            sum_ += files[r]
            r += 1
            # 记录 最大的 子文件集的 大小之和
            max_ = max(max_, sum_)
        elif new_sum == M:
            return M
    return max_

if __name__ == '__main__':
    file_sizes = [100, 300, 500, 400, 400, 150, 100]
    assert solve_method(1000, file_sizes) == 950

    file_sizes = [100, 500, 400, 150, 500, 100]
    assert solve_method(1000, file_sizes) == 1000

    file_sizes = [100, 100, 500, 500, 100, 100]
    assert solve_method(1000, file_sizes) == 1000