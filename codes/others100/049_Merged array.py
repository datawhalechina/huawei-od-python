#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:049_Merged array.py
@Date：2023/08/11 0:47
"""
from typing import List


def solve_method(length: int, arrays: List[str]) -> None:
    lists = [array.split(",") for array in arrays]  # 将输入的字符串数组转换为列表
    res = []  # 用于存储最终结果的列表

    # 当还有未处理的元素时，继续处理
    while any(lists):
        for str_list in lists:
            # 每次从当前列表中取出最多length个元素
            res += str_list[:length]
            del str_list[:length]

    # 打印结果
    print(",".join(res))


if __name__ == "__main__":
    length = int(input())
    num = int(input())
    arrays = [input() for _ in range(num)]  # 读取num个数组
    solve_method(length, arrays)
