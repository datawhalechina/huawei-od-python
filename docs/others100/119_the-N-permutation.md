## 第 N 个排列

## 题目描述

给定参数 `n` ，从`1`到 `n` 会有 n 个整数 `1，2，3，...n`
这 `n` 个数字共有 `n!`种排列 按大小顺序升序列出所有排列情况
并一一标记当 `n = 3` 时，所有排列如下
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

```text
3
3
```

**输出：**

```text
213
```

### 示例二

**输入：**

```text
2
2
```

**输出：**

```text
21
```



## 解题思路

使用 Python 的内置库 itertools的permutations函数，来生成排列。

> permutations(iterable, r=None)返回的是一个可迭代元素的一个排列组合，并且是按照顺序的，且不包含重复的结果。

## 解题代码

```python
import itertools

def solve_method(n, k):
	arr = [i + 1 for i in range(n)]
	perms = list(itertools.permutations(arr))
	res = int("".join(str(x) for x in perms[k - 1]))
	return res

if __name__ == '__main__':

	assert solve_method(2,2) == 21
```

