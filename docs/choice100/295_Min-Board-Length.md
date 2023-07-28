# 295 最短木板长度

## 题目描述
小明有n块木板，第i(1≤i≤n)块木板长度为$a_i$。
小明买了一块长度为m的木料，这块木料可以切割成任意块，拼接到已有的木板上，用来加长木板。\
小明想让最短的木板尽量长。\
请问小明加长木板后，最短木板的长度可以为多少？
## 输入描述
输入的第一行包含两个正整数，${n(1≤n≤10^3),m(1≤m≤10^6)}$ \
n表示木板数，m表示木板长度。\
输入的第二行包含n个正整数，${a_1,a_2,...a_n(1≤a_i≤10^6)}$。

## 输出描述
输出的唯一一行包含一个正整数，表示加长木板后，最短木板的长度最大可以为多少？

### 示例一
**输入：**
```shell
5 3
4 5 3 5 5
```

**输出：**
```shell
5
```

**说明：**  
给第1块木板长度增加1，给第3块木板长度增加2后，这5块木板长度变为${[5,5,5,5,5]}$，最短的木板的长度最大为5。

### 示例二
**输入：**
```shell
5 2
4 5 3 5 5
```

**输出：**
```shell
4
```

**说明：**  
给第3块木板长度增加1后，
这5块木板长度变为[4,5,4,5,5]，剩余的木料长度为1。\
此时剩余木料无论给哪块木板加长，最短木料的长度都为4。

## 解题思路
首先对长度LIST升序排序，滑动填充，遇到已填平or一趟无法填平or到达末尾的情况时倒退回第一个元素(也一直是最小的)开启另一趟填充，直到用完M米的木头，全部木头都用完之后再排序一次，然后返回最小的

## 解题代码

```python
def solution(N, M, length):
	'''
	N: number of boards
	M: meters of total unused boards
	length: length of each boards
	'''
	length.sort() # sort ascending
	i = 0 # index of current length of board
	for j in range(M): # use every meter
		length[i] += 1
		if i == (N - 1) or length[i + 1] >= length[i]: # greater_euqal after filling
			i = 0 # back to i=0 and refill
		else:
			i += 1 # move forward
	return sorted(length)[0] # re-sort and return minValue

if __name__ == "__main__":
	N, M = map(int, input().split())
	length = list(map(int, input().split()))
	print(solution(N, M, length))
	# print(solution(5, 10, [4,5,5,5,5]))
```