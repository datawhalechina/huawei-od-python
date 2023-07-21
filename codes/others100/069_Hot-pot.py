def hotPot(n, m, x, y):
    arrTime = [x[i] + y[i] for i in range(n)]
    arrTime.sort()
    arrCount = [0] * n
    arrCount[0] = 1
    next = 0
    for i in range(1, n):
        if arrTime[i] > arrTime[next] + m:
            arrCount[i] = 1
            next = i
    res = sum(arrCount)
    return res


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split(' ')))
    x, y = [], []
    for _ in range(n):
        xy = list(map(int, input().strip().split(' ')))
        x.append(xy[0])
        y.append(xy[1])
    res = hotPot(n, m, x, y)
    print(res)
