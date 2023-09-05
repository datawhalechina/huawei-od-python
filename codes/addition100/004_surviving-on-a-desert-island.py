#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 004_surviving-on-a-desert-island.py
@time: 2023/9/4 11:11
@project: huawei-od-python
@desc: 
"""


def main():
    # 输入字符串，获取数字列表
    nums = [int(x) for x in input().split()]

    # 将正数放入右侧列表，负数的绝对值放入左侧列表
    left = [abs(x) for x in nums if x <= 0]
    right = [x for x in nums if x > 0]
    # 迭代处理左侧和右侧列表
    while right and left:
        if left[-1] > right[-1]:
            left[-1] -= right.pop()
        elif left[-1] < right[-1]:
            right[-1] -= left.pop()
        else:
            left.pop()
            right.pop()

    # 输出最终列表的长度之和
    print(len(right)+len(left))


# 调用主函数
if __name__ == "__main__":
    main()
