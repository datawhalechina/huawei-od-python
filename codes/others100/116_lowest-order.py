COMMA = ","

def solve_method(line):
	nums = line.split(COMMA)
	list_ = [int(num) for num in nums]
	list_.sort(key=lambda x: abs(x) % 10)


	result = [str(x) for x in list_ ]
	print(COMMA.join(result))

line = input()
solve_method(line)