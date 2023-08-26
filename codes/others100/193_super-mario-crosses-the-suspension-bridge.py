#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 193_super-mario-crosses-the-suspension-bridge.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 193 超级玛丽过吊桥
"""


def solve(M, N, K, trap):
    bridge = [True] * (N + 2)
    for i in range(K):
        bridge[trap[i]] = False

    dp = [[0] * (M + 2) for _ in range(N + 2)]
    dp[0][M] = 1

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0]) - 1):
            k = j + 1 if not bridge[i] else j
            if i == 1:
                dp[i][j] = dp[i - 1][k]
            elif i == 2:
                dp[i][j] = dp[i - 1][k] + dp[i - 2][k]
            else:
                dp[i][j] = dp[i - 1][k] + dp[i - 2][k] + dp[i - 3][k]
    res = sum(dp[N + 1][: len(dp[0]) - 1])
    return res


if __name__ == "__main__":
    M, N, K = map(int, input().split())
    trap = list(map(int, input().split()))
    s = solve(M, N, K, trap)
    print(s)
