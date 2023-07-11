#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 267_count-outstanding-students.py
@time: 2023/7/11 23:49
@project: huawei-od-python
@desc: 267 优秀学员统计
"""


def solve_method(N, card_total, card_records):
    """
    :param N: 新员工数量
    :param card_total: 每天打卡的员工数量
    :param card_records: 30天每天打卡的员工id集合
    :return:
    """
    # key表示员工编号
    # value是一个元组，元组第一个数表示打卡次数，元组第二个数表示第一次打卡的时间
    card_dict = {}
    for day, item in enumerate(card_records):
        for p_id in item:
            if p_id in card_dict.keys():
                value = card_dict.get(p_id)
                count = value[0]
                card_dict[p_id] = (count + 1, value[1])
            else:
                card_dict[p_id] = (1, day + 1)

    # 首先按照打卡次数排序，然后再按照第一次打卡的时间排序，最后默认按照id排序
    sorted_card_dict = sorted(card_dict.items(), key=lambda x: (-x[1][0], x[1][1]))

    return [n[0] for n in sorted_card_dict[:5]]


if __name__ == '__main__':
    N = 11
    card_total = [4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
    card_records = [[0, 1, 7, 10],
                    [0, 1, 6, 10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [10],
                    [6, 10],
                    [7, 10]]
    assert solve_method(N, card_total, card_records) == [10, 0, 1, 7, 6]

    N = 7
    card_total = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    card_records = [
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5]
    ]
    assert solve_method(N, card_total, card_records) == [0, 1, 2, 3, 4]

    N = 2
    card_total = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
    card_records = [
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [0, 1],
        [0, 1]
    ]
    assert solve_method(N, card_total, card_records) == [1, 0]