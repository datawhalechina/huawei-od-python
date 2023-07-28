import re

# 如果端口组间存在2个及以上不同端口相同，则认为这2个端口组互相关联，可以合并。
# 下面方法实现中：要形成两对“端口值不同的端口对”，即 a = [1,2,3]，b=[2,3,4]可以合并，但是a = [1,3,3]，b=[3,3,4]不可以合并
def canUnion(port1, port2):
    set1 = set(port1)
    set2 = set(port2)

    same = 0
    for v in set1:
        if v in set2:
            same += 1
            if same >= 2:
                return True

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

    # return list(map(distinctAndSort, ports))
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
