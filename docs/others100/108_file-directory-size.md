#  108-文件目录大小

## 题目描述

一个文件目录的数据格式为:目录 id，本目录中文件大小，(子目录 id 列表)。其中目录 id 全局唯一，取值范围[1,200]，本目录中文件大小范围[1,1000]，子目录 id 列表个数[0,10]
例如: 1 20(2,3) 表示目录 1 中文件总大小是 20，有两个子目录，id 分别是 2 和3
现在输入一个文件系统中所有目录信息，以及待查询的目录 id，返回这个目录和及该目录所有子目录的大小之和。

## 输入描述

第一行为两个数字 M，N，分别表示目录的个数和待查询的目录 id，1 <= M <=100,1<= N <=200
接下来 M 行，每行为 1个目录的数据: 目录 id 本目录中文件大小(子目录 id 列表)，子目录列表中的子目录 id 以逗号分隔.

## 输出描述

待查询目录及其子目录的大小之和

## 补充说明

不用考虑输入数据不合法的情况；假设最多100 个输入文件。

## 示例描述

### 示例一

**输入：**

```
3 1
3 15 ()
1 20 (2)
2 10 (3)
```

**输出：**

```
45
```

**说明：**  

目录 1大小为 20，包含一个子目录2 (大小为 10)，子目录 2包含一个子目录 3 (大小为 15)，总的大小为 20+10+15=45.

### 示例二

**输入：**

```
4 2
4 20 ()
5 30 ()
2 10 (4,5)
1 40 ()
```

**输出：**

```
60
```

**说明**

目录 2 包含 2 个子目录4和 5，总的大小为 10+20+30 = 60

## 解题思路



## 解题代码

```python
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
```