#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 012_blockchain-file-dumping-system.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 012 区块链文件转储系统
"""


def solve_method(M, files):
    l, r = 0, 0
    sum_val, max_val = 0, 0
    while r < len(files):
        # 计算新的子文件集大小之和
        new_sum = sum_val + files[r]
        if new_sum > M:
            # 如果子文件集大小之和超过了容量，则删除最左边的文件，左指针向左移
            sum_val -= files[l]
            l += 1
        elif new_sum < M:
            # 如果子文件集大小之和小于容量，则添加该文件，右指针向右移
            sum_val += files[r]
            r += 1
            # 比较并得到文件集的最大容量
            max_val = max(sum_val, max_val)
        else:
            # 如果相等，则得到最大容量为M
            return M

    return max_val


if __name__ == '__main__':
    file_sizes = [100, 300, 500, 400, 400, 150, 100]
    assert solve_method(1000, file_sizes) == 950

    file_sizes = [100, 500, 400, 150, 500, 100]
    assert solve_method(1000, file_sizes) == 1000

    file_sizes = [100, 100, 500, 500, 100, 100]
    assert solve_method(1000, file_sizes) == 1000
