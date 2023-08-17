#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:046_双十一.py
@Date：2023/08/11 0:47
"""
def main():
    m = input()
    r = int(input())
    goods_prices = sorted(map(int, m.split(',')))

    # 检查是否有至少3个商品，且最便宜的3个商品的总价不超过r
    if len(goods_prices) < 3 or sum(goods_prices[:3]) > r:
        print(-1)
        return

    # 寻找所有可能的组合，并找到总价最接近但不超过r的组合
    res = -1
    # 通过三重循环来遍历所有可能的3个商品的组合，从而消除了递归函数,这种方法只能用于较小的数据集
    for i in range(len(goods_prices)):
        for j in range(i + 1, len(goods_prices)):
            for k in range(j + 1, len(goods_prices)):
                total_price = goods_prices[i] + goods_prices[j] + goods_prices[k]
                if total_price > res and total_price <= r:
                    res = total_price

    print(res)

if __name__ == '__main__':
    main()

