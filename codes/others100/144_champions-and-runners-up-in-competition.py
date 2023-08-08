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

    # 初始顺序
    rank = list(range(0, nums))

    # 需要比较的轮次：n= log2(nums)的向上取整=log2(nums-1)向下取整+1
    n = int(math.log2(nums - 1)) + 1

    # 每一轮的胜者和已经产生的失败者
    win = []
    lose = []

    # 模拟法；模拟两两比赛的过程
    for epoch in range(0, n):
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
        rank = win[:]
        # 失败者不清空;但这一轮的胜利者要清空
        win.clear()

    # rank[]里只包含冠军的id,lose[]的倒数第一位是亚军
    ret = [str(rank[0]), str(lose[-1])]
    return " ".join(ret)


if __name__ == '__main__':
    res = solve_method([2, 3, 4, 5])
    print(res)
    print(res == "3 1")

    res2 = solve_method([6, 5, 4, 3, 2, 1])
    print(res2)
    print(res2=="0 4")
