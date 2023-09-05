#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 005_numeric-sequence-comparison.py
@time: 2023/9/4 11:12
@project: huawei-od-python
@desc: 
"""
# 定义函数，接受两个列表 A 和 B 作为参数
def compare_arrays(A, B):
    # 确保 N 为 A 和 B 中较小的长度
    N = min(len(A), len(B))

    # 对列表 A 和 B 进行排序
    A.sort()
    B.sort()

    res = 0
    # 遍历列表 A 中的元素
    for i in range(N):
        numA = A[i]
        # 判断当前元素 numA 与列表 B 的第一个元素的大小关系
        if numA < B[0]:
            # 若 numA 小于列表 B 的第一个元素，则将结果变量 res 减 1，移除列表 B 的最后一个元素
            res -= 1
            B.pop()
        else:
            if numA > B[0]:
                #  numA 大于列表 B 的第一个元素，则将结果变量 res 加 1
                res += 1
            # 移除列表 B 的第一个元素
            B.pop(0)

    # 打印结果
    print(res)

# 接收数组的长度
len_arrays = int(input("Enter the length of arrays A and B: "))

# 接收用户输入并转换为整数列表
A = list(map(int, input(f"Enter {len_arrays} values for array A: ").split()))[:len_arrays]
B = list(map(int, input(f"Enter {len_arrays} values for array B: ").split()))[:len_arrays]

# 调用函数
compare_arrays(A, B)
