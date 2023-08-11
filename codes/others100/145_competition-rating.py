# encoding: utf-8
"""
@author: Yalin Feng
@file: 145_competition-rating.py
@time: 2023/8/9 23:45
@project: huawei-od-python
@desc: 145 比赛评分
"""
from typing import List
from functools import cmp_to_key


def solve_method(M: int, N: int, ratings: List[List[int]]) -> str:
    # 1. 检查输入参数是否满足要求(M,N,评分)
    if not (3 <= M <= 10) or not (3 <= N <= 100):
        return "-1"
    for row in ratings:
        if not all(1 <= num <= 10 for num in row):
            return "-1"

    # 2.用 *得分频数矩阵* scores 记录选手得分情况
    # scores[i][j] 表示运动员 i 得到分数 j 的次数, scores[i][0] 表示运动员 i 得到的总分
    scores = [[0] * 11 for _ in range(101)]

    # 3.遍历评分,记录分数
    for i in range(M):
        for j in range(N):
            score = ratings[i][j]

            # 运动员编号从 1 到 N
            player_id = j + 1
            scores[player_id][0] += score  # 运动员总分增加
            scores[player_id][score] += 1  # 运动员的某个分数频数+1

    # 4. 自定义排序规则
    def compare_function(id1: int, id2: int) -> int:
        player1 = scores[id1]  # 通过运动员编号id,让player保存每个运动员的得分情况
        player2 = scores[id2]
        if player1[0] != player2[0]:  # player1[0]是1号运动员的总分
            return -1 * (player1[0] - player2[0])  # -1 是逆序; 让总分高的排前边

        # 接下来比较得分高分值的频数
        for score in range(10, -1, -1):
            if player1[score] != player2[score]:
                return -1 * (player1[score] - player2[score])  # -1 是逆序; 让得分高分值最多的选手排名靠前

        return 0

    # 5.根据记录的分数 scores 和我们定义的排序规则排序(第一名，第二名，...)
    rank = sorted(range(1, N + 1), key=cmp_to_key(compare_function))

    # 6.将前三名的id转化为string后返回
    return ",".join([str(rank[0]), str(rank[1]), str(rank[2])])


if __name__ == '__main__':
    ratings1 = [
        [10, 6, 9, 7, 6],
        [9, 10, 6, 7, 5],
        [8, 10, 6, 5, 10],
        [9, 10, 9, 4, 9],
    ]
    res1 = solve_method(4, 5, ratings1)
    print(res1)
    print(res1 == "2,1,5")

    ratings2 = [
        [7, 3, 5, 4, 2],
        [8, 5, 4, 4, 3],
    ]
    res2 = solve_method(2, 5, ratings2)
    print(res2)
    print(res2 == "-1")

    ratings3 = [
        [8, 5],
        [5, 6],
        [10, 4],
        [8, 9],
    ]
    res3 = solve_method(4, 2, ratings3)
    print(res3)
    print(res3 == "-1")

    ratings4 = [
        [11, 6, 9, 7, 8],
        [9, 10, 6, 7, 8],
        [8, 10, 6, 9, 7],
        [9, 10, 8, 6, 7],
    ]
    res4 = solve_method(4, 5, ratings4)
    print(res4)
    print(res4 == "-1")
