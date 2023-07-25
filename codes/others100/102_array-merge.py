def solve_method():
	k =int(input().strip())
	n=int(input().strip())
	strings=[input().strip() for i in range(n)]

	builder = ""
	lists= [list(map(int, i.split(","))) for i in strings]
	index=0
	while len(lists)>0:
		linked_list= lists[index]
		for i in range(k):
			if len(linked_list) == 0:
				lists.pop(index)
				index -= 1
				break

			builder += str(linked_list.pop(0)) + ","
		index+=1
		if index >= len(lists):
			index = 0


	return builder[:-1]


if __name__ == "__main__":
	print(solve_method())
