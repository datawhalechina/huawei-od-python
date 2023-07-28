import sys

# 输入获取
arr = list(map(int, input().split()))

# 算法入口
def getResult(arr):
    minDiff = sys.maxsize
    ans = None

    for k in range(-127, 129):
        sum = 0
        for j in range(len(arr)):
            # 新图的像素值会自动截取到[0,255]范围。当新像素值<0，其值会更改为0；当新像素值>255，其值会更改为255；
            newVal = min(max(0, arr[j] + k), 255)
            sum += newVal

        diff = abs(sum / len(arr) - 128)

        if diff < minDiff:
            minDiff = diff
            ans = k
        elif diff == minDiff and ans is not None:
            # 如有多个整数k都满足，输出小的那个k
            ans = min(ans, k)

    return ans

# 算法调用
print(getResult(arr))
