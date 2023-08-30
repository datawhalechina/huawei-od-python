#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 051_employee-attendance.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 051 员工出勤
"""


def solve_method(records):
    result = []
    for record in records:
        # 缺勤如果超过1次，没有出勤奖
        if record.count("absent") > 1:
            result.append("false")
            continue

        # 如果有连续的迟到、早退，没有出勤奖
        prev = record[0]
        for day in records[1:]:
            if prev in ["late", "leaveearly"] and day in ["late", "leaveearly"]:
                result.append("false")
                continue

        if len(record) <= 3:
            result.append("true")
        else:
            # 检查任何连续的7天是否有4天或更多的正常上班状态
            flag = all([record[i:i + 7].count("present") >= 4 for i in range(len(record) - 6)])
            result.append(str(flag).lower())

    return result


if __name__ == "__main__":
    records = [["present"],
               ["present", "present"]]
    assert solve_method(records) == ["true", "true"]

    records = [["present"],
               ["present", "absent", "present", "present", "leaveearly", "present", "absent"]]
    assert solve_method(records) == ["true", "false"]

    records = [["present"],
               ["present", "present", "late", "present", "leaveearly", "present", "leaveearly", "present", "late",
                "present"]]
    assert solve_method(records) == ["true", "false"]
