# 输入获取
n = int(input())
cmds = [input() for i in range(2 * n)]

# 算法入口
def getResult(cmds):
    size = 0
    isSorted = True
    count = 0

    for cmd in cmds:
        if cmd.startswith("head add"):
            if size > 0 and isSorted:
                isSorted = False
            size += 1
        elif cmd.startswith("tail add"):
            size += 1
        else:
            if size <= 0:
                continue

            if not isSorted:
                count += 1
                isSorted = True

            size -= 1

    return count

# 算法调用
print(getResult(cmds))