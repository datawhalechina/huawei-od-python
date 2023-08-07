#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiHongYu
@file: 029_faulty-or-gate-circuit.py
@time: 2023/8/7 18:44
@project: huawei-od-python
@desc: 029 出错的或电路
"""


def solve_method(binary1, binary2):
    # 先统计第1个二进制数的0与1的次数，方便后续计算次数改变
    cnt_binary1_1 = binary1.count('1')
    cnt_binary1_0 = binary1.count('0')

    # 存储结果
    count = 0

    # 遍历第2个二进制数的每一位
    for i in range(len(binary1)):
        # 遇到0时，分类计数
        if binary2[i] == '0':
            # 当第2个二进制数的某一位为1时，无论第1个二进制数对应的位改变了为什么，都不会影响结果。
            # 当某一位为0时，这时就会影响结果：
            # 当第1个二进制数的该位为1时，1|0=1变为0|0=0，那么统计第1个二进制数的所有0的次数，就是让电路改变结果的次数。
            # 当第1个二进制数的该位为0时，0|0=0变为1|0=1，同上，统计第1个二进制数的所有1的次数。
            if binary1[i] == '1':
                count += cnt_binary1_0
            if binary1[i] == '0':
                count += cnt_binary1_1
    return count


if __name__ == '__main__':
    assert solve_method("010", "110") == 1
    assert solve_method("011011", "110110") == 4
    assert solve_method("110", "001") == 2
