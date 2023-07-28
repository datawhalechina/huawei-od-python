# 294 最左侧冗余覆盖子串

## 题目描述

给定两个字符串 `s1`和 `s2`和正整数 `K`，其中 `s1`长度为 `n1`，`s2`长度为 `n2`，
在 `s2`中选一个子串，满足:

1. 该子串长度为 `n1+k`
2. 该子串中包含 `s1`中全部字母，
3. 该子串每个字母出现次数不小于 `s1`中对应的字母，
   我们称 `s2以长度k冗余覆盖s1`，

给定 `s1`，`s2`，`k`,
求最左侧的 `s2`以长度 `k`冗余覆盖 `s1`的子串的首个元素的下标，
如果没有返回 `-1`。

## 输入描述

输入三行，
第一行为 `s1`，
第二行为 `s2`，
第三行为 `k`，
`s1`和 `s2`只包含小写字母

## 输出描述

最左侧的 `s2`以长度 `k`冗余覆盖 `s1`的子串首个元素下标，如果没有返回 `-1`

### 示例一

**输入：**

```shell
ab
aabcd
1
```

**输出：**

```shell
0
```

**说明：**

### 示例二

**输入：**

```shell
abc
dfs
10
```

**输出：**

```shell
-1
```

**说明：**

## 解题思路

哈希法，用长度为26的 LIST 存储每个 str 中各个字符的数量，并进行比较

## 解题代码

```python
def getWordDict(s)->list:
	# return LIST recording dict of String
	wd = [0] * 26 # Word Dictionary of 26 Chars
	for c in s:
		wd[ord(c) - ord('a')] += 1
	return wd

def solution(s1, s2, k):
	'''
	Compare Word Dict
	'''
	wd_s1 = getWordDict(s1)
	# first (len(s1) + k) substring
	wd_s2 = getWordDict(s2[:len(s1) + k])
	# matches at first index
	if wd_s1 <= wd_s2: # compare LIST of same size
		return 0
	else:
		for r in range(len(s1) + k, len(s2)): # new right BDRY(Boundary)
			l = r - (len(s1) + k) # old left BDRY
			rw, lw = s2[r], s2[l]
			wd_s2[ord(rw) - ord('a')] += 1
			wd_s2[ord(lw) - ord('a')] -= 1
			if wd_s1 <= wd_s2:
				return l + 1
		return -1 # failed

if __name__ == "__main__":
	s1, s2 = input(), input()
	k = int(input())
	print(solution(s1, s2, k))
```
