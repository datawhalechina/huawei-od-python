# def solve_method(t):
# 	print( "{}={}".format(t,t))
# 	res=1
# 	for i in range(1, int(t/2+0.99999)): #对整数的一半向上取整 因为后面的数没有可能是答案
# 		sum = i
# 		builder = "{}={}".format(t,i)
# 		for j in range(i+1, int(t/2+0.99999)):
# 			sum += j
# 			builder=builder+"+"+str(j)
# 			if sum == t:
# 				print(builder)
# 				res +=1
# 				break
		
# 	print("Result:{}".format(res))

# t= int(input().strip())
# solve_method(t)


def solve_method():
	t= int(input().strip())
	print( "{}={}".format(t,t))
	res=1
	for i in range(1, int(t/2+0.99999)): #对整数的一半向上取整 因为后面的数没有可能是答案
		m=((8*t+ (2*i-1)**2)**.5-2*i+1)/2#利用等差数数列公式求解 应为m要求大于零所以排除一个解
		if m<= int(m):
			res+=1
			print("{}={}".format(t,"+".join(map(str,range(i,i+int(m))))))
	print("Result:{}".format(res))
if __name__ == "__main__":
	solve_method()