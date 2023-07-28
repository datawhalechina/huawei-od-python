# 296 查找充电设备组合

## 题目描述

某个充电站，可提供 n 个充电设备，每个充电设备均有对应的输出功率。 
任意个充电设备组合的输出功率总和，均构成功率集合
P 的1个元素。 
功率集合 P 的最优元素，表示最接近充电站最大输出功率 p_max 的元素。

## 输入描述

输入为三行： 
第一行为充电设备个数 n。 
第二行为每个充电设备的输出功率。 
第三行为充电站最大输出功率 p_max。

## 输出描述

功率集合 P 的最优元素

## 备注

1. 充电设备个数 n>0
2. 最优元素必须小于或等于充电站最大输出功率 p_max。

### 示例一

**输入：**

```shell
4
50 20 20 60
90
```

**输出：**

```shell
90
```

**说明：**
当充电设备输出功率50、20、20组合时，其输出功率总和为90，最接近充电站最大充电输出功率，因此最优元素为90。

### 示例二

**输入：**

```shell
2
50 40
30
```

**输出：**

```shell
0
```

**说明：**
所有充电设备的输出功率组合，均大于充电站最大充电输出功率30，此时最优元素值为0。

## 解题思路
动态规划，用一个二维数组dp[amount-of-charger][max-power-in-total]表示Actual max power under given condition

## 解题代码

```python
def solution(N, power, pm):
	'''
	N: number of powers
	power: [power,...]
	pm: max power
	'''
	# dp[amount-of-charger][max-power-in-total]: Actual-max-power under given condition
	dp = [[0] * (pm + 1) for _ in range(N + 1)]
	for i in range(1, N + 1):
		for v in range(min(power), pm + 1):
			if power[i - 1] > v: # current value greater than max power
				dp[i][v] = dp[i - 1][v]
			else:
				dp[i][v] = max(dp[i - 1][v], power[i - 1] + dp[i - 1][v - power[i - 1]])
	return dp[N][pm]

if __name__ == "__main__":
	N = int(input())
	power = list(map(int, input().split()))
	pm = int(input())
	print(solution(N, power, pm))
	# print(solution(4, [50, 20, 20, 60], 90))
```
