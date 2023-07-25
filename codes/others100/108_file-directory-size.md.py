def split(string):
	"""
	逗号分隔的数字字符串解析为整数列表

	Parameters :
		string (str): 逗号分隔的数字字符串，带有方括号
	Returns:
		result (list): 解析得到的整数列表
	"""
	result = []
	trimmed_str = string[1:-1] # 除字符串的首尾方括号
	if not trimmed_str:
		return result

	while "," in trimmed_str:
		pos = trimmed_str.find(",")
		num_str = trimmed_str[:pos]
		result.append(int(num_str))
		trimmed_str = trimmed_str[pos + 1 :]

	result.append(int(trimmed_str))
	return result

data_map = {}

def dfs (n):
	"""
	深度优先搜索函数，计算给定节点 n 的结果
	
	Parameters:n (int): 
		n (int): 节点值


	Returns:
		result (int): 计算得到的结果

	"""

	result = 0
	if n in data_map:
		 data = data_map[n]
		 result = data[0]
		 for i in range(1, len(data)):
		 	result += dfs(data[i])
	return result


m, n = map(int, input().split())


# 循环读取 m 行 数据
for _ in range(m):
	a, b, c= input().split()
	a = int(a)
	b = int(b)

	data_map.setdefault(a, []).extend([b] + split(c))

res = dfs(n)

print(res)