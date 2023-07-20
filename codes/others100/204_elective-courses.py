#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 204_elective-courses.py
@time: 2023/7/20 14:57
@project: huawei-od-python
@desc: 204 选修课
"""
from collections import defaultdict


def solve_method(course1, course2):
    # 选修两门课的学生信息，key为班级编号，value为(学生学号， 两门课的成绩和)
    choose_two_courses = defaultdict(list)
    for stu, score in course2.items():
        if stu in course1.keys():
            choose_two_courses[stu[:5]].append((stu, score + course1[stu]))

    if len(choose_two_courses) > 0:
        # 按照班级编号升序排序
        sorted(choose_two_courses)
        result = defaultdict(list)
        for key, value in choose_two_courses.items():
            # 按照成绩和降序、按照学号升序
            sorted(value, key=lambda x: (-x[1], int(x[0])))
            # 将学号保存到结果列表中
            result[key].extend([x[0] for x in value])

        return result
    else:
        return "NULL"


if __name__ == '__main__':
    course1 = {"01202021": 75,
               "01201033": 95,
               "01202008": 80,
               "01203006": 90,
               "01203088": 100}
    course2 = {"01202008": 70,
               "01203088": 85,
               "01202111": 80,
               "01202021": 75,
               "01201100": 88}
    assert solve_method(course1, course2) == {"01202": ["01202008", "01202021"], "01203": ["01203088"]}

    course1 = {"01201022": 75,
               "01202033": 95,
               "01202018": 80,
               "01203006": 90,
               "01202066": 100}
    course2 = {"01202008": 70,
               "01203102": 85,
               "01202111": 80,
               "01201021": 75,
               "01201100": 88}
    assert solve_method(course1, course2) == "NULL"
