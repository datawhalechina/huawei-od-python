# encoding: utf-8
"""
@author: Yalin Feng
@file: 148_minimum-sum-of-integers.py
@time: 2023/8/11 15:30
@project: huawei-od-python
@desc: 148 求字符串中所有整数的最小和
"""


def solve_method(string: str) -> int:
    # 检查输入是否有效
    Legal_chars = ['+', '-']
    Legal_chars.extend(list(range(10)))
    Legal_chars.extend([chr(i) for i in range(65, 65 + 26)])
    Legal_chars.extend([chr(i) for i in range(97, 97 + 26)])
    if all(set(string)) not in Legal_chars:
        return -1

    i = 0
    sum_val = 0
    chars = list(string)
    # 遍历字符串中的每一个字符
    while i < len(chars):
        c = chars[i]

        # 遇到"-"，则一直往后读取数字，直到遇到非数字字符时，让和减去该数字。
        if c == '-':
            num = 0
            while i < len(chars):
                i += 1
                if chars[i].isdigit():
                    num = num * 10 + int(chars[i])
                else:
                    sum_val += -1 * num
                    break
        elif c.isdigit():
            sum_val += int(c)
        i += 1

    return sum_val


if __name__ == '__main__':
    assert solve_method("bb1234aa") == 10
    assert solve_method("bb12-34aa") == -31
