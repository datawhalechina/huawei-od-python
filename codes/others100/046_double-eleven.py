#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 046_double-eleven.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 046 双十一
"""


def solve_method(M, R):
    """
    :param M: 商品价格数组
    :param R: 购买资金的额度
    """
    # 按照商品价格从小到大排序
    M.sort()

    # 检查是否有至少3个商品，且最便宜的3个商品的总价不超过R
    if len(M) < 3 or sum(M[:3]) > R:
        return -1

    max_price = -1
    for i in range(len(M) - 2):
        # 左指针从当前元素的下一个位置开始
        left = i + 1
        # 右指针从数组的最后一个位置开始
        right = len(M) - 1
        while left < right:
            current_sum = M[i] + M[left] + M[right]
            if max_price < current_sum <= R:
                max_price = current_sum
                left += 1
            else:
                right -= 1

    return max_price


if __name__ == '__main__':
    assert solve_method([23, 26, 36, 27], 78) == 76
    assert solve_method([23, 30, 40], 26) == -1
