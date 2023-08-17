#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:041_reverse-words 2.py
@Date：2023/08/11 0:47
"""

def solve_method(line, start, end):
    words = line.split()
    # 检查索引是否有效，如果无效则直接打印原始行
    if 0 <= start < end < len(words):
        # 交换start和end之间的单词
        while start < end:
            words[start], words[end] = words[end], words[start]
            start += 1
            end -= 1
    print(" ".join(words))

def main():
    line = input().strip()
    start, end = map(int, input().strip().split())
    solve_method(line, start, end)

if __name__ == '__main__':
    main()

