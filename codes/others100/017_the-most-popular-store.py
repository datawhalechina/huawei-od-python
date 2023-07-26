#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 017_the-most-popular-store.py
@time: 2023/7/26 21:21
@project: huawei-od-python
@desc: 017 人气最高的店铺
"""
import math
from collections import defaultdict


def check_shop1_max_ticket(change_list):
    global money, shop_ticket
    temp_map = shop_ticket.copy()
    money = 0
    # 1号店铺加票，其他店铺减票，并累加发放购物补贴金额
    for shop_id, shop_money in change_list:
        money += shop_money
        temp_map[shop_id] -= 1
        temp_map[1] += 1

    sorted_shop = sorted(temp_map.items(), key=lambda x: -x[1])

    # 获取当前得票最多的店铺ID
    first_shop_id = sorted_shop[0][0]
    # 检查是否为1号店铺，或者1号店铺是否为得票最多的店铺
    if first_shop_id == 1 and (len(sorted_shop) == 1 or sorted_shop[0][1] > sorted_shop[1][1]):
        return True
    return False


def backstracking(tickets, change_list, index):
    global min_money, money
    # 如果是1号店铺得票最多，则获取最少的发放购物补贴金额
    if check_shop1_max_ticket(change_list) and min_money > money:
        min_money = money
        return

    for i in range(index, len(tickets)):
        change_list.append(tickets[i])
        backstracking(tickets, change_list, i + 1)
        change_list.pop()


def solve_method(tickets):
    global shop_ticket, min_money
    # 最少发放购物补贴金额
    min_money = math.inf
    # 店铺票数字典，key为店铺号，value为店铺所得票数
    shop_ticket = defaultdict(int)
    shop_ticket[1] = 0
    for ticket in tickets:
        shop_id = ticket[0]
        shop_ticket[shop_id] += 1

    # 使用回溯法
    backstracking(tickets, [], 0)

    return min_money


if __name__ == '__main__':
    tickets = [[2, 10], [3, 20], [4, 30], [5, 40], [5, 90]]
    assert solve_method(tickets) == 50

    tickets = [[2, 10], [3, 20], [4, 30], [5, 80], [5, 90]]
    assert solve_method(tickets) == 60
