#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 136_service-dependencies.py
@time: 2023/7/19 9:10
@project: huawei-od-python
@desc: 136 服务依赖、服务失效判断
"""


def dfs(node, server_deps, paths):
    # 添加到故障服务中
    if node not in paths:
        paths.append(node)

    if node not in server_deps:
        return

    # 得到依赖服务
    next_node = server_deps[node]
    dfs(next_node, server_deps, paths)


def solve_method(servers, errors):
    # 服务依赖服务
    servers = servers.split(",")
    # 故障服务
    errors = errors.split(",")
    # 所有服务
    nodes = []
    # 服务依赖关系
    server_dependencies = {}
    for server in servers:
        val, next = server.split("-")
        if val not in nodes:
            nodes.append(val)
        if next not in nodes:
            nodes.append(next)
        # 建立服务依赖关系
        server_dependencies[next] = val

    paths = []
    for error in errors:
        dfs(error, server_dependencies, paths)

    # 按照顺序排除掉故障服务
    good_nodes = [node for node in nodes if node not in paths]

    return ",".join(good_nodes) if len(good_nodes) != 0 else ","


if __name__ == '__main__':
    servers = "a1-a2,a5-a6,a2-a3"
    errors = "a5,a2"
    assert solve_method(servers, errors) == "a6,a3"

    servers = "a1-a2"
    errors = "a2"
    assert solve_method(servers, errors) == ","
