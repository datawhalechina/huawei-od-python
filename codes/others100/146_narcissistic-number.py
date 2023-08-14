# encoding: utf-8
"""
@author: Yalin Feng
@file: 146_narcissistic-number.py
@time: 2023/8/11 0:30
@project: huawei-od-python
@desc: 146 水仙花数
"""


def solve_method(N: int, M: int) -> int:
    # 检查输入是否有效
    if not (3 <= N <= 7):
        return -1

    # digit_power[i][j]表示数字i的j次幂的值
    digit_power = [[0] * (N + 1) for _ in range(10)]
    for i in range(1, 10):
        digit_power[i][0] = 1
        for j in range(1, N + 1):
            digit_power[i][j] = digit_power[i][j - 1] * i

    # 通过循环查找自幂数,注意使用 digit_power 避免重复计算
    nums = []
    start, end = 10 ** (N - 1), 10 ** N

    for num in range(start, end):
        # 保存每个数字的幂次之和
        sum_val = 0
        # 用来获取数字的每一位数
        bit = num
        while bit != 0:
            sum_val += digit_power[(bit % 10)][N]
            bit //= 10

        if sum_val == num:
            nums.append(num)

        # 如果要查找的M已经找到，提前返回
        if len(nums) == M + 1:
            return nums[-1]

    # 若M大于水仙花数的个数，返回最后一个水仙花数和M的乘积
    if M > len(nums):
        return M * nums[-1]


if __name__ == '__main__':
    assert solve_method(3, 0) == 153
    assert solve_method(9, 1) == -1
    assert solve_method(4, 0) == 1634
    assert solve_method(4, 1) == 8208
