#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 279_abnormal-attendance-records.py
@time: 2023/7/14 9:29
@project: huawei-od-python
@desc: 279 异常的打卡记录
"""


def solve_method(clock_records):
    employee_records = []
    for record in clock_records:
        employee_record = EmployeeRecord(record[0], record[1], record[2], record[3], record[4])
        employee_record.set_vaild(employee_record.check_device_number())
        employee_records.append(employee_record)

    for i in range(len(employee_records)):
        for j in range(i + 1, len(employee_records)):
            if employee_records[i].id == employee_records[j].id:
                # 计算打卡时间
                time_diff = abs(employee_records[i].time - employee_records[j].time)
                # 计算打卡距离
                distance_diff = abs(employee_records[i].distance - employee_records[j].distance)
                # 如果两个打卡记录时间小于60，并且打卡距离超过5km，打卡异常
                if time_diff < 60 and distance_diff > 5:
                    employee_records[i].vaild = False
                    employee_records[j].vaild = False

    # 得到打卡异常的记录
    result = ";".join(str(record) for record in employee_records if not record.vaild)
    return "null" if len(result) == 0 else result


class EmployeeRecord:
    def __init__(self, id, time, distance, actual_device_number, registered_device_number):
        self.id = id
        self.time = time
        self.distance = distance
        self.actual_device_number = actual_device_number
        self.registered_device_number = registered_device_number
        # 打卡是否合法
        self.vaild = True

    def set_vaild(self, vaild):
        self.vaild = vaild

    def __str__(self):
        return f"{self.id},{self.time},{self.distance},{self.actual_device_number},{self.registered_device_number}"

    def check_device_number(self):
        # 实际设备号与注册设备号不一致，打卡异常
        if self.actual_device_number == self.registered_device_number:
            return True
        return False


if __name__ == '__main__':
    clockRecords = [
        ["100000", 10, 1, "ABCD", "ABCD"],
        ["100000", 50, 10, "ABCD", "ABCD"]
    ]
    assert solve_method(clockRecords) == "100000,10,1,ABCD,ABCD;100000,50,10,ABCD,ABCD"

    clockRecords = [
        ["100000", 10, 1, "ABCD", "ABCD"],
        ["100000", 80, 10, "ABCE", "ABCD"]
    ]
    assert solve_method(clockRecords) == "100000,80,10,ABCE,ABCD"

    clockRecords = [
        ["100000", 10, 1, "ABCD", "ABCD"],
        ["100000", 80, 10, "ABCE", "ABCE"]
    ]
    assert solve_method(clockRecords) == "null"
