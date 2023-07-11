# coding: gbk
# 要设置编码
n = int(input()) #输入行数

lights = []

for x in range(n):
    # input获取用户输入后使用split按空格分隔成一个字符串列表，并通过map将每个元素映射成整数
    input_data = list(map(int, input().split()))
    # 接下来依次将该列表的元素填入
    id = input_data[0]
    x1 = input_data[1]
    y1 = input_data[2]
    x2 = input_data[3]
    y2 = input_data[4]
    # 用id,xy坐标的平均值和坐标的差值一半（也就是灯泡的宽半径）组合成一个数组再压入lights中
    lights.append([id, (x1 + x2)//2, (y1 + y2)//2,(x2-x1)//2])

# 利用内置函数进行排序
# 注：lambda 是一个在Python中用于创建匿名函数的关键字。
#   匿名函数是一种没有名称的函数，通常用于编写简短的功能代码。
# 用法：
#   如lambda arguments: expression
#       arguments 是函数的参数，可以是一个或多个。
#       expression 是函数执行的表达式。也就是最后这个匿名函数返回的值
# 对于下面这个匿名函数其实就相当于 
# def key(a): 
#   a[2] # 返回了数组的第三个变量
# 传入匿名函数的参数是a数组，对lights排序的key是lights中每个数组的第三个元素，也就是y坐标的平均值
# 使得lights中的元素依次按y心排行从小到大排序
lights.sort(key=lambda a: a[2])

# 这里可以输出lights看看

result = []
# 每一行的起始索引
row_start_index = 0
for i in range(1,n):
    # 要求两个灯高低偏差不超过灯半径算同一行
    # 判断y坐标之差也就是灯高度差是否小于灯的半径
    # 如果大于则表示是新的一行了
    if lights[i][2] - lights[row_start_index][2] > lights[row_start_index][3]:
        # 对起始行row_start_index到当前行i的子列表进行排序，按照每个元组的 x 坐标进行排序
        lights[row_start_index:i] = sorted(lights[row_start_index:i],key=lambda a:a[1])
        # 使用列表推导式将起始行到当前行的 id 生成列表添加到 result 列表中，具体如下：
        #   对列表 lights[row_start_index:i] 中的每个元素 light
        #   取出其中的第一个元素，并将这些元素组成一个新的列表
        result.extend([light[0] for light in lights[row_start_index:i]])
        # 更新起始行的索引，将其设置为当前行的索引
        row_start_index = i
# 因为最后那一行if一直绿灯下去，所以得对剩下的排序进行收尾工作
lights[row_start_index:n] = sorted(lights[row_start_index:n],key=lambda a:a[1])
result.extend([light[0]for light in lights[row_start_index:n]])

# 将列表 result 中的元素转换为字符串，并将它们连接起来
print(' '.join(map(str,result)))