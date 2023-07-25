res = list("123456")




def solve_method(line):
	for c in line:
		if c == "L":
			roll(0, 2, 4, 6)
		elif c == "R":
			roll(4, 6, 0, 2)
		elif c == "F":
			roll(2, 4, 4, 6)
		elif c == "B":
			roll(4, 6, 2, 4)
		elif c == "A":
			roll(2, 4, 0, 2)
		elif c == "C":
			roll(0, 2, 2, 4)

	print("".join(res))

def roll(s1, e1 , s2, e2):
	tmp = list(reversed(res[s1:e1]))
	res[s1:e1] = res[s2:e2]
	res[s2:e2] = tmp



if __name__ == "__main__":
	line = input().strip()
	solve_method(line)