# 输入获取
m = int(input())
f = list(map(int, input().split()))
s = list(map(int, input().split()))


# 算法入口
def getResult(m, f, s):
    # count用于保存每个文件出现的次数
    count = {}
    # size用于保存文件的大小，即扫描成本
    size = {}

    for i in range(len(f)):
        # k是文件标识
        k = f[i]
        if count.get(k) is None:
            count[k] = 1
        else:
            count[k] += 1

        if size.get(k) is None:
            size[k] = s[i]

    ans = 0
    for k in count.keys():
        # 选择每次都重新扫描的成本  和  扫描一次+缓存的成本  中最小的
        ans += min(count[k] * size[k], size[k] + m)
    return ans


print(getResult(m, f, s))
