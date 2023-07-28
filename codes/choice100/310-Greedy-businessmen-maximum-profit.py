# 输入获取
number = int(input())
days = int(input())
item = list(map(int, input().split()))
prices = [list(map(int, input().split())) for i in range(number)]


# 如果当前解法通过率较低，可以尝试将第5行的prices的初始化，改为下面这种，通过率应该会有所上升
# prices = []
# for i in range(number):
#     prices.append(list(map(int, input().split())))
#     print(0)

# 算法入口
def getResult(number, days, item, prices):
    """
    :param number: 几种商品
    :param days: 几天
    :param item: 每种商品的最大囤货数量
    :param prices: 每种商品的在days天内的价格变动情况
    :return: 最大利润
    """
    ans = 0
    for i in range(number):
        price = prices[i]
        for j in range(days - 1):
            if price[j] < price[j + 1]:
                ans += (price[j + 1] - price[j]) * item[i]
    return ans


# 算法调用
print(getResult(number, days, item, prices))
