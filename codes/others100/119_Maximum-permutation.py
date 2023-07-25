# def solve_method(nums):
# 	nums = [str(x) for x in nums]
# 	nums.sort(key=lambda x: x * 3,reverse=True)
# 	return int("".join (nums ))

# nums = map(int, input().strip().split(" "))
# print(solve_method(nums))


# def solve_method2(nums):
# 	nums = [str(num) for num in nums]
# 	nums .sort(key=lambda num: num * 3,reverse=True)
# 	return int("".join (nums))
# input_nums = input("") .strip().split(" ")
# nums = [int(num) for num in input_nums]
# result = solve_method(nums)
# print(result)


import itertools

def solve method(n, k):
	arr = [i + 1 for i in range(n)]
	perms = list(itertools.permutations(arr))
	res = "".join(str(x) for x in perms[k - 1])
	print(res)

if __name__ == '__main__':
	n = int(input().strip())
	k = int(input().strip())
	solve method(n, k)