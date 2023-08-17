#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:054-Shout Seven.py
@Date：2023/08/11 0:47
"""
def solve_method(line):
    numbers = list(map(int, line.split()))  # 将输入行分割为整数列表
    res = [0] * len(numbers)  # 初始化结果列表

    j = 0
    for i in range(1, 300):
        j %= len(numbers)  # 保持j在列表长度范围内
        if i % 7 == 0 or '7' in str(i):
            res[j] += 1
            if sum(res) == sum(numbers):  # 如果结果列表的总和等于输入数字的总和，终止循环
                break
        j += 1

    print(*res)  # 打印结果列表


if __name__ == "__main__":
    line = input()
    solve_method(line)  # 调用solve_method函数，并传递输入行
