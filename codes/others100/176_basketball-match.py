#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 176_basketball-match.py
@time: 2023/8/8 23:28
@project: huawei-od-python
@desc: 176 篮球比赛
"""


def solve_method(players):
    # 从大到小排序
    players.sort(reverse=True)
    team1 = []
    team2 = []
    for player in players:
        # 所有队伍未满5人时，比较战斗力总和
        if len(team1) != 5 and len(team2) != 5:
            if sum(team1) <= sum(team2):
                team1.append(player)
            else:
                team2.append(player)
        # 某个队伍满了5人时
        else:
            # 第1队满了，则进入第2队
            if len(team1) == 5:
                team2.append(player)
            # 第2队满了，则进入第1队
            else:
                team1.append(player)
    return abs(sum(team1) - sum(team2))


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert solve_method([1, 2, 3, 4, 5, 6, 7, 8, 999, 10]) == 973
    assert solve_method([1, 2, 3, 4, 5, 6, 7, 8, 999, 1000]) == 1
