n = input()
lst = []
for i in range(int(n)):
	lst.append(int(input()) )
uniq = set(lst)
lst = list(uniq)
lst.sort()

for i in lst:
	print(i)