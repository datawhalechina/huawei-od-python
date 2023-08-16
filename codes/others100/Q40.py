#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:Q40.py
@Date：2023/08/11 0:47
"""


def solve_method(line, l, r):
    words = line.strip().split()
    r = min(r, len(words) - 1)

    if len(words) == 0 or l < 0 or r - l <= 0:
        print("EMPTY")
        return

    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1

    print(" ".join(words))


def main():
    line = input().strip()
    l = int(input().strip())
    r = int(input().strip())
    solve_method(line, l, r)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
