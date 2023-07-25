#  119-最大排列

## 题目描述

给定一组整数，重排序后输出一个最大的整数

## 输入描述

数字组合

## 输出描述

最大的整数

## 示例描述

### 示例一

**输入：**

```
10 9
```

**输出：**

```
910
```

## 解题思路

排序函数的应用，理解题意即可

## 解题代码

```python
def solve_method(nums):
	nums = [str(x) for x in nums]
	nums.sort(key=lambda x: x * 3,reverse=True)
	return int("".join (nums ))

#nums = map(int, input().strip().split(" "))
#print(solve_method(nums))


def solve_method2(nums):
	nums = [str(num) for num in nums]
	nums .sort(key=lambda num: num * 3,reverse=True)
	return int("".join (nums))
#input_nums = input("") .strip().split(" ")
#nums = [int(num) for num in input_nums]
#result = solve_method(nums)
#print(result)
```

## 代码运行结果

```
10 9
910
```

## 第 N 个排列

## 题目描述

给定参数 `n` ，从`1`到 `n` 会有 n 个整数 `1，2，3，...n`
这 `n` 个数字共有 `n!`种排列 按大小顺序升序列出所有排列情况
并一一标记当
 `n = 3` 时，所有排列如下
`"123' , "132"  "213 , "231" , "312"  "321"`
给定 `n` 和 `k` 返回第 `n` 个排列

## 输入描述

第一行为 `n`
第二行为 `k`
`k`的范围是 `1 ~ n!`
输出排序为第`K`位置的数字

## 示例描述

### 示例一

**输入：**

```
3
3
```

**输出：**

```
213
```

### 示例二

**输入：**

```
2
2
```

**输出：**

```
21
```



## 解题思路

本题重点是使用 Python 的内置库 itertools来生成排列。

## 解题代码

```python
import itertools

def solve method(n, k):
	arr = [i + 1 for i in range(n)]
	perms = list(itertools.permutations(arr))
	res = "".join(str(x) for x in perms[k - 1])
	print(res)

if __name__ == '__main__':
	n = int(input().strip())
	k = int(input().strip())
	solve method(n, k)
```

## 代码运行结果

```
3
3
213
```

