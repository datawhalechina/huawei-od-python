#!/usr/bin/env python
# encoding: utf-8
"""
@author: Yalin Feng
@file: 146_narcissistic_number.py
@time: 2023/8/11 0:30
@project: huawei-od-python
@desc: 146 水仙花数
"""
from typing import List


from typing import List


def solve_method(N: int, M: int) -> int:
    # 1. 检查输入是否有效
    if not (3 <= N <= 7):
        return -1

    # 2. 空间换时间: 制作一个数字 0 到 9 的 n次方的"哈希表"(这里用二维列表)，避免后续重复计算一个数字的 n次方
    # digit_power[i][j] 数字i 的 j次幂的值
    digit_power = [[0] * (N + 1) for _ in range(10)]
    for i in range(1, 10):
        digit_power[i][0] = 1
        for j in range(1, N + 1):
            digit_power[i][j] = digit_power[i][j - 1] * i

    # 3.通过循环查找自幂数,注意使用 digit_power 避免重复计算
    nums: List[int] = []
    start, end = 10 ** (N - 1), 10 ** N

    for num in range(start, end):
        sum = 0			# 保存每个数字的幂次之和
        num_copy = num 	# 用来获取数字的每一位数
        while num_copy != 0:
            sum += digit_power[(num_copy % 10)][N]
            num_copy //= 10

        if sum == num:
            nums.append(num)

        # 提前返回: 如果要查找的 M 已经找到,提前返回(注意M类似索引,从0开始，而自幂数列表的长度比索引多1)
        if len(nums) == M + 1:
            return nums[-1]

    # 4. 若`M`大于水仙花数的个数，返回最后一个水仙花数和 `M`的乘积。
    return nums[M] if M < len(nums) else M * nums[-1]


if __name__ == '__main__':
    res1 = solve_method(3, 0)
    print(res1)
    assert res1 == 153

    res2 = solve_method(9, 1)
    print(res2)
    assert res2 == -1

    res3 = solve_method(4, 0)
    print(res3)
    assert res3 == 1634

    res4 = solve_method(4, 1)
    print(res4)
    assert res4 == 8208
