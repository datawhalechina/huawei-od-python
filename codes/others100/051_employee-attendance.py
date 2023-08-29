#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 051_employee-attendance.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 051 员工出勤
"""


def solve_method(days):
    res = []  # 初始化结果列表
    for day in days:  # 遍历每一天的状态
        absent = day.count("absent")  # 计算 "absent" 的数量
        # 检查是否有超过1个 "absent" 或连续的 "late" 或 "leaveearly"
        if absent > 1 or any(
                cur in ("late", "leaveearly") and next in ("late", "leaveearly") for cur, next in zip(day, day[1:])):
            res.append("false")  # 如果满足条件，则添加 "false" 到结果列表
            continue
        # 将每天的状态转换为整数列表，其中 "present" 转换为0，其他状态转换为1
        ints = [1 if item != "present" else 0 for item in day]
        # 检查整数列表的长度是否小于或等于7，并且总和是否大于或等于3
        if len(ints) <= 7 and sum(ints) >= 3:
            res.append("false")  # 如果满足条件，则添加 "false" 到结果列表
        else:
            # 检查任何连续的7天是否有3天或更多的非 "present" 状态
            flag = any(sum(ints[i:i + 7]) >= 3 for i in range(len(ints) - 7))
            res.append(str(not flag).lower())  # 添加结果到结果列表
    print("".join(res))  # 打印结果列表


if __name__ == "__main__":
    n = int(input())  # 读取天数
    days = [input().split() for _ in range(n)]  # 读取每一天的状态
    solve_method(days)  # 调用解决方法
