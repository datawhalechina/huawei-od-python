#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 166_the_area_for_intersect_rectangles.py
@time: 2023/8/8 22:08
@project: huawei-od-python
@desc: 166 矩形相交的面积
"""


def solve_method(s1, s2, s3):
    areas = [s1, s2, s3]
    new_points = []
    # 输入字符串，转化为整数坐标
    # 后面两个坐标转化成正常值（变成右下角）
    for area in areas:
        x, y, w, h = list(map(int, area.split()))
        new_points.append([x, y, x+w, y-h])
    
    # 初始化一个空的相交区域为原点，记录它的左上角和右下角的坐标值
    inter_area = []
    
    # 这里我们将所有的area，每个坐标通过zip函数分别集合到一起
    # 比如三个area的左上x，左上y，右下x，右下y
    # 然后我们找左上x里的较大值（注意坐标系左负右正，上正下负），即靠右，能满足最小的矩形
    #         找左上y里的较小值，即靠下
    #         找右下x里的较小值，即靠左
    #         找右下y里的较大值，即靠上
    # 这四个极值找到后就是重叠区域的左上和右下坐标
    for ind, coro in enumerate(zip(*new_points)):
        if ind == 0 or ind==3:
            inter_area.append(max(coro))
        if ind == 1 or ind==2:
            inter_area.append(min(coro))
    # print((inter_area[0], inter_area[1]), (inter_area[2], inter_area[3]))
    
    # 右下x一定大于左上x，左上y一定大于右下x,否则不存在相交区域
    # 如果不相交，也会求取一个面积，为他们最近点围成的面积，需要去掉
    # 这个不相交的面积，下面两个判断任意一个小于等于0
    if (inter_area[2]-inter_area[0])<=0 or (inter_area[1]-inter_area[3])<=0:
        return 0
    else:
        return (inter_area[2]-inter_area[0])*(inter_area[1]-inter_area[3])


if __name__ == '__main__':
    assert solve_method("1 6 4 4", "3 5 3 4", "0 3 7 3") == 2 # 相交，面积为2
    assert solve_method("2 0 2 2", "0 2 2 2", "4 2 2 2") == 0 # 不相交，面积为0
    assert solve_method("1 7 2 2", "4 2 2 2", "8 7 2 2") == 0 # 不相交，面积为15
