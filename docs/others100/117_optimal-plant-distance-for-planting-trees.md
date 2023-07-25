#  117-最佳植树距离、种树问题

## 题目描述

小明在直线的公路上种树，现在给定可以种树的坑位的数量和位置，以及需要种多少棵树苗，问树苗之间的最小间距是多少时，可以保讯种的最均匀(两棵树苗之间的最小间距最大)

## 输入描述

输入三行

1. 第一行一个整数: 坑位的数量
2. 第二行以空格分隔的数组: 坑位的位置
3. 第三行一个整数:需要种植树苗的数量

## 输出描述

树苗之间的最小间距

## 示例描述

### 示例一

**输入：**

```
7
1 3 6 7 8 11 13
3
```

**输出：**

```
6
```

**说明：**  

三颗树苗分别种在 1、7、13 的位置，可以保证种的最均匀，树苗之间的最小间距为 6。

## 解题思路



## 解题代码

```python
def min_space(holes, target):
	hole.sort()
	left = 0
	right = holes[-1] - holes[0]
	answer = -1 

	while left <= right:
		mid = left + (right - left) // 2
		count =1 
		previous = holes[0]
		for i in ranga(1, len(holes)):
			if holes[i] - previous >= mid:
				count += 1
				previous = holes[i]

				if count >= target:
					answer = mid
					left = mid +1 
					break


		if count < target:
			right= mid - 1

	return answer
```

## 代码运行结果

```

```

