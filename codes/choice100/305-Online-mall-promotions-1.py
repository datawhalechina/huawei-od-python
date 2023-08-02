#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 305-Online-mall-promotions-1.py
@time: 2023/8/2 11:38
@project: huawei-od-python
@desc: 305 网上商城优惠活动（一）
"""


def full_discount(res, ticket):
    """
    满减规则
    :param res: 总价
    :param ticket: 满减券数量
    :return: 总价满减后结果，对应数组含义是 (用券后剩余总价， 使用满减券数量)
    """
    # 满100最多用1张满减券，满200最多用2张满减券....
    # price总价最多使用price/100张券
    use_tickets = 0
    max_count = int(res / 100)
    # 实际可使用的满减券数量
    count = min(ticket, max_count)

    res -= count * 10
    ticket -= count
    use_tickets += count
    return res, use_tickets


def discount(res, ticket):
    """
    打折规则
    :param res: 总价
    :param ticket: 打折券数量
    :return: 总价打折后结果，对应数组含义是 (用券后剩余总价， 使用打折券数量)
    """
    use_tickets = 0
    if ticket > 0:
        res = int(res * 0.92)
        use_tickets += 1
    return res, use_tickets


def threshold_free(res, ticket):
    """
    无门槛规则
    :param res: 总价
    :param ticket: 无门槛券数量
    :return: 门槛券用后结果，对应数组含义是 (用券后剩余总价， 使用无门槛券数量)
    """
    use_tickets = 0
    while res > 0 and ticket > 0:
        res -= 5
        # 避免无门槛券过多会导致优惠后总价小于0
        res = max(res, 0)
        ticket -= 1
        use_tickets += 1
    return res, use_tickets


def solve_method(t1, t2, t3, prices):
    """
    :param t1: 满减的优惠券
    :param t2: 打折的优惠券
    :param t3: 无门槛的优惠券
    :param prices: 用户的购物价格
    :return:
    """
    result = []
    for price in prices:
        res_t1, tickets_t1 = full_discount(price, t1)
        res_t2, tickets_t2 = discount(price, t2)
        res_t3, tickets_t3 = threshold_free(price, t3)
        tickets_res = 0
        if price < 100:
            if price <= 62 and t3 > 0:
                # 先使用无门槛券，再使用打折券
                res, tickets_res = discount(res_t3, t2)
                tickets_res += tickets_t3
            else:
                # 先使用打折券，再使用无门槛券
                res, tickets_res = threshold_free(res_t2, t3)
                tickets_res += tickets_t2

            result.append([res, tickets_res])
            continue

        if res_t1 < res_t2:
            copy_res = res_t1
            tickets_res += tickets_t1
            # 先使用满减券，再使用无门槛券
            r3, tickets_r3 = threshold_free(res_t1, t3)
            # 或者先使用满减券，再使用打折券
            r2, tickets_r2 = discount(copy_res, t2)
            if r3 < r2:
                res = r3
                tickets_res += tickets_r3
            else:
                res = r2
                tickets_res += tickets_r2
        else:
            copy_res = res_t2
            tickets_res += tickets_t2
            # 先使用打折券，再使用无门槛券
            r3, tickets_r3 = threshold_free(res_t2, t3)
            # 或者使用打折券，再使用满减券
            r1, tickets_r1 = full_discount(copy_res, t1)
            if r3 < r1:
                res = r3
                tickets_res += tickets_r3
            else:
                res = r1
                tickets_res += tickets_r1

        result.append([res, tickets_res])

    return result


if __name__ == '__main__':
    assert solve_method(3, 2, 5, [100, 200, 400]) == [[65, 6], [155, 7], [338, 4]]
