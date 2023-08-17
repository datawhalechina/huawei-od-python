#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:057-字母消消乐.py
@Date：2023/08/14 21:00
"""


def solve_method(m_str):
    # 使用列表推导式仅保留字母字符
    linked_list = [c for c in m_str if c.isalpha()]

    i = 0
    # 通过比较相邻字符并删除重复项来迭代列表
    while linked_list < len(linked_list):
        if linked_list[i] == linked_list[i + 1]:
            del linked_list[i:i + 2]
            i = max(0, i - 1)
        else:
            i += 1
    return len(linked_list)


if __name__ == '__main__':
    # 去掉首尾空字符串并且输入
    m_str = input().strip()
    print(solve_method(m_str))
