def solve_method(nums):
    # 将输入的数字字符串分割成列表
    nums_list = nums.split(" ")
    # 初始化变量 builder、select 和 copy
    builder = ""
    select = ""
    copy = ""
    # 遍历数字列表
    for op in nums_list:
        if op == "1":
            # 执行操作1：清空 select，并在 builder 中添加 'A'
            select = empty(builder, select)
            builder += 'A'
        elif op == "2":
            # 执行操作2：复制 select 的值给 copy
            if select != "":
                copy = select
        elif op == "3":
            # 执行操作3：清空 select、builder 和 copy 的值
            if select != "":
                copy = select
                select = ""
                builder = ""
        elif op == "4":
            # 执行操作4：清空 select，并在 builder 中添加 copy 的值
            select = empty(builder, select)
            builder += copy
        elif op == "5":
            # 执行操作5：将 builder 的值赋给 select
            if len(builder) != 0:
                select = builder
        else:
            pass
    # 输出 builder 的长度
    print(len(builder))

def empty(builder, select):
    # 清空 select 在 builder 中的值，并将 select 置为空字符串
    if select != "":
        builder = builder.replace(select, "")
        select = ""
    return select

def main():
    # 读取输入的数字字符串，调用 solve_method 函数进行处理
    nums = input()
    solve_method(nums)

if __name__ == '__main__':
    main()
