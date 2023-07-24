#  105-整数分解

## 题目描述

一个整数可以由连续的自然数之和来表示。
给定一个整数，计算该整数有几种连续自然数之和的表达式，并打印出每一种表达式。

## 输入描述

一个目标整数`t`，`1<=t<=100`

## 输出描述

1. 该整数的所有表达式和表达式的个数，如果有多种表达式，自然数个数最少的表达式优先输出
2. 每个表达式中按自然数递增输出
   具体的格式参见样例
   在每个测试数据结束时，输出一行 `Result:X`
   其中 X 是最终的表达式个数

## 示例描述

### 示例一

**输入：**

```
9
```

**输出：**

```
9=9
9=4+5
9=2+3+4
Result:3
```

**说明：**  
整数9有三种表达方法

### 示例二

**输入：**

```
10
```

**输出：**

```
10=10
10=1+2+3+4
Result:2
```

## 解题思路

我们可以直接用循环遍历寻找解，因为题目要求求解连续整数的解我们可以缩小范围只考虑 对整数t的一半向上取整范围内的结果。这样需要用到两个循环求解。(解法一)
如果我们利用等差数列求和公式，可以只用一个循环办到这一点。(解法二)

## 解题代码

### 解法一

```python
def solve_method():
    t= int(input().strip())
	print( "{}={}".format(t,t))
	res=1
	for i in range(1, int(t/2+0.99999)): #对整数的一半向上取整 因为后面的数没有可能是答案
		sum = i
		builder = "{}={}".format(t,i)
		for j in range(i+1, int(t/2+0.99999)):
			sum += j
			builder=builder+"+"+str(j)
			if sum == t:
				print(builder)
				res +=1
				break
		
	print("Result:{}".format(res))
if __name__ == "__main__":
	solve_method()
```
### 解法二
```python
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
```

