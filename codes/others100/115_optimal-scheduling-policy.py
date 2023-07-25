n = int(input())
res = 0
preIndex = -1
for i in range(n):
	times = list(map(int, input().split()))
	if preIndex == -1:
		minTime = min(times)
		preIndex = times.index(minTime)
	else:
		minTime = min(times[:preIndex] + times[preIndex + 1:])
		preIndex = times.index(minTime)
	res += minTime
print(res)