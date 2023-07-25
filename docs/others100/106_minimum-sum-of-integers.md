#  106-整数对最小和

## 题目描述

给定两个整数数组 arrayl array2

数组元素按升序排列

假设从 arrayI array2 中分别取出一个元素可构成一对元素

现在需要取出 K 个元素

并对取出的所有元素求和

计算和的最小值
注意:
两对元素如果对应于 array1 array2 中的两个下标均相同，则视为同一个元素

## 输入描述

输入两行数组 arrayl array2

每行首个数字为数组大小 size( < size <= 100 )
0 < arrayl(i) <= 1000
 < array2(i) <= 1000
接下来一行为正整数 k ( < k <= arrayl.size() * array2.size() )

## 输出描述

满足要求的最小和

## 示例描述

### 示例一

**输入：**

```
3 1 1 2
3 1 2 3
2
```

**输出：**

```
4
```

**说明：** 
用例中，需要取两个元素 取第一个数组第0个元素 与第二个数组第0个元素，组成一对元素`[1,1]`
取第一个数组第 1个元素 与第二个数组第0个素，组成一对元素[1,1]求和为 `1+1+1+1=4` 为满足要求的最小和

## 解题思路

该算法的输入是两个长度为n的整数列表 arr1和 arr2，以及一个整数，输出是 arr1和 arr2中的元素相加后，从小到大排序后前k 个元素的和。

算法的实现方法比较简单:首先创建一个空的列表，用于存储 arr1 和 rr2 中每个元素的和，然后对该列表进行排序。最后，取出前k个元素，并计算它们的和。

## 解题代码

```python
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
```

## 代码运行结果

```
3 1 1 2
3 1 2 3
2
4
```

