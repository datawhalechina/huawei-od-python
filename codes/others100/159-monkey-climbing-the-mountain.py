def count_jump_ways(n):
    # 创建一个长度为n+1的列表，用于保存每个台阶的跳跃方式数
    jump_ways = [0] * (n + 1)

    # 初始化第一个台阶的跳跃方式数为1
    jump_ways[0] = 1

    # 计算每个台阶的跳跃方式数
    for i in range(1, n + 1):
        # 如果当前台阶可以跳1步，则加上从前一个台阶跳上来的方式数
        if i >= 1:
            jump_ways[i] += jump_ways[i - 1]
        # 如果当前台阶可以跳3步，则加上从前三个台阶跳上来的方式数
        if i >= 3:
            jump_ways[i] += jump_ways[i - 3]

    return jump_ways[n]

# 读取输入
n = int(input())

# 调用函数计算跳跃方式数
jump_ways = count_jump_ways(n)

# 输出结果
print(jump_ways)