n = int(input())
nodes = {}
for i in range(n):
    id, pid, val = map(int, input().split(" "))
    if id < 0 or id >= n or pid < -1 or pid >=n:
        continue
    nodes[id] = [pid, val]
dp = {}

def dfs(i):
    if i not in dp:
        if nodes[i][0] == -1:
            dp[i] = nodes[i][1]
        else:
            dp[i] = max(nodes[i][1], nodes[i][1] + dfs(nodes[i][0]))
    return dp[i]

max_val = -float("inf")
for i in reversed(range(n)):
    if i not in nodes:
        continue
    max_val = max(max_val, dfs(i))

print(max_val)