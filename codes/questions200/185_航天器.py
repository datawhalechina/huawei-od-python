import sys
#从标准输入读取一行并去除首尾的空白字符
line = sys.stdin.readline().strip()

longs = list(map(int, line.split(",")))

res = 0

for i in range(len(longs)):
    for j in range(i+1, len(longs)):
        area = min(longs[i], longs[j]) * (j-i)
        res = max(res,area)

print(res)