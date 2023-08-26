def calculate_max_score(scores):
    n = len(scores)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # 如果当前轮次小于等于3，则总分数置0
        if i <= 3:
            dp[i] = 0
        else:
            # 选择获取该轮牌面分数
            dp[i] = dp[i - 1] + scores[i - 1]
        # 跳过该轮，将当前总分数还原为三轮前的总分数
        dp[i] = max(dp[i], dp[i - 3])

    return dp[n]

# 读取输入
scores = list(map(int, input().split(",")))

# 调用函数计算最高总分数
max_score = calculate_max_score(scores)

# 输出结果
print(max_score)