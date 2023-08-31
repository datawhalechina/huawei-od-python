#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 035_specific-double-ended-que.py
@time: 2023/8/1 17:39
@project: huawei-od-python
@desc: 035 特异性双端队列
"""


def solve_method(cmds):
    size = 0
    # 标识当前是否输出的顺序正确
    isSorted = True
    count = 0

    for cmd in cmds:
        if cmd.startswith("head add"):
            # 从头部添加，导致输出顺序不正常，设置标识为False
            if size > 0 and isSorted:
                isSorted = False
            size += 1
        elif cmd.startswith("tail add"):
            size += 1
        else:
            if size <= 0:
                continue

            if not isSorted:
                # 如果标识为False，则调整次数加1
                count += 1
                isSorted = True

            # 队列长度减1
            size -= 1

    return count


if __name__ == '__main__':
    cmds = ["head add 1",
            "remove",
            "tail add 2",
            "head add 3",
            "remove",
            "remove"]
    assert solve_method(cmds) == 1
