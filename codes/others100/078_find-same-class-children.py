#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 078_find-same-class-children
@time:  2023/8/23 23:57
@project:  huawei-od-python
@desc: 078 找出同班小朋友
"""


def solve_method(line):
    try:
        classes = [[], []]
        class_no = 0
        for i, p in enumerate(line):
            p_id, p_flag = p.split("/")

            if p_flag == "N":
                # 如果不同班，则换到另一个班
                class_no = not class_no

            # 进行分班
            classes[class_no].append(int(p_id))

        # 按照第一个编号小的排在第一行
        classes.sort(key=lambda x: x[0])
        return classes
    except:
        return "ERROR"


if __name__ == '__main__':
    assert solve_method(["1/N", "2/Y", "3/N", "4/Y"]) == [[1, 2], [3, 4]]
