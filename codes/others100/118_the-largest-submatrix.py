n = int(input())
m = int(input())

ints = []


for  i in range(n):

	input_str = input()
	input_list = input_str.split(",")
	hang = []
	for j in range(m):
		hang.append(int(input_list[j]))
	ints.append(hang)


max_value= 0
for start_row in range(n):
	for start_col in range(m):
		for end_row in range(start_row, n):
			jisuan = 0
			for end_col in range(start_col, m):
				row_index = end_row
				while  row_index >= start_row:
					jisuan += ints[row_index][end_col]
					row_index -= 1

				max_value = max(max_value, jisuan)

print(max_value)