def solve_method():
	s = input().split(" ")

	len_s = len(s)
	list_s = []

	for i in range(len_s):
		if s[i] == "J":
			list_s.append(11)
		elif s[i] == "Q":
			list_s.append(12)
		elif s[i] =="K":
			list_s.append(13)
		elif s[i] =="A":
			list_s.append(14)
		elif s[i] != "2":
			list_s.append(int(s[i]))


	list_s.sort()


	ress = []
	is_a = False

	while not is_a:
		res = [list_s[0]]
		count = 1

		for i in range(1, len(list_s)):
			x = list_s[i]

			if x == list_s[i - 1] + 1 :
				count += 1
				res.append(x)
			elif x == list_s[i - 1] and i != len(list_s) - 1:
				continue

			if x != list_s[i-1] + 1 or i == len(list_s) - 1:
				if count >= 5:
					ress.append(res)
				elif i == len(list_s) -1 :
					is_a = True
					break

				for j in range(len(res)):
					for k in range(len(list_s)):
						if res[j] == list_s[k]:
							list_s.pop(k)
							break


				if len(list_s) < 5 :
					is_a = True


				break


	if len(ress) == 0:
		print("No")
	else:
		for i in range(len(ress)):
			string_res = " "
			for j in range(len(ress[i])):
				if ress[i][j] == 11:
					string_res += "J"
				elif ress[i][j] == 12:
					string_res += "Q"
				elif ress[i][j] == 13:
					string_res += "K"
				elif ress[i][j] == 14:
					string_res += "A"
				else:
					string_res += str(ress[i][j])
				

				if i < len(ress[i]) - 1:
					string_res += " "

			print(string_res)


if __name__ == "__main__":
	solve_method()