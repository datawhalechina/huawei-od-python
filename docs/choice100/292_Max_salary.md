# 292 最大报酬

## 题目描述
小明每周上班都会拿到自己的工作清单，工作清单内包含 n 项工作，每项工作都有对应的耗时时间(单位 h )和报酬,工作的总报酬为所有已完成工作的报酬之和，那么请你帮小明安排一下工作，保证小明在指定的工作时间内工作收入最大化。

## 输入描述
输入的第一行为两个正整数 T，n。 \
T 代表工作时长 (单位 h，0<T<1000000 ) ,
n 代表工作数量 ( 1<n<=3000 )。 \
接下来是 n 行，每行包含两个整数 t，w。
t 代表该工作消耗的时长 (单位 h，t>0), w 代表该项工作的报酬。

## 输出描述
输出小明制定工作时长内工作可获得的最大报酬。
### 示例一
**输入：**
```shell
40 3
20 10
20 20
20 5
```

**输出：**
```shell
30
```

**说明：**  

## 解题思路
用一个dp二维数组存储状态信息，dp[i][j]表示j小时内前i份工作所能所得的最大报酬，在迭代i与j的过程中不断更新dp[i][j]，直到求得dp[n][t]，即在t小时内所有工作中所能取得的最大报酬

## 解题代码

```python
def solution(T, N, jobs):
	m_t = min(jobs, key = lambda x: x['hour'])['hour'] # min hours of jobs
	# dp[i][j]: max wage in the first i jobs in j hours
	dp = [[0] * (T + 1) for _ in range(N + 1)]
	for j in range(1, N + 1): # job
		for t in range(m_t, T + 1): # time
			job = jobs[j - 1]
			w1 = dp[j - 1][t]
			w2 = job['wage'] + dp[j - 1][t - job['hour']] if job['hour'] <= t else 0
			# update max wage or not 
			dp[j][t] = max(w1, w2)
	return dp[N][T]

if __name__ == "__main__":
	T, N = map(int, input().split())
	jobs = [dict(zip(['hour', 'wage'], map(int, input().split()))) for _ in range(N)]
	res = solution(T, N, jobs)
	print(res)
```