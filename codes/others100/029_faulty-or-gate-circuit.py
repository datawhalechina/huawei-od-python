#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 029_faulty-or-gate-circuit.py
@time: 2023/8/7 18:44
@project: huawei-od-python
@desc: 029 出错的或电路
"""


def solve_method(binary1, binary2):
    count = 0
    length = len(binary1)

    value = int(binary1, 2) | int(binary2, 2)
    # 遍历比特位索引
    for i in range(length):
        for j in range(i, length):
            # 交换两个比特位
            binary1_list = list(binary1)
            binary1_list[i], binary1_list[j] = binary1_list[j], binary1_list[i]

            # 计算交换后的结果
            binary1_str = "".join(binary1_list)
            result = int(binary1_str, 2) | int(binary2, 2)

            # 检查结果是否发生改变
            if result != value:
                count += 1

    return count


if __name__ == '__main__':
    assert solve_method("010", "110") == 1
    assert solve_method("011011", "110110") == 4
    assert solve_method("110", "001") == 2
