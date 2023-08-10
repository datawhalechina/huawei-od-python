#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 088_recruitment.py
@time: 2023/8/10 15:55
@project: huawei-od-python
@desc: 088 招聘
"""


def solve_method(m, interviews):
    """
    :param m: 面试官的最多面试人次
    :param interviews: 面试时间，每场面试的起始时间和结束时间
    :return:
    """
    interviews.sort(key=lambda x: x[0])
    # 面试官，每个元素有两个值，第一个值表示面试官的面试结束时间，第二个值表示面试官的面试次数
    interviewer = []
    for interview in interviews:
        # 如果面试官的上一轮的面试结束时间小于当前面试者的开始时间，并且面试次数没有达到m次，则表示可用
        interviewer_mask = [True if x[0] <= interview[0] and x[1] < m else False for x in interviewer]
        if any(interviewer_mask):
            # 如果存在空闲的面试官，则分配面试
            i = interviewer_mask.index(True)
            interviewer[i][1] += 1
            interviewer[i][0] = interview[1]
        else:
            # 如果没有空闲，则新增1位面试官
            interviewer.append([interview[1], 1])

    return len(interviewer)


if __name__ == '__main__':
    arr = [[1, 2],
           [2, 3],
           [3, 4],
           [4, 5],
           [5, 6]]
    assert solve_method(2, arr) == 3

    arr = [[1, 2],
           [2, 3],
           [3, 4]]
    assert solve_method(3, arr) == 1
