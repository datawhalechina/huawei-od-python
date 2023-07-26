#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 008_we-are-a-team.py
@time: 2023/7/26 15:19
@project: huawei-od-python
@desc: 008 We Are A Team
"""


def solve_method(n, messages):
    result = []
    # 团队列表，每个团队都是一个set集合
    relations = []
    for message in messages:
        # 如果c为其他值，或当前行a或b超出1\~n的范围，输出da pian zi。
        if message[2] not in [0, 1] or message[0] > n or message[1] > n:
            result.append("da pian zi")
        else:
            if message[2] == 0:
                # 如果c为0，添加到对应的团队中
                set_added = False
                for relation in relations:
                    if message[0] in relation or message[1] in relation:
                        relation.add(message[0])
                        relation.add(message[1])
                        set_added = True
                        break
                if not set_added:
                    relations.append({message[0], message[1]})
            if message[2] == 1:
                # 如果c为1，判断a和b是否在一个团队
                is_team = False
                for relation in relations:
                    if message[0] in relation and message[1] in relation:
                        result.append("We are a team")
                        is_team = True
                        break

                if not is_team:
                    result.append("We are not a team")

    return result

if __name__ == '__main__':
    messages = [[1, 2, 0],
                [4, 5, 0],
                [2, 3, 0],
                [1, 2, 1],
                [2, 3, 1],
                [4, 5, 1],
                [1, 5, 1]]
    assert solve_method(5, messages) == ["We are a team", "We are a team",
                                         "We are a team", "We are not a team"]

    messages = [[1, 2, 0],
                [1, 2, 1],
                [1, 5, 0],
                [2, 3, 1],
                [2, 5, 1],
                [1, 3, 2]]
    assert solve_method(5, messages) == ["We are a team", "We are not a team",
                                         "We are a team", "da pian zi"]
