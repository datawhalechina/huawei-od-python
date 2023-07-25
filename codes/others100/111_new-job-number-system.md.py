import math


def solve_method(line: str):
	split = line.split(" ")
	x = int(split[0])
	y = int(split[1])

	cb = math.pow(26, y)

	if cb > x:
		print(1)
	else:
		i = 1
		while cb * (math.pow(10, i)) < x:
			i += 1
		print(i)

line = input()
solve_method(line)

