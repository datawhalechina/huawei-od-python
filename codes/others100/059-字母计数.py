#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:059-字母计数.py
@Date：2023/08/16 13:12
"""
from collections import Counter


def solve_method(line: str) -> None:
    # 使用Counter计算每个字符的出现次数
    char_counter = Counter(line)

    # 对字符进行排序，首先按出现次数降序，然后按ASCII值升序
    char_count_pairs = sorted(char_counter.items(), key=lambda item: (-item[1], item[0]))

    # 打印每个字符及其出现次数
    for char, count in char_count_pairs:
        print(f"{char}:{count};", end="")
    print()


def main() -> None:
    line = input().strip()  # 读取输入的字符串
    solve_method(line)  # 调用solve_method处理字符串


if __name__ == "__main__":
    main()  # 如果是主程序，则调用main函数
