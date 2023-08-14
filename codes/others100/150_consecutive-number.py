# encoding: utf-8
"""
@author: Yalin Feng
@file: 150_consecutive-number.py
@time: 2023/8/11 16:00
@project: huawei-od-python
@desc: 150 求解连续数列
"""


def solve_method(S: int, N: int):
    # 用公式求解最小项
    a1 = (S - (N ** 2 - N) / 2) / N

    if abs(a1 - int(a1)) < 1e-6:
        a1 = int(a1)
        result = [num for num in range(a1, a1 + N)]
    else:
        return -1

    return result


if __name__ == '__main__':
    assert solve_method(525, 6) == [85, 86, 87, 88, 89, 90]
    assert solve_method(7, 3) == -1
