# encoding: utf-8
"""
@author: Yalin Feng
@file: 145_competition-rating.py
@time: 2023/8/9 23:45
@project: huawei-od-python
@desc: 145 比赛评分
"""
from collections import Counter
from typing import List


class Player(Counter):
    def __lt__(self, other):
        self_total = 0
        for k, v in self.items():
            self_total += k * v
        other_total = 0
        for k, v in self.items():
            other_total += k * v

        if self_total != other_total:
            return self_total > other_total
        else:
            for i in range(10, 0, -1):
                return self.get(i, 0) > other.get(i, 0)

        return False


def solve_method(M: int, N: int, ratings: List[List[int]]):
    """
    :param M: 评委个数
    :param N: 选手个数
    :param ratings: 选手得分
    :return:
    """
    # 检查输入参数是否满足要求(M,N,评分)
    if not (3 <= M <= 10) or not (3 <= N <= 100):
        return -1
    for row in ratings:
        if not all(1 <= num <= 10 for num in row):
            return -1

    players = []
    for i in range(N):
        scores = []
        for j in range(M):
            score = ratings[j][i]
            scores.append(score)
        # 构造选手类
        players.append([i + 1, Player(scores)])

    # 使用自定义的比较方法进行排序
    players.sort(key=lambda x: x[1])

    # 取出前3名选手
    return [x[0] for x in players[:3]]


if __name__ == '__main__':
    arr = [
        [10, 6, 9, 7, 6],
        [9, 10, 6, 7, 5],
        [8, 10, 6, 5, 10],
        [9, 10, 9, 4, 9],
    ]
    assert solve_method(4, 5, arr) == [2, 1, 5]

    arr = [
        [7, 3, 5, 4, 2],
        [8, 5, 4, 4, 3],
    ]
    assert solve_method(2, 5, arr) == -1

    arr = [
        [8, 5],
        [5, 6],
        [10, 4],
        [8, 9],
    ]
    assert solve_method(4, 2, arr) == -1

    arr = [
        [11, 6, 9, 7, 8],
        [9, 10, 6, 7, 8],
        [8, 10, 6, 9, 7],
        [9, 10, 8, 6, 7],
    ]
    assert solve_method(4, 5, arr) == -1
