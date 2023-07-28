# 293 最小施肥机能效

## 题目描述

某农场主管理了一大片果园， fields[i] 表示不同果林的面积，单位: ($m^2$)，现在要为所有的果林施肥且必须在 n 天之内完成，否则影响收成。

小布是果林的工作人员，他每次选择一片果林进行施肥，且一片果林施肥完后当天不再进行施肥作业。

假设施肥机的能效为 k，单位: ($m^2/day$) ，请问至少租赁能效 k 为多少的施肥机才能确保不影响收成?

如果无法完成施肥任务，则返回 -1。

## 输入描述

第一行输入为 m 和 n，m 表示 fields 中的素个数，n 表示施肥任务必须在 n 天内 (含 n 天)完成

第二行输入为 fields， fields[i] 表示果林 i 的面积，单位：($m^2$)

## 输出描述

对于每组数据，输出最小施肥机的能效 (k)，无多余空格。

## 备注

$1 \le fields.length \le 10^4$

$1 \le n \le 10^9$

$1 \le fields[i] \le 10^9$

### 示例一

**输入：**

```shell
5 7
5 7 9 15 10
```

**输出：**

```shell
9
```

**说明：**
当能效k为9 时，

fields[0] 需要 1天

fields[1] 需要 1天

fields[2] 需要 2 天

fields[3] 需要 2 天

fields[4] 需要 2 天

共需要 7 天，不会影响收成。

### 示例二

**输入：**

```shell
3 1
2 3 4
```

**输出：**

```shell
-1
```

**说明：**
由于一天最多完成一片果林的施肥，无论 k 为多少都至少需要 3 天才能完成施肥，因此返回 -1。

## 解题思路

使用二分查找，以1作为左边界，max(fields) 作为最大值

## 解题代码

```python
def solution(M, N, fields):
	if N < len(fields):
		return -1 # failed
	l = 1 # min velocity, left
	res = r = max(fields) # max velocity, right
	while l <= r:
		m = (l + r) // 2
		hour = sum(list(map(lambda x : x // m if x % m == 0 else (x // m) + 1, fields)))
		if hour <= N: # equal
			r = m - 1
			res = min(res, m)
		else: # over time
			l = m + 1
	return res


if __name__ == "__main__":
	M, N = map(int, input().split()) # M: numbers N: days
	fields = list(map(int, input().split()))
	res = solution(M, N, fields)
	print(res)
```
