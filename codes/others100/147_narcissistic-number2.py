# encoding: utf-8
"""
@author: Yalin Feng
@file: 147_narcissistic-number2.py
@time: 2023/8/11 14:30
@project: huawei-od-python
@desc: 147 水仙花数2
"""


def check_narcissistic(num):
    bit = num
    sum_val = 0
    n = len(str(num))
    while bit != 0:
        sum_val += (bit % 10) ** n
        bit //= 10
    return sum_val == num


def split_string(string, res):
    for i in range(1, len(string) + 1):
        sub1 = string[:i]
        sub2 = string[i:]

        sub1_num = sum(map(ord, sub1))
        sub2_num = sum(map(ord, sub2))

        if check_narcissistic(sub1_num):
            if check_narcissistic(sub2_num):
                if sub1_num != 0 and sub2_num != 0:
                    if sub1_num < sub2_num:
                        res.append([sub1, sub2])
                    else:
                        res.append([sub2, sub1])
            else:
                split_string(sub2, res)


def solve_method(line: str) -> int:
    # 确保输入有效
    if len(line) > 200:
        return -1

    res = []
    split_string(line, res)

    if len(res) > 1:
        # 若分割成功且结果不唯一，返回-1
        return -1
    elif len(res) == 0 or len(res[0]) == 1:
        return 0
    else:
        # 返回分割后子串的数目
        return len(res[0])


if __name__ == '__main__':
    assert solve_method("abc") == 0
    assert solve_method("f3@d5a8") == -1
    assert solve_method("AXdddF") == 2
    assert solve_method("f3") == 0
