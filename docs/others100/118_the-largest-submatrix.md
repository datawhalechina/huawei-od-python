#  118-最大子矩阵

## 题目描述

给定一个二维整数矩阵，要在这个矩阵中，选出一个子矩阵，使得这个子矩阵内所有的数字和尽量大。我们把这个子矩阵成为“和最大子矩阵”，子矩阵的选取原则，是原矩阵中一段相互连续的矩形区域。

## 输入描述

输入的第一行包含两个整数 `N`,`M`
`(1 <= N,M <= 10)`
表示一个 N 行 M 列的矩阵
下面有 `N` 行每行有 `M`个整数
同一行中每两个数字之间有一个空格
最后一个数字后面没有空格
所有的数字得在 `-1000 ~ 1000` 之间

## 输出描述

输出一行,一个数字
表示选出的“和最大子矩阵”内所有数字的和

## 示例描述

### 示例一

**输入：**

```text
3 4
-3 5 -1 5
2 4 -2 4
-1 3 -1 3
```

**输出：**

```text
20
```

**说明：**  

一个 `3*4` 的矩阵中
后面 `3` 列的和为 `20`,和最大

## 解题思路

1. 遍历`(0-N*M)`范围内子矩阵左上角位置行位置`start_row` 

2. 嵌套循环，遍历`(0-N*M)`范围内子矩阵左上角位置列位置`start_col`

3. 嵌套循环，遍历`(start_row, N)`范围内子矩阵右下角位置行位置

4. 嵌套循环，遍历`(start_col, M)`范围内子矩阵右下角位置行位置

5. 利用`while` 循环求和 子矩阵的所有元素

6. 每次求和完，判断一下求和结果是否小于0 如果小于0 跳出一层循环。

   

## 解题代码

```python

def solve_method(n,m,arr):
	max_value= 0
	for start_row in range(n):
		for start_col in range(m):
			for end_row in range(start_row, n):
				sums = 0
				for end_col in range(start_col, m):
					row_index = end_row
					while  row_index >= start_row:
						sums += arr[row_index][end_col]
						row_index -= 1

					if sums <=0:
						break
					max_value = max(max_value, sums)

	return max_value





if __name__ == '__main__':

	assert solve_method(3,4,[[-3,5,-1,5],[2,4,-2,4],[-1,3,-1,3]]) == 20
	assert solve_method(3,4,[[-3,50,-10,-5],[-2,-4,-2,-4],[-1,-3,-1,-3]]) == 50


```





