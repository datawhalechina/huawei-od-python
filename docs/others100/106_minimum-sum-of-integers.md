#  106-整数对最小和

## 题目描述

给定两个整数数组 array1array2,数组元素按升序排列。假设从 array1 array2 中分别取出一个元素可构成一对元素。现在需要取出 K 个元素，并对取出的所有元素求和。计算和的最小值
注意:两对元素如果对应于 array1 array2 中的两个下标均相同，则视为同一个元素。

## 输入描述

输入两行数组 array1array2

每行首个数字为数组大小 size(0 < size <= 100 )
0 < array1(i) <= 1000
0 < array2(i) <= 1000
接下来一行为正整数 k ( 0< k <= array1.size() * array2.size() )

## 输出描述

满足要求的最小和

## 示例描述

### 示例一

**输入：**

```text
3 1 1 2
3 1 2 3
2
```

**输出：**

```text
4
```

**说明：** 
用例中，需要取两个元素 取第一个数组第0个元素 与第二个数组第0个元素，组成一对元素`[1,1]`
取第一个数组第 1个元素 与第二个数组第0个素，组成一对元素[1,1]求和为 `1+1+1+1=4` 为满足要求的最小和

## 解题思路

### 解法一

**基本思路：**`heapq.heappush()`是往堆中添加新值，此时自动建立了小根堆

1. 计算最大需要相加到数组的范围
2. 先判断是否存在长度为1的数组 如果存在，直接取该数组元素和另一个数组前k个元素的相加返回为结果。
3. 如果没有长度为1的数组 则再最大可以相加到的范围内按顺序遍历两数组的和 加入到堆sum中。
4. 弹出堆的前k个值 累加得到结果。

### 解法二

**基本思路：**

1. 调换数组顺序，将短数组赋给arr1，为了后面遍历用短数组因为都是最短的数组先被抽取完。
2. 先判断是否存在长度为1的数组 如果存在，直接取该数组元素和另一个数组前k个元素的相加返回为结果。
3. 如果没有长度为1的数组 ，利用Counter函数生成一个关于arr1包含所有不同值`num`以及该值对应存在元素个数`num_count`的列表。
4. 遍历这个列表，优先把前面小的值和长数组的元素相加。
5. 返回结果。

## 解题代码

### 解法一

```python
import heapq
def parse_array(line):
	return list(map(int, line.strip().split()))

def solve_method_1(arr1, arr2 , k):
	arr1=parse_array(arr1)
	arr2=parse_array(arr2)
	k=int(k)
	#计算最大需要相加到数组的范围
	len_addarr1=min(k+1,arr1[0]+1)
	len_addarr2=min(k+1,arr2[0]+1)
	#如果含有长度为一的数组我们直接返回取该数组元素和另一个数组前k个元素的相加
	if arr1[0]==1:
		return arr1[1]*k+sum(arr2[1:len_addarr2])
	elif arr2[0]==1:
		return arr2[1]*k+sum(arr1[1:len_addarr1])
	sums = []
	for x in arr1[1:len_addarr1]:
		for  y  in arr2[1:len_addarr2]:
			heapq.heappush(sums,x + y)
			
	res = 0
	for i in range(k):
		res += heapq.heappop(sums)
	return (res)


if __name__ == "__main__":
	assert solve_method_1("1 1","3 1 2 3" ,"2") == 5 
	assert solve_method_1("3 1 1 2","3 1 2 3" ,"2") == 4 
	assert solve_method_1("3 1 1 1","3 1 2 3" ,"3") == 6
	assert solve_method_1("3 1 1 ","3 1 2 3" ,"5") == 14
	assert solve_method_1("3 1 1 ","3 1 2 3" ,"6") == 18
```

### 解法二

```python
from collections import Counter

def parse_array(line):
	return list(map(int, line.strip().split()))
def solve_method_2(arr1, arr2 , k):
	arr1=parse_array(arr1)
	arr2=parse_array(arr2)
	k=int(k)
	#调换数组顺序为了后面用短数组排序 因为无论k多大都是短的数组先被抽取完
	if arr1[0]> arr2[0]:
		arr1 , arr2=arr2 , arr1

	len_addarr1=min(k+1,arr1[0]+1)
	
	#如果含有长度为一的数组我们直接返回取该数组元素和另一个数组前k个元素的相加
	if arr1[0]==1:
		return k*arr1[1]+sum(arr2[1:k+1])

	arr2_position=1
	res=0
#优先计算前面的小的数相加
	for num, num_count in Counter(arr1[1:]).items():
		if k -num_count*arr2[0] <= 0 :
			remainder,quotient=k%num_count,k//num_count
			if remainder==0:
				res += (num*quotient+sum(arr2[1:1+quotient]))*(num_count)
			else:
				
				
				res += (num*quotient+sum(arr2[1:1+quotient]))*(num_count)+(num+arr2[quotient+remainder])*(k-num_count*(quotient))
			
			return res

		res += (num +arr2[1:])*num_count
		k-=num_count*arr2[0]


	return (res)



if __name__ == "__main__":
	assert solve_method_2("1 1","3 1 2 3" ,"2") == 5 
	assert solve_method_2("3 1 1 2","3 1 2 3" ,"2") == 4 
	assert solve_method_2("3 1 1 1","3 1 2 3" ,"3") == 6
	assert solve_method_2("3 1 1 ","3 1 2 3" ,"5") == 14
	assert solve_method_2("3 1 1 ","3 1 2 3" ,"6") == 18
```

