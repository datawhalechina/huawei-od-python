#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 078_find-same-class-children
@time:  2023/8/23 23:57
@project:  huawei-od-python
@desc: 078 找出同班小朋友
"""


def solve_method(s):
    try:
        queue = s.split(' ')
        class1, class2 = [int(queue.pop(0).split('/')[0])], []
        prev = 1
        while queue:
            id_, flag = queue.pop(0).split('/')
            if (flag == 'Y' and prev == 1) or (flag == 'N' and prev == 2):
                class1.append(int(id_))
                prev = 1
            else:
                class2.append(int(id_))
                prev = 2
        class1 = sorted(class1)
        class2 = sorted(class2)
        if class1[0] < class2[0]:
            return '\n'.join([' '.join(map(str, class1)), ' '.join(map(str, class2))])
        else:
            return '\n'.join([' '.join(map(str, class2)), ' '.join(map(str, class1))])
    except:
        return 'ERROR'


if __name__ == '__main__':
    s = input().strip()
    res = solve_method(s)
    print(res)
