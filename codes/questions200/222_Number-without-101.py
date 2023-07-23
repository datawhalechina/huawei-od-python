#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 222_Number-without-101.py
@time: 2023/7/23
@project: huawei-od-python
@desc: 222 不含101的数
"""

def solution(l, r):
    count = 0
    x = 0b0000_0000_0000_0000_0000_0000_0000_0111

    for i in range(l, r + 1):
        n = i
        while n >= 5:
            # 看是否有101(5)
            if ((x & n) - 5) == 0:
                count += 1
                break
            n >>= 1
    return r - l + 1 - count

if __name__ == '__main__':
    while(True):
        # 处理输入格式
        l = int(input().strip())
        r = int(input().strip())
        print(solution(l, r))

        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break