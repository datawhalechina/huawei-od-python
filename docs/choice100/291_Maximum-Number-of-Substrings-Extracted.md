# 291 最多提取子串数目

## 题目描述
给定由 $[a - z]$ 个英文小写字母组成的字符串A和B，其中 A中可能存在重复字母，B中不会存在重复字母。现从字符串A 中按规则挑选一些字母，可以组成字符串B。挑选规则如下：
1) 同一个位置的字母只能被挑选一次
1) 被挑选字母的相对先后顺序不能改变

求最多可以同时从 A 中挑选多少组能组成 B 的字符串

## 输入描述
输入为 2 行，第 1 行输入字符串 A，第 2 行输入字符串 B，行首行尾无多余空格 \
其中 A、B 均由 $[a - z]$ 26 个英文小写字母组成 \
0 < A.length < 100，A中可能包含重复字母 \
0 < B.length < 10，B 中不会出现重复字母

## 输出描述
输出 1 行，包含 1 个数字，表示最多可以同时从 A 中挑选多少组能组成 B 的字符串 \
行末无多余空格

### 示例一
**输入：**
```shell
badc
bac
```

**输出：**
```shell
1
```
**说明：**  
从字符串 A("badc")中可以按字母相对先后顺序取出字符串 B("bac")

### 示例二
**输入：**
```shell
badc
abc
```

**输出：**
```shell
0
```
**说明：**  
从字符串 A("badc")中无法按字母相对先后顺序取出字符串 B("abc")

### 示例三
**输入：**
```shell
aabbcxd
abcd
```

**输出：**
```shell
1
```

**说明：**  

### 示例四
**输入：**
```shell
aaa
a
```

**输出：**
```shell
3
```

**说明：**  
从字符串 A("aaa")中可以挑选 3 个字符串 B("a")
## 解题思路

## 解题代码

```python
def solution(A:list, B:list)->int:
	# ababcecfdc
	# abc
	res = 0
	exist = [True for _ in range(len(A))] # -1:removed
	flg = True # Find one pair?
	while flg: # not null
		flg = False
		ib = 0
		for ia in range(len(A)):
			if exist[ia]: # exist
				if A[ia] == B[ib]: # match 
					ib += 1 # move forward
					exist[ia] = False # remove 
				ia += 1 # move 

			if ib == len(B): # reach end of B
				res += 1
				flg = True
				break
	return res

if __name__ == '__main__':
    assert solution('ababcecfdc', 'abc') == 2
```