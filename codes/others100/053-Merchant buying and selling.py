#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:053-Merchant buying and selling.py
@Date：2023/08/11 0:47
"""


def main():
    # 读取物品数量和天数
    number, _ = map(int, input().split())
    # 读取每个物品的数量
    items = list(map(int, input().split()))
    # 读取每个物品在不同天数的价格
    prices = [list(map(int, input().split())) for _ in range(number)]
    # 调用求解函数，并打印最终结果
    print(solve(items, prices))


def solve(items, prices):
    total_sum = 0  # 初始化总和

    # 遍历每个物品的数量和价格
    for item, price in zip(items, prices):
        # 计算每个物品在不同天数的最大价格差异
        # 使用列表推导式遍历所有价格，并找到两个不同天数的价格之间的最大差值
        print("Price list for current item:", price)
        max_diff = max(price[i] - price[j] for i in range(len(price)) for j in range(i) if i != j)

        # 将最大价格差异与该物品的数量相乘，并累加到总和中
        total_sum += item * max_diff

    return total_sum  # 返回总和


if __name__ == "__main__":
    main()  # 调用主函数
