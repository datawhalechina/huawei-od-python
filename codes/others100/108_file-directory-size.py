#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-27 14:30:46
# @Author  : catcooc 
# @Link    : https://github.com/catcooc
# @desc    : 108 文件目录大小


def get_dir_id(string):
    dir_ids = []
    # 除字符串的首尾括号
    trimmed_str = string[1:-1]
    if not trimmed_str:
        return dir_ids
    trimmed_str = trimmed_str.split(",")
    dir_ids = list(map(int, trimmed_str))
    return dir_ids


def dfs(n, dir_map):
    if n in dir_map and len(dir_map[n]) == 1:
        return dir_map[n][0]

    dir_size = 0
    if n in dir_map:
        data = dir_map[n]
        dir_size = data[0]
        for i in range(1, len(data)):
            dir_size += dfs(data[i], dir_map)
    return dir_size


def solve_method(n, dirs):
    dir_map = {}
    for i in range(len(dirs)):
        a, b, c = dirs[i].split()
        dir_id = int(a)
        dir_size = int(b)
        dir_map[dir_id] = [dir_size] + get_dir_id(c)

    dir_total_size = dfs(n, dir_map)
    return dir_total_size


if __name__ == "__main__":
    dirs = ["3 15 ()", "1 20 (2)", "2 10 (3)"]
    assert solve_method(1, dirs) == 45
    dirs = ["4 20 ()", "5 30 ()", "2 10 (4,5)", "1 40 ()"]
    assert solve_method(2, dirs) == 60
