# coding: utf-8

def solve_method(ip:str):
    # 以#分隔字符串
    strings = ip.split("#")
    # 获取长度
    length = len(strings)
    count = 0
    # 置为合法
    is_valid = True
    # 首先该字符串得是四小节
    if length == 4:
        for i in range(length):
            # 取出每一个数
            n = int(strings[i])
            # 第一个数的取值范围是1~128
            if i==0 and (n < 1 or n > 128):
                is_valid = False
                break
            # 过滤其他位置上的非法
            elif n < 0 or n > 255:
                is_valid = False
                break
            # 分析可得出一个数值对应两位十六进制数也就是八位二进制数
            # 位运算左移（3-i）个八位
            count+=n<<(8*(3-i))
    else:
        is_valid = False
    if is_valid:
        print(count)
    else:
        print("invalid IP")

if __name__ =='__main__':
    ip = input()
    solve_method(ip)