#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 095_sequence-restore.py
@time: 2023/8/11 18:41
@project: huawei-od-python
@desc: 095 数列还原
"""


def solve_method(n):
    prev_chars = "1"

    # 从第2项开始生成
    for _ in range(1, n + 1):
        # 获取前一项
        current = prev_chars
        # 计数器初始化为1
        count = 1
        description = ""

        for i in range(1, len(current)):
            if current[i] == current[i - 1]:
                # 如果当前数字与前一个数字相同，计数器加1
                count += 1
            else:
                # 将计数和数字添加到描述中，重置计数器为1
                description += str(count) + current[i - 1]
                count = 1

        # 处理最后一个数字，得到前一个数的描述
        description += str(count) + current[-1]
        # 将描述保存到prev_chars变量中
        prev_chars = description

    return prev_chars


if __name__ == '__main__':
    assert solve_method(0) == "1"
    assert solve_method(4) == "111221"
