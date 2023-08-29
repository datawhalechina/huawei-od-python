#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 192_comment-convert-output.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 192 评论转换输出
"""


def ensure_level_exists(tree, level):
    if len(tree) < level:
        # 如果本层列表不存在，则创建一个
        tree.append([])


def recursive(nodes, level, child_count, tree):
    for i in range(child_count):
        comment = nodes.pop(0)
        ensure_level_exists(tree, level)
        tree[level - 1].append(comment)
        count = int(nodes.pop(0))
        if count > 0:
            # 继续向下一层的列表中添加节点
            recursive(nodes, level + 1, count, tree)


def solve_method(line):
    nodes = line.split(",")
    tree = []
    level = 1
    while nodes:
        comment = nodes.pop(0)
        # 构建一层的节点列表
        ensure_level_exists(tree, level)
        tree[level - 1].append(comment)
        child_count = int(nodes.pop(0))
        # 继续遍历，向下一层的列表中添加节点
        recursive(nodes, level + 1, child_count, tree)

    result = []
    for nodes in tree:
        result.append(" ".join(nodes))

    return result


if __name__ == '__main__':
    line = "hello,2,ok,0,bye,0,test,0,one,1,two,1,a,0"
    assert solve_method(line) == ["hello test one", "ok bye two", "a"]

    line = "A,5,A,0,a,0,A,0,a,0,A,0"
    assert solve_method(line) == ["A", "A a A a A"]

    line = "A,3,B,2,C,0,D,1,E,0,F,1,G,0,H, 1,I,1,J,0,K,1,L,0,M,2,N,0,O,1,P,0"
    assert solve_method(line) == ["A K M", "B F H L N O", "C D G I P", "E J"]
