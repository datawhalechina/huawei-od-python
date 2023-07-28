import math
import re

# 输入获取
n = int(input())
arr = [input() for i in range(n)]


# 算法入口
def getResult(arr):
    exchage = {
        "CNY": 100,
        "JPY": 100 / 1825 * 100,
        "HKD": 100 / 123 * 100,
        "EUR": 100 / 14 * 100,
        "GBP": 100 / 12 * 100,
        "fen": 1,
        "cents": 100 / 123,
        "sen": 100 / 1825,
        "eurocents": 100 / 14,
        "pence": 100 / 12
    }

    ans = 0

    s = "".join(arr) + "0"
    num = ""
    unit = ""

    for c in s:
        if "0" <= c <= "9":
            if unit != "":
                ans += int(num) * exchage[unit]
                num = ""
                unit = ""
            num += c
        elif "a" <= c <= "z" or "A" <= c <= "Z":
            unit += c

    return math.floor(ans)


# 算法调用
print(getResult(arr))
