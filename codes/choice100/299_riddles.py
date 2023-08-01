#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 299_riddles.py
@time: 2023/8/1 18:27
@project: huawei-od-python
@desc: 299 猜字谜
"""


def solve_method(issues, answers):
    ans = []

    for issue in issues:
        str1 = "".join(sorted(set(issue.lower())))
        find = False

        for answer in answers:
            answer = answer.lower()
            str2 = "".join(sorted(set(answer)))

            if str1 == str2:
                ans.append(answer)
                find = True

        if not find:
            ans.append("not found")

    return ans


if __name__ == '__main__':
    assert solve_method(["conection"], ["connection", "today"]) == ["connection"]
    assert solve_method(["bdni", "wooood"], ["bind", "wrong", "wood"]) == ["bind", "wood"]
