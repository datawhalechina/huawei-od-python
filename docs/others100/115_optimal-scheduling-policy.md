#  115-最优调度策略

## 题目描述

在通信系统中有一个常见的问题是对用户进行不同策略的调度，会得到不同系统消耗的性能。假设由 `N` 个待串行用户，每个用户可以使用 `A/B/C` 三种不同的调度策略。不同的策略会消耗不同的系统资源，相邻的用户不使用相同的调度策略，要求返回对系统资源消耗最少的策略。
例如:
第一个用户使用 A 策略 则第二个用户只能使用 B 和 C 策略
对单的用户而言，不同的调度策略对系统资源的消耗可以规划后抽象为数值
例如：
某用户分别使用 `ABC` 策略的系统消耗，分别为 `15 8 17`
每个用户依次选择当前所能选择的对系统资源消耗最少的策略,局部最优如果有多个满足要求的策略，选最后一个

## 输入描述

第一行表示用户个数 N
接下来表示每一行表示一个用户分别使用三个策略的资源消耗
`resA` `resB` `resC`

## 输出描述

最优策略组合下的总的系统消耗资源数

## 示例描述

### 示例一

**输入：**

```text
3
15 8 17
12 20 9
11 7 5
```

**输出：**

```text
24
```

**说明：**  

`1` 号用户使用 `B` 策略
`2` 号用户使用 `C` 策略
`3` 号用户使用 `B` 策略
系统资源消耗 `8+9+7`

## 解题思路



1. 遍历用户策略数组arr,当指标`preIndex=None`时在当前用户三个策略中寻找资源消耗最小值`minTime`，如果`preIndex!=None`，则在`preIndex`标记以外的策略中寻找资源消耗最小值`minTime`。
2. 如果当前用户策略资源消耗有两个最小值则记`preIndex=None`，只有一个最小值则记`preIndex`为最小值策略坐标。
3. 累加得到的策略资源消耗最小值`res += minTime`。
4. 重复1-3 直到遍历结束，返回结果`res`。

## 解题代码

```python
def solve_method(arr):
	
	res = 0
	preIndex = None
	for i in range(len(arr)):
		times = list(map(int, arr[i].split()))
		if preIndex == None:

			minTime = min(times)
			preIndex = times.index(minTime)
			
			if  minTime in  times[:preIndex] + times[preIndex + 1:]:
				
				preIndex = None  
		else:
			minTime = min(times[:preIndex] + times[preIndex + 1:])
			preIndex = times.index(minTime)
			
			if   minTime in  times[:preIndex] + times[preIndex + 1:]:	
				preIndex = None 
		res += minTime
	return res
if __name__ == '__main__':

	solve_method(["15 8 17","9 20 9","5 7 11"])==8+9+5
	solve_method(["15 8 17","12 20 9","5 7 11"])==8+9+11

```





