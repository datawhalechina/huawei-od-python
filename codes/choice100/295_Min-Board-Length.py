def solution(N, M, length):
	'''
	N: number of boards
	M: meters of total unused boards
	length: length of each boards
	'''
	length.sort() # sort ascending
	i = 0 # index of current length of board
	for j in range(M): # use every meter
		length[i] += 1
		if i == (N - 1) or length[i + 1] >= length[i]: # greater_euqal after filling
			i = 0 # back to i=0 and refill
		else:
			i += 1 # move forward
	return sorted(length)[0] # re-sort and return minValue

if __name__ == "__main__":
	N, M = map(int, input().split())
	length = list(map(int, input().split()))
	print(solution(N, M, length))
	# print(solution(5, 10, [4,5,5,5,5]))