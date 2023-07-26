#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 011_nine-cell-key-input.py
@time: 2023/7/26 17:29
@project: huawei-od-python
@desc: 011 九宫格按键输入
"""


def solve_method(line):
    BUTTON_WORDS = [
        [' '],
        [',', '.'],
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', '1'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    mode_num = True
    result = ""
    i = 0
    while i < len(line):
        ch = line[i]
        if ch.isdigit() and ch != '0':
            if mode_num:
                # 数字模式时，直接输出对应数字
                result += ch
            else:
                pre = ch
                count = 0
                # 持续按同一个键，记录按键次数
                while i < len(line) and pre == line[i]:
                    count += 1
                    i += 1
                num = int(ch)
                button_word = BUTTON_WORDS[num]
                # 根据按键次数，把对应的字母存入结果字符串中
                word = button_word[(count - 1) % len(button_word)]
                result += word
                # 防止按同一个键时，索引i后移了一位
                i -= 1
            # 继续下一个按键
            i += 1
            continue

        if ch == "#":
            # 切换模式
            mode_num = not mode_num
        elif ch == "0":
            # 输出0或空格
            result += "0" if mode_num else " "
        # 继续下一个按键
        i += 1

    return result


if __name__ == '__main__':
    assert solve_method("2222/22") == "222222"
    assert solve_method("#2222/22") == "ab"
