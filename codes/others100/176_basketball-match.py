#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 176_basketball_match.py
@time: 2023/8/8 23:28
@project: huawei-od-python
@desc: 176 篮球比赛
"""


def solve_method(s):
    players = list(map(int, s.split()))
    total = sum(players)
    half = total // 2
    # 从大到小排序
    players.sort(reverse=True)
    team_a = []
    team_b = []
    # 从大遍历所有运动员，哪个队伍能力值总和小进入哪个队伍
    # 当某个队伍满了五个人时，剩下的人只能进入另一个队伍
    for player in players:
        # 所有队伍未满五人时
        if len(team_a)!=5 and len(team_b)!=5:
            if sum(team_a) <= sum(team_b):
                team_a.append(player)
            else:
                team_b.append(player)
        # 某个队伍满了五人时
        else:
            # a队伍满了，则进入b队伍
            if len(team_a)==5:
                team_b.append(player)
            # b队伍满了，则进入a队伍
            else:
                team_a.append(player)
    print(team_a, team_b)
    return abs(sum(team_a) - sum(team_b))


if __name__ == '__main__':
    assert solve_method("1 2 3 4 5 6 7 8 9 10") == 1
    assert solve_method("1 2 3 4 5 6 7 8 999 10") == 973
    assert solve_method("1 2 3 4 5 6 7 8 999 1000") == 1
