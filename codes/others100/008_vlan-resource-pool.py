# 去除首尾空白字符
input_str = input().strip()
request = int(input().strip())

# “，” 拆分
input_list = input_str.split(",")
result_set = set()

for i in input_list:
    # 判断是否包含 "-"
    if "-" in i:
        # 将 - 两端拆分转整型
        start,end = map(int,i.split("-"))
        # 遍历添加
        for j in range(start,end +1):
            result_set.add(j)
    else:
        # 单个字符直接添加
        result_set.add(int(i))

# 从列表中删除指定元素
result_set.remove(request)
# 转换为列表
result_list = list(result_set)
# 对其排序
result_list.sort()

# 确定起始
start = result_list[0]
last = start
output_list = []

# 从第二个元素开始遍历
for i in range(1,len(result_list)):
    cur = result_list[i]
    # 如果cur等于last的后序元素
    if cur == last +1:
        # 更新尾数
        last = cur
    else:
        # 否则将start到last的元素添加进output_list里面
        output_list.append((start,last))
        # 更新起始
        start = last = cur
# 把剩下的加入
output_list.append((start,last))

# 使用列表推导式构建一个字符串列表 output_str
# 并使用 ",".join(output_str) 方法以逗号为分隔符将其连接成一个字符串。
# 列表推导式会根据范围元组 (start, last) 是否相等，
# 使用不同的格式进行格式化
output_str =",".join(["{}-{}".format(i,j) if i!=j else "{}".format(i) for i,j in output_list])
print(output_str)