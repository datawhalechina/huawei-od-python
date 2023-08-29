#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 068_shot-competition
@time:  /2023/8/23 17:24
@project:  huawei-od-python
@desc: 068 射击比赛
"""
from collections import defaultdict


def solve_method(players, scores):
    # 选手分数字典，key为选手id，value为选手得分
    id2score = defaultdict(list)
    for player_id, score in zip(players, scores):
        id2score[player_id].append(score)

    # 如果一个选手成绩小于3个，则忽略该选手
    id2score = dict(filter(lambda x: len(x[1]) > 2, id2score.items()))
    # 累加所有选手最高三个分数之和
    id2score = {k: sum(sorted(v, reverse=True)[:3]) for k, v in id2score.items()}
    # 对总和进行从大到小、对ID进行从大到小排序
    id2score = dict(sorted(id2score.items(), key=lambda x: (-x[1], -x[0])))
    # 返回选手ID
    return [x for x in id2score.keys()]


if __name__ == '__main__':
    players = [3, 3, 7, 4, 4, 4, 4, 7, 7, 3, 5, 5, 5]
    scores = [53, 80, 68, 24, 39, 76, 66, 16, 100, 55, 53, 80, 55]
    assert solve_method(players, scores) == [5, 3, 7, 4]
