def solution(N, power, pm):
	'''
	N: number of powers
	power: [power,...]
	pm: max power
	'''
	# dp[amount-of-charger][max-power-in-total]: Actual-max-power under given condition
	dp = [[0] * (pm + 1) for _ in range(N + 1)]
	for i in range(1, N + 1):
		for v in range(min(power), pm + 1):
			if power[i - 1] > v: # current value greater than max power
				dp[i][v] = dp[i - 1][v]
			else:
				dp[i][v] = max(dp[i - 1][v], power[i - 1] + dp[i - 1][v - power[i - 1]])
	return dp[N][pm]

if __name__ == "__main__":
	N = int(input())
	power = list(map(int, input().split()))
	pm = int(input())
	print(solution(N, power, pm))
	# print(solution(4, [50, 20, 20, 60], 90))