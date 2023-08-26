#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 192_comment-convert-output.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 192 评论转换输出
"""

def ensure_level_exists(tree,level):
    if len(tree) < level:
        tree.append([])


def print_tree(tree) :
    print(len (tree))
    for nodes in tree:
        print(" ".join (nodes) )
def recursive (nodes, level, child_count, tree) :
    for i in range (child_count):
        comment = nodes. pop(0)
        ensure_level_exists(tree,level)
        tree[level - 1 ].append(comment)
        count = int(nodes.pop(0))
        if count > 0:
            recursive(nodes, level + 1,count, tree)



def main():
    comments = input().split(",")

    tree = []
    nodes = comments.copy()

    level = 1
    while nodes:
        comment = nodes.pop(0)
        ensure_level_exists(tree, level)
        tree[level - 1].append(comment)
        child_count = int(nodes.pop(0))
        recursive(nodes, level + 1, child_count, tree)

    print_tree(tree)

main()
