#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:055-Good friend.py
@Date：2023/08/14 21:00
"""
def solve_method(n, ints):
    # 如果n为0，则直接打印0并返回
    if n == 0:
        print(0)
        return

    # 使用列表推导式找到每个元素右侧第一个大于它的元素的位置
    # 如果没有找到，则位置为0
    res = [next((j for j in range(i + 1, n) if ints[j] > ints[i]), 0) for i in range(n)]
    # for i in range(n):
    #     pos=0
    #     for j in range(i+1, n):
    #         if ints[j] > ints[i]:
    #             pos = j
    #             break
    #     res.append(pos)

    # 打印结果
    print(*res)


if __name__ == "__main__":
    # 从用户输入中读取n和ints
    n = int(input("Enter the number of elements: "))
    ints = list(map(int, input("Enter the elements separated by space: ").split()))

    # 调用解决方案方法
    solve_method(n, ints)
