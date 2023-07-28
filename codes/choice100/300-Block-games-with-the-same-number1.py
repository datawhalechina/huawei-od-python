# 输入获取
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# 算法入口
def getResult(arr, n):
    idx = {}

    for i in range(n):
        num = arr[i]
        if idx.get(num) is None:
            idx[num] = [i]
        else:
            idx[num].append(i)

    ans = -1
    for k in idx.keys():
        if len(idx[k]) > 1:
            ans = max(ans, idx[k][-1] - idx[k][0])

    return ans

# 算法调用
print(getResult(arr, n))