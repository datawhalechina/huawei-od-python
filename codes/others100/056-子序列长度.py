#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:056-子序列长度.py
@Date：2023/08/14 21:00
"""


def solve_method(ints, target_sum):
    max_len = 0  # 初始化最大长度为0

    # 遍历整数列表，寻找和为target_sum的子序列
    for i in range(len(ints)):
        tmp_sum = 0
        for j in range(i, len(ints)):
            tmp_sum += ints[j]
            if tmp_sum > target_sum:
                break
            if tmp_sum == target_sum:
                max_len = max(max_len, j - i + 1)

    return -1 if max_len == 0 else max_len


if __name__ == '__main__':
    # 从输入读取整数列表和目标和
    ints = list(map(int, input().strip().split(',')))
    target_sum = int(input().strip())

    # 调用函数并打印结果
    print(solve_method(ints, target_sum))
