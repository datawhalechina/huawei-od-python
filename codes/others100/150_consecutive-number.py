# encoding: utf-8
"""
@author: Yalin Feng
@file: 150_consecutive-number.py
@time: 2023/8/11 16:00
@project: huawei-od-python
@desc: 150 求解连续数列
"""


def solve_method(sum: int, N: int) -> str:
    # 用公式求解最小项
    a1 = (sum - (N ** 2 - N) / 2) / N

    if abs(a1 - int(a1)) < 1e-6:  # a1==int(a1) 求最小项的公式能整除,不用我们后面再验证,说明是有解的
        a1 = int(a1)
        ret = [str(num) for num in range(a1, a1 + N)]
    else:  # 不能整除,没有解
        return "-1"

    return " ".join(ret)


if __name__ == '__main__':
    res1 = solve_method(525, 6)
    print(res1)
    assert res1 == "85 86 87 88 89 90"

    res2 = solve_method(7, 3)
    print(res2)
    assert res2 == "-1"
