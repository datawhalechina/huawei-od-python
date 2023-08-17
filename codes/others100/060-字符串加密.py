#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:060-字符串加密.py
@Date：2023/08/16 13:12
"""


def solve_method(strings):
    # 初始化a列表和offsets列表
    a = [1, 2, 4]
    offsets = [0] * 50

    # 计算前50个偏移量
    for i in range(len(offsets)):
        if i < 3:
            offsets[i] = a[i]
        else:
            offsets[i] = offsets[i - 1] + offsets[i - 2] + offsets[i - 3]

    # 遍历输入的字符串列表
    for str_ in strings:
        chars = list(str_)
        # 遍历字符串中的每个字符
        for i in range(len(chars)):
            c = chars[i]
            # 计算新字符的ASCII值，并将其转换为字符
            chars[i] = chr((ord(c) - 97 + offsets[i]) % 26 + 97)
        # 将字符列表连接为字符串并打印
        print(''.join(chars))


if __name__ == '__main__':
    # 读取输入的字符串数量和字符串
    n = int(input().strip())
    strings = [input().strip() for _ in range(n)]
    solve_method(strings)
