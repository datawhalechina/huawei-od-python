# 算法入口
def getResult(arr):
    """
    :param total: 误码总数目
    :param arr: 误码出现频率数组
    :return: 包含频率最高的误码最小子数组长度
    """
    idxs = {}

    for i in range(len(arr)):
        code = arr[i]
        if idxs.get(code) is None:
            idxs[code] = [i]
        else:
            idxs[code].append(i)

    maxSize = 0
    minLen = 0

    for values in idxs.values():
        size = len(values)
        length = values[-1] - values[0] + 1

        if size > maxSize or (size == maxSize and length < minLen):
            maxSize = size
            minLen = length

    return minLen


# 输入获取
total = int(input())

if total == 0:
    print(0)
else:
    arr = list(map(int, input().split()))
    print(getResult(arr))
