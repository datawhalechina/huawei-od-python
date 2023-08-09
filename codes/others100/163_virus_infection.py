#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 163_virus_infection.py
@time: 2023/8/8 21:27
@project: huawei-od-python
@desc: 163 病毒感染
"""


def solve_method(s):
    s = s.split(',')
    n = len(s)
    # 因为行列相等，直接开方
    row = col = int(n**0.5)

    # 一维数组切分成二维数组，方便遍历
    places = []
    for i in range(0, n, row):
        places.append(s[i:i+row])
        
    # 先将病毒的初始位置记录下来
    virus = []
    for i in range(row):
        for j in range(col):
            if places[i][j]=='1':
                virus.append((i,j))
    # 记录天数，每次广度优先搜索一次，天数+1
    days = 0
    # 从病毒的初始位置开始，广度优先搜索
    while virus:
        tmp = []
        while virus:
            i, j = virus.pop()
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0<=x<row and 0<=y<col and places[x][y]=='0':
                    tmp.append((x, y))
                    places[x][y]='1'
        virus = tmp
        if not virus:
            break
        else:
            days+=1
    return days if days else -1


if __name__ == '__main__':
    assert solve_method("1,0,1,0,0,0,1,0,1") == 2
    assert solve_method("0,0,0,0") == -1
    assert solve_method("1,1,1,1,1,1,1,1,1") == -1
    assert solve_method("1") == -1
    assert solve_method("0,1,1,0") == 1
