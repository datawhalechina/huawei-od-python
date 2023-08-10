#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 225_Preferred-nucleic-acid-testing-points.py
@time: 2023/8/10
@project: huawei-od-python
@desc: 225 优选核酸检测点
"""
import heapq

def solve_method(start_time, end_time, sites):
    (EIGHT_ACLOCK, TEN_ACLOCK, TWELVE_ACLOCK, FORTEEN_ACLOCK, TWENTY_ACLOCK) = \
    (8 * 60, 10 * 60, 12 * 60, 14 * 60, 20 * 60)
         
    # 模拟从出发到每个核酸点的时间变化过程
    selected = [] 

    for site in sites:
        id, distance, people = site
        time_cost = distance * 10 # 计算到达核酸点花费的时间 = 需要花费的费用
        arrive_time = start_time + time_cost    # 到达时间
        test_time = 0
        
        if arrive_time > end_time: # 到达核酸点后，若已超过结束时间，则不再模拟后续过程
            continue

        # 模拟到达核酸检测点后，前面还有多少人
        if  start_time < TEN_ACLOCK:
            # 计算 start_time - arrive_time 在 8:00 - 10:00 区间内的时长
            queue_time = min(TEN_ACLOCK, arrive_time) - max(EIGHT_ACLOCK, start_time)
            if queue_time > 0:  # 8:00 - 10:00 每分钟新增3人
                people += queue_time * (3 - 1)
        
        if start_time < TWELVE_ACLOCK: # 10:00 - 12:00 无新增
            people = max(people - (min(TWELVE_ACLOCK, arrive_time) - max(start_time, TEN_ACLOCK)), 0)

        if start_time < FORTEEN_ACLOCK:
            # 计算 start_time - arrive_time 在 12:00 - 14:00 区间内的时长
            quque_time = min(FORTEEN_ACLOCK, arrive_time) - max(TWELVE_ACLOCK, start_time)
            if quque_time > 0:  # 12:00 - 14:00 每分钟新增10人
                people += quque_time * (10 - 1)

        if start_time < TWENTY_ACLOCK and arrive_time > FORTEEN_ACLOCK: # 14:00 - 20:00 无新增
            people = max(people - (arrive_time - max(start_time, FORTEEN_ACLOCK)), 0)
        
        # 判断是否能在规定时间内完成核酸    
        if arrive_time + people <= end_time:
            selected.append((id, time_cost + people, time_cost))
            
    # 按题目要求排序        
    selected.sort(key=lambda x: (x[1], x[2], x[0])) 
    
    return len(selected), selected

# 打印输出
if __name__ == '__main__':
    while(True):
        start = 10 * 60 + 30
        end = 14 * 60 + 50
        sites = {(1, 10, 19), (2, 8, 20), (3, 21, 3)}

        assert solve_method(start, end, sites) == (2, [(2, 80, 80), (1, 190, 100)])