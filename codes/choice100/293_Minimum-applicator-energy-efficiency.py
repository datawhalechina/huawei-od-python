def solution(M, N, fields):
	if N < len(fields):
		return -1 # failed
	l = 1 # min velocity, left
	res = r = max(fields) # max velocity, right
	while l <= r:
		m = (l + r) // 2
		hour = sum(list(map(lambda x : x // m if x % m == 0 else (x // m) + 1, fields)))
		if hour <= N: # equal
			r = m - 1
			res = min(res, m)
		else: # over time
			l = m + 1
	return res


if __name__ == "__main__":
	M, N = map(int, input().split()) # M: numbers N: days
	fields = list(map(int, input().split()))
	res = solution(M, N, fields)
	print(res)