#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 007_vlan-resource-pool.py
@time: 2023/7/26 14:19
@project: huawei-od-python
@desc: 007 VLAN资源池
"""


def solve_method(pool, vlan_id):
    # 根据原资源池，得到所有可用的vlan集合
    pools = set()
    for vlan in pool:
        if "-" in vlan:
            vlan_seq = vlan.split("-")
            for i in range(int(vlan_seq[0]), int(vlan_seq[1]) + 1):
                pools.add(i)
        else:
            pools.add(int(vlan))

    # 删除申请的vlan
    if vlan_id in pools:
        pools.remove(vlan_id)

    # 将剩下的资源按从小到大排序
    pools = sorted(list(pools))

    # 得到各段的始末vlan
    result = []
    start_vlan = pools[0]
    end_vlan = start_vlan
    for i in range(1, len(pools)):
        cur_vlan = pools[i]
        if cur_vlan == end_vlan + 1:
            end_vlan = cur_vlan
        else:
            result.append((start_vlan, end_vlan))
            start_vlan = end_vlan = cur_vlan

    result.append((start_vlan, end_vlan))

    # 按题目格式输出资源池的字符串
    return [str(start) + "-" + str(end) if start != end else str(start) for start, end in result]


if __name__ == '__main__':
    assert solve_method(["1-5"], 2) == ["1", "3-5"]
    assert solve_method(["20-21", "15", "18", "30", "5-10"], 15) == ["5-10", "18", "20-21", "30"]
    assert solve_method(["5", "1-3"], 10) == ["1-3", "5"]
