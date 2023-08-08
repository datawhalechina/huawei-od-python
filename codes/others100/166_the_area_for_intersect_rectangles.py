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
    # 右下x一定大于左上x，左上y一定大于右下x。当然也可以不区分，直接相减加上绝对值
    return (inter_area[3]-inter_area[0])*(inter_area[1]-inter_area[2])


if __name__ == '__main__':
    assert solve_method("1 6 4 4", "3 5 3 4", "0 3 7 3") == 2
