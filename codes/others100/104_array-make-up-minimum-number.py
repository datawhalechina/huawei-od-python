def solve_method():
	line= input()
	arr = line.split(",")
	len_arr = len(arr)
	arr.sort()
	if len_arr <=2:
		print(''.join(map(str,arr)))
	else:
		print(''.join(map(str,arr[:3])))



if __name__ == "__main__":
	solve_method()