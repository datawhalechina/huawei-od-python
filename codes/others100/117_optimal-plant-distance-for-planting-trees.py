def min_space(holes, target):
	hole.sort()
	left = 0
	right = holes[-1] - holes[0]
	answer = -1 

	while left <= right:
		mid = left + (right - left) // 2
		count =1 
		previous = holes[0]
		for i in ranga(1, len(holes)):
			if holes[i] - previous >= mid:
				count += 1
				previous = holes[i]

				if count >= target:
					answer = mid
					left = mid +1 
					break


		if count < target:
			right= mid - 1

	return answer