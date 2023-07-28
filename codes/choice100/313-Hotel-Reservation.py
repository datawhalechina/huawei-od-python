# 输入获取
n, k, x = map(int, input().split())
prices = list(map(int, input().split()))


# 算法入口
def getResult(n, k, x, prices):
    tmp = []

    for p in prices:
        tmp.append((p, abs(p - x)))

    tmp.sort(key=lambda x: (x[1], x[0]))

    ans = list(map(lambda x: x[0], tmp[:k]))

    ans.sort()

    return " ".join(map(str, ans))


# 调用算法
print(getResult(n, k, x, prices))
