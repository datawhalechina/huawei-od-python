#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 170_vertical-quad.py
@time: 2023/8/8 22:45
@project: huawei-od-python
@desc: 170 竖直四子棋
"""


def solve_method(s1, s2):
    # 检查是否规范，超出界限，或重溢出
    def check_valid(c):
        # 合法范围内
        if c not in [i+1 for i in range(row)]:
            return False
        # 已经满了，溢出
        if 0 not in board[c-1]:
            return False
        return True
    # 检查是否赢了
    def win(flag):
        color = 'red' if flag==1 else 'blue'
        # 竖，横，左对角线，右对角线
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        
        for i in range(row):
            for j in range(col):
                if board[i][j]==color:
                    for direction in directions:
                        dr, dc = direction
                        tmp_r, tmp_c = i, j
                        count=0
                        while 0<=tmp_r<row and 0<=tmp_c<col and board[tmp_r][tmp_c]==color:
                            count+=1
                            tmp_r+=dr
                            tmp_c+=dc
                        if count>=4:
                            return True
        return False
        
    # 行列不变，我们将棋子往y轴下坠
    row, col = list(map(int, s1.split()))
    board = [[0]*col for _ in range(row)]
    
    chess = list(map(int, s2.split()))
    flag = -1
    for ind, c in enumerate(chess):
        flag=-flag
        # 这一步落子是否有效，
        if check_valid(c):
            # 有效则添加棋子
            for i in range(col):
                if board[c-1][i]==0:
                    board[c-1][i]='red' if flag==1 else 'blue'
                    break
            # 如果放入这个棋子赢了，返回
            if win(flag):
                return str(ind+1)+',red' if flag==1 else str(ind+1)+',blue'
        else:
            return str(ind+1)+',error'
    return '0,draw'


if __name__ == '__main__':
    assert solve_method("5 5", "1 1 2 2 3 3 4 4") == '7,red'          # 横
    assert solve_method("5 5", "2 1 3 1 2 1 3 1") == '8,blue'         # 竖
    assert solve_method("5 5", "1 2 2 3 4 3 3 4 5 4 4 5") == '11,red' # 左对角
    assert solve_method("5 5", "5 4 4 3 2 3 3 2 1 2 2 1") == '11,red' # 右对角
    assert solve_method("5 5", "1 1 2 2 1 1 2 2") == '0,draw'         # 平局
    assert solve_method("5 5", "0 1 2 2 3 3 4 4") == '1,error'        # 超出范围
    assert solve_method("5 5", "1 2 2 2 2 2 2 4") == '7,error'        # 放置溢出
