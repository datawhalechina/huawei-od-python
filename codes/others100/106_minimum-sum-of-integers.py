import heapq
def parse_array(line):
	return list(map(int, line.strip().split()))
def main():
	arr1= parse_array(input())
	arr2= parse_array(input())
	k = int(input())
	solve_method(arr1, arr2 , k)

def solve_method(arr1, arr2 , k):
	sums = []
	for x in arr1:
		for  y  in arr2:
			heapq.heappush(sums,x + y)
	res = 0
	for i in range(k):
		res += heapq.heappop(sums)
	print(res)





if __name__ == "__main__":
	main()