# encoding: utf-8
"""
@author: Yalin Feng
@file: 144_champions-and-runners-up-in-competition.py
@time: 2023/8/8 15:30
@project: huawei-od-python
@desc: 144 比赛的冠亚军
"""
import math
from typing import List


def solve_method(strengh: List[int]) -> str:
    nums = len(strengh)
    rank = list(range(0, nums))  # 初始顺序, 代表还要比赛的选手
    win = []  # 每一轮的胜者
    lose = []  # 和已经产生的失败者
    semi_final = {}  # 半决赛 对阵情况(便于输出季军)
    # 需要比较的轮次：n= log2(nums)的向上取整=log2(nums-1)向下取整+1
    n = int(math.log2(nums - 1)) + 1

    # 模拟法；模拟运动员两两比赛的过程，需要比赛n轮
    for epoch in range(0, n):
        # 如果还需比赛的选手不足 4人(半决赛)，为了便于输出季军，保存此时他们的对阵情况
        if 3 <= len(rank) <= 4:
            semi_final = {rank[0]: rank[1], rank[1]: rank[0]}
            if len(rank) == 4:
                semi_final.update({rank[2]: rank[3], rank[3]: rank[2]})

        # while 循环模拟每一轮比赛
        win.clear()
        i = 0
        while i < len(rank):
            player_id = rank[i]

            # 轮空的直接进入下一轮
            if i == len(rank) - 1:
                win.append(player_id)
                i += 1

            # 和相邻的比较
            else:
                neighbor_player = rank[i + 1]
                if strengh[player_id] >= strengh[neighbor_player]:
                    win.append(player_id)
                    lose.append(neighbor_player)
                else:
                    win.append(neighbor_player)
                    lose.append(player_id)
                # 同时处理了2个运动员;
                i += 2

        # 本轮胜出的选手参加下一轮比赛
        rank = win[:]

    # 循环终止时,rank[]里只包含冠军的id,lose[]的倒数第一位是亚军
    # 季军可以用之前的 semi_final 字典找到
    champion = rank[0]
    second_player = lose[-1]
    third_player = semi_final.get(champion, semi_final.get(second_player))
    ret = [str(champion), str(second_player), str(third_player)]
    return " ".join(ret)


if __name__ == '__main__':
    res = solve_method([2, 3, 4, 5])
    print(res)
    print(res == "3 1 2")

    res2 = solve_method([7, 6, 5, 4, 3, 2, 1, 0])
    print(res2)
    print(res2 == "0 4 2")
