import re

# 如果端口组间存在2个及以上不同端口相同，则认为这2个端口组互相关联，可以合并。
# 下面方法实现中：对于“不同端口”的理解是：端口位置不同，端口值可以相同，即以不同位置的端口视为不同端口
def canUnion(port1, port2):
    port1.sort()
    port2.sort()

    same = 0
    i = 0
    j = 0

    while i < len(port1) and j < len(port2):
        if port1[i] == port2[j]:
            i += 1
            j += 1
            same += 1
            if same >= 2:
                return True
        elif port1[i] > port2[j]:
            j += 1
        else:
            i += 1

    return False

# 从头开始尝试合并端口组
def forPorts(ports):
    # 这里倒序遍历端口组是为了实现：组外顺序保持输入顺序
    for i in range(len(ports) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            # 判断两个端口是否可以合并
            if canUnion(ports[i], ports[j]):
                # 将后面的端口组，并入前面的端口组，这样就不会破坏组外顺序
                ports[j].extend(ports[i])
                ports.pop(i)
                return True  # 继续尝试合并

    return False  # 合并尝试结束

# 组内相同端口仅保留一个，从小到达排序
def distinctAndSort(port):
    tmp = list(set(port))
    tmp.sort()
    return tmp

# 算法入口
def getResult(ports):
    while True:
        if not forPorts(ports):
            break

    # return list(map(distinctAndSort, ports)) # 如果输出内容不去除空格，可得83.33%通过率
    return re.sub(f"\\s", "", str(list(map(distinctAndSort, ports))))

# 输入获取
m = int(input())

if m < 1 or m > 10:
    print("[[]]")
else:
    ports = [list(map(int, input().split(","))) for _ in range(m)]
    if len(list(filter(lambda p: len(p) < 1 or len(p) > 100, ports))) > 0:
        print("[[]]")
    else:
        print(getResult(ports))
