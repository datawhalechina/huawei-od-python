def solve_method():
	line=input().strip()
	split = line.split(",")
	num_list = []
	num_map = {}
	for item in split:
		num = int(item)
		if num not in num_list:
			num_list.append(num)
		if num in num_map:
			num_map[num] += 1
		else:
			num_map[num] = 1


	res = []
	for i in num_list:
		ints = [i, num_map[i]]
		res.append(ints)

	res.sort(key=lambda x: x[1], reverse=True)

	result = []
	for i in range(len(res)):
		result.append(str(res[i][0]))

	return ",".join(result)

if __name__ == "__main__":
	print(solve_method())
