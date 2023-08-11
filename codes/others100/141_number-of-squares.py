# encoding: utf-8
"""
@author: Yalin Feng
@file: 141_number-of-squares.py
@time: 2023/8/11 18:00(fix)
@project: huawei-od-python
@desc: 141 正方形数量，构成正方形的数量
"""
import itertools
from typing import List

"""
方法一: 通过不重复地挑选 4个点,通过调用 is_square 根据边长判断是否构成正方形
"""


def solve_method(points: List[List[int]]) -> int:
    # 1. 定义 is_square([points1,...,points4]= 点1,点2,点3,点4能否构成正方形
    def is_square(points: List[List[int]]) -> bool:
        assert len(points) == 4
        # 计算每个点两两之间的边长
        distances = []
        for i in range(3):
            for j in range(i + 1, 4):
                x, y = points[i][0] - points[j][0], points[i][1] - points[j][1]
                distances.append(x * x + y * y)

        distances.sort()
        # 条件1：四条边长度相等（保证是菱形）
        # 条件2：两条对角线长度相等（菱形的两条对角线相等,那么就是正方形）
        return (distances[0] == distances[1]) and (distances[1] == distances[2]) and (
                distances[2] == distances[3]) and (distances[4] == distances[5])

    # 2. 使用  itertools.combinations 生成4个点索引的不重复组合; 调用 is_square 判断点的组合能否构成正方形
    points_combination = itertools.combinations(range(len(points)), 4)
    count = 0
    for combination in points_combination:
        count += 1 if is_square([points[index] for index in combination]) else 0
    return count


"""
方法二: 每次组合只选2个点.并以这两个点为顶点，能构成多少个正方形.好处是O(n^2)的时间复杂度.
"""


def solve_method2(points: List[List[int]]) -> int:
    count = 0
    points_combination = itertools.combinations(range(len(points)), 2)
    for combination in points_combination:
        index1, index2 = combination[0], combination[1]
        x1, y1 = points[index1][0], points[index1][1]
        x2, y2 = points[index2][0], points[index2][1]

        x3, y3, x4, y4 = x1 + (y1 - y2), y1 - (x1 - x2), x2 + (y1 - y2), y2 - (x1 - x2)
        count += 1 if [x3, y3] in points and [x4, y4] in points else 0

        x3, y3, x4, y4 = x1 - (y1 - y2), y1 + (x1 - x2), x2 - (y1 - y2), y2 + (x1 - x2)

        count += 1 if [x3, y3] in points and [x4, y4] in points else 0

    # 一个正方形ABCD会被重复计算4次,所以真实次数还要除以4. 如: ABCD,AB+1,BC+1,CD+1,AD+1
    count //= 4
    return count


if __name__ == '__main__':
    points = [
        [1, 3],
        [2, 4],
        [3, 1]
    ]
    assert solve_method(points) == 0
    assert solve_method2(points) == 0

    points = [
        [0, 0],
        [1, 2],
        [3, 1],
        [2, -1]
    ]
    assert solve_method(points) == 1
    assert solve_method2(points) == 1
