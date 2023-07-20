# encoding: utf-8
from typing import List


def is_square(point1: List[int], point2: List[int], point3: List[int], point4: List[int]) -> bool:
    """第一种方法，每次组合选4个点;通过4个点判断能否构成正方形.缺点是复杂度较高，为O(n^4).
     :param point1: 第一个点的坐标,需要是列表类型,列表长度需要为2;其他三个参数以此类推
     :return: 四个点可否构成正方形
     """
    points = [point1, point2, point3, point4]
    distances = []

    # 每个点两两之间形成一条边,计算这些边的长度(的平方),保存到 distances 里
    for i in range(3):
        for j in range(i + 1, 4):
            x, y = points[i][0] - points[j][0], points[i][1] - points[j][1]
            distance = x * x + y * y
            distances.append(distance)

    # 按边的长度排序,默认是升序
    distances.sort()

    # 条件1：四条边长度相等（保证是菱形）
    # 条件2：两条对角线长度相等（一个菱形的两条对角线相等,那么这个菱形就是正方形）
    return (distances[0] == distances[1]) and (distances[1] == distances[2]) and (
            distances[2] == distances[3]) and (distances[4] == distances[5])


def method2(n: int, points: List[List[int]]) -> int:
    """第二种方法，每次组合只选2个点.并以这两个点为顶点，能构成多少个正方形.好处是O(n^2)的时间复杂度.
     :param n: 坐标个数
     :param points: 所有坐标，里面的每个元素都是长度为2的列表，表示每个点的坐标。
     :return: 四个点可否构成正方形
     """
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[j][0], points[j][1]

            x3, y3, x4, y4 = x1 + (y1 - y2), y1 - (x1 - x2), x2 + (y1 - y2), y2 - (x1 - x2)
            if [x3, y3] in points and [x4, y4] in points:
                count += 1

            x3, y3, x4, y4 = x1 - (y1 - y2), y1 + (x1 - x2), x2 - (y1 - y2), y2 + (x1 - x2)
            if [x3, y3] in points and [x4, y4] in points:
                count += 1

    # 一个正方形ABCD会被重复计算,ABCD,AB+1,BC+1,CD+1,AD+1,所以真实次数还要除以4
    count /= 4
    print(count)
    return int(count)


if __name__ == '__main__':
    # 1. 处理输入
    n = int(input())
    points = []
    for i in range(n):
        # input().split()的结果是 一个字符串列表["0","0"]
        # 我们使用 map(int,input().split()),即对input().split()的里的每个元素执行 int(),即转化为int类型
        # x,y = (int("0"),int("0")) = 0,0
        x, y = map(int, input().split())
        points.append([x, y])

    # 2.计算能构成多少个正方形
    # 方法一: 通过四重循环来不重复地挑选 4个点,通过调用 is_square 判断是否构成正方形
    count = 0
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for p in range(k + 1, n):
                    if is_square(points[i], points[j], points[k], points[p]):
                        count += 1

    # 方法二: 调用 method2，每次只选两个点
    # count = method2(n,points)

    # 3. 打印输出
    print(count)
