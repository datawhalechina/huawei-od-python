#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 001_Tree -structured-query.py
@time: 2023/9/2 4:42
@project: huawei-od-python
@desc: 
"""


def split_str(s):
    """将字符串's'按空格分割并返回结果列表。"""
    return s.split()


def main():
    """主函数，用于处理树结构并打印目标节点的子节点。"""

    # 初始化一个空字典来存储树结构
    tree = {}

    # 从用户那里获取节点的数量
    n = int(input("输入节点的数量: "))

    # 读取每个节点并更新树结构
    for _ in range(n):
        a, b = split_str(input("输入由空格分隔的节点对: "))
        tree.setdefault(b, []).append(a)

    # 从用户那里获取目标节点
    target = input("输入目标节点: ")

    # 检索目标节点的子节点
    children = tree.get(target, [])
    result = []

    while children:
        node = children.pop(0)
        result.append(node)
        children.extend(tree.get(node, []))

    # 对结果进行排序并打印
    result.sort()
    for res in result:
        print(res)


# 运行主函数
if __name__ == "__main__":
    main()
