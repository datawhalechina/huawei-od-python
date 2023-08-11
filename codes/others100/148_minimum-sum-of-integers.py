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
    allowed_character = ['+', '-']
    allowed_character.extend(list(range(10)))
    allowed_character.extend([chr(i) for i in range(65, 65 + 26)])
    allowed_character.extend([chr(i) for i in range(97, 97 + 26)])
    assert all(set(string)) in allowed_character

    # 遍历字符串中的每一个字符
    i = 0   # 索引,使用while循环便于我们手动改变i的值
    sum = 0 # 返回的最小和
    chars = list(string)
    while i < len(chars):
        c = chars[i]

        # 遇到"-"，则贪心地往后读取数字，直到遇到非数字字符时，让和减去该数字，出循环。
        if c == '-':
            num = 0
            while i < len(chars):
                i += 1
                if chars[i].isdigit():
                    num = num * 10 + int(chars[i])
                else:
                    sum += -1 * num
                    break

        elif c.isdigit():
            sum += int(c)

        i += 1

    return sum


if __name__ == '__main__':
    res1 = solve_method("bb1234aa")
    print(res1)
    assert res1 == 10

    res2 = solve_method("bb12-34aa")
    print(res2)
    assert res2 == -31
