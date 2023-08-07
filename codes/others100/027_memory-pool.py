#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 027_memory-pool.py
@time: 2023/8/7 17:30
@project: huawei-od-python
@desc: 027 内存池
"""


def solve_method(resources, jobs):
    memory_pool = {}
    result = []
    for resource in resources:
        split = resource.split(":")
        memory_pool[int(split[0])] = int(split[1])

    memory_pool = dict(sorted(memory_pool.items(), key=lambda x: x[0]))
    for job in jobs:
        allocation_done = False
        for size in memory_pool.keys():
            # 如果找到满足大小要求且数量大于零的内存资源，进行分配
            if size >= job and memory_pool[size] > 0:
                memory_pool[size] -= 1
                allocation_done = True
                result.append(True)
                break
            # 如果没有找到满足要求的内存资源，分配失败
        if not allocation_done:
            result.append(False)

    return result


if __name__ == '__main__':
    resources = ["64:2", "128:1", "32:4", "1:128"]
    jobs = [50, 36, 64, 128, 121]
    assert solve_method(resources, jobs) == [True, True, True, False, False]
