# 输入获取
m, n = map(int, input().split())
arr = list(map(int, input().split()))

# 算法入口
def getResult(arr, m, n):
    arr.sort()

    count = 0

    i = 0
    j = n - 1

    while i < j:
        if arr[i] + arr[j] <= m:
            i += 1
        j -= 1
        count += 1

    if i == j:
        count += 1

    return count

# 算法调用
print(getResult(arr, m, n))
