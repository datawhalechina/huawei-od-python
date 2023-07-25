#  118-最大子矩阵

## 题目描述

给定一个二维整数矩阵，要在这个矩阵中 选出一个子矩阵
使得这个子矩阵内所有的数字和尽量大
我们把这个子矩阵成为“和最大子矩阵”，子矩阵的选取原则，是原矩阵中一段相互连续的矩形区域

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

```
3 4
-3 5 -1 5
2 4 -2 4
-1 3 -1 3
```

**输出：**

```
20
```

**说明：**  

一个 `3*4` 的矩阵中
后面 `3` 列的和为 `20`,和最大

## 解题思路

本算法解决的是矩阵中的最大子矩阵和问题。首先读入矩阵的行列数，然后读入矩阵，将其保存到二维列表中。之后通过三重循环遍历每一个子矩阵，计算其和，更新最大和。在计算子矩阵和的过程中，利用了动态规划的思想，可以快速计算出以某个元素为右下角的子矩阵和。

## 解题代码

```python
n = int(input())
m = int(input())

ints = []


for  i in range(n):

	input_str = input()
	input_list = input_str.split(",")
	hang = []
	for j in range(m):
		hang.append(int(input_list[j]))
	ints.append(hang)


max_value= 0
for start_row in range(n):
	for start_col in range(m):
		for end_row in range(start_row, n):
			jisuan = 0
			for end_col in range(start_col, m):
				row_index = end_row
				while  row_index >= start_row:
					jisuan += ints[row_index][end_col]
					row_index -= 1

				max_value = max(max_value, jisuan)

print(max_value)
```

## 代码运行结果

```
3
4
-3,5,-1,5
2,4,-2,4
-1,3,-1,3
20
```

