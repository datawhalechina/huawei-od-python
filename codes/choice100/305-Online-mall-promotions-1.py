m, n, k = map(int, input().split())

x = int(input())

prices = []
for i in range(x):
    prices.append(int(input()))

def fullSubtraction(price, m):
    """
    满减规则
    :param price: 总价
    :param m: 满减券数量
    :return: 总价满减后结果，对应数组含义是 (用券后剩余总价， 剩余满减券数量)
    """
    maxCount = int(price / 100)  # 满100最多用1张满减券，满200最多用2张满减券....，price总价最多使用price/100张券
    count = min(m, maxCount)  # 实际可使用的满减券数量

    price -= count * 10
    m -= count

    return price, m

def discount(price, n):
    """
    打折规则
    :param price: 总价
    :param n: 打折券数量
    :return: 总价打折后结果，对应数组含义是 (用券后剩余总价， 剩余打折券数量)
    """
    if n >= 1:
        price = int(price * 0.92)
    return price, n - 1

def thresholdFree(price, k):
    """
    无门槛你规则
    :param price: 总价
    :param k: 无门槛券数量
    :return: 门槛券用后结果，对应数组含义是 (用券后剩余总价， 剩余无门槛券数量)
    """
    while price > 0 and k > 0:
        price -= 5
        price = max(price, 0)  # 无门槛券过多会导致优惠后总价小于0，此时我们应该避免
        k -= 1
    return price, k

for price in prices:
    ans = []

    resM = fullSubtraction(price, m)  # 先满减

    resMN_N = discount(resM[0], n)  # 满减后打折
    ans.append((resMN_N[0], m + n - (resM[1] + resMN_N[1])))  # m + n 是满减后打折方式的总券数量， resM[1] + resMN_N[1] 是满减券剩余数+打折券剩余数

    resMK_K = thresholdFree(resM[0], k)  # 满减后无门槛
    ans.append((resMK_K[0], m + k - (resM[1] + resMK_K[1])))

    resN = discount(price, n)  # 先打折

    resNM_M = fullSubtraction(resN[0], m)  # 打折后满减
    ans.append((resNM_M[0], n + m - (resN[1] + resNM_M[1])))

    resNK_K = thresholdFree(resN[0], k)  # 打折后无门槛
    ans.append((resNK_K[0], n + k - (resN[1] + resNK_K[1])))

    # 对ans进行排序，排序规则是：优先按剩余总价升序，如果剩余总价相同，则再按“使用掉的券数量”升序
    ans.sort(key=lambda x: (x[0], x[1]))

    print(" ".join(map(str, ans[0])))
