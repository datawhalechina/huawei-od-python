#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 068_shot-competition
@time:  23/8/2023 下午 5:24
@project:  huawei-od-python 
"""


def solve_method(id_lst, score_lst):
    id2score = dict()
    for id_, score in zip(id_lst, score_lst):
        if id_ not in id2score:
            id2score[id_] = [score]
        else:
            id2score[id_].append(score)
    items = filter(lambda x: len(x[1]) > 2, list(id2score.items()))
    items = [[id_, sum(sorted(scores)[:3])] for id_, scores in items]
    items = sorted(items, key=lambda x: (x[1], x[0]), reverse=True)
    return ','.join([str(item[0]) for item in items])


if __name__ == '__main__':
    n = int(input().strip())
    id_lst = list(map(int, input().strip().split(',')))
    score_lst = list(map(int, input().strip().split(',')))
    res = solve_method(id_lst,score_lst)
    print(res)
