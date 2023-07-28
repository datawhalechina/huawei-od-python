# 输入获取
s = input()


# 算法入口
def getResult(s):
    # 此时count记录统计W,A,S,D字母的数量
    count = {
        "W": 0,
        "A": 0,
        "S": 0,
        "D": 0
    }

    for c in s:
        count[c] += 1

    avg = len(s) / 4  # 平衡状态时，W,A,S,D应该都是avg数量
    total = 0  # total用于记录多余字母个数
    flag = True  # flag表示当前是否为平衡状态，默认是

    for c in count.keys():
        if count[c] > avg:
            flag = False  # 如果有一个字母数量超标，则平衡打破
            count[c] -= avg  # 此时count记录每个字母超过avg的数量
            total += count[c]
        else:
            count[c] = 0

    if flag:
        return 0  # 如果平衡，则输出0

    i = 0
    j = 0
    minLen = len(s) - 1

    while j < len(s):
        jc = s[j]

        if count[jc] > 0:
            total -= 1
        count[jc] -= 1

        while total == 0:
            minLen = min(minLen, j - i + 1)

            ic = s[i]
            if count[ic] >= 0:
                total += 1
            count[ic] += 1

            i += 1

        j += 1

    return minLen


print(getResult(s))
