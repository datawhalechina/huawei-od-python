import string

# x进制转换n
def f35(n,x):
    # 检查非法
    if x < 2 or x > 35 or x > n:
        return 'ERROR'
    
    # 0-9的数字
    lil = [i for i in range(10)]
    # 定义所有ASCII字母
    li2 = list(string.ascii_letters)
    li3=['@','_']

    # 全拼在一起
    li = lil + li2 + li3
    result =''
    # 一个无限循环
    while True:
        # 计算在x进制下的商
        m = n //x
        # 计算余数
        r = n % x 
        # 说明转换已经结束，只剩下一个个位数了
        if n < x:
            # 取出li数组中索引为n的元素与结果result拼接后跳出循环
            result = str(li[n]) + result
            break
        # 不断拼接
        result = str(li[r])+result
        # 更新
        n = m
    return result

# 将num这个n进制的字符数组转换为十进制数
def any_to_decimal(num,n):
    # 定义字典：每个字符对应的十进制数
    baseStr = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
                "a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19}
    new_num = 0
    # num长度减一做最高位的幂次方
    nNum = len(num)-1
    for i in num:
        # 乘以n的nNum次方
        new_num = new_num + baseStr[i] * pow(n,nNum)
        # 幂减一
        nNum = nNum-1
    return new_num

def solve_method(line):
    split = line.split(" ")
    # 检查第二第三个元素
    if check(split[1]):return
    if check(split[2]):return
    # 将列表第一个转换为整数（进制）
    radix = int(split[0])
    # 被减数按radix进制转换为十进制
    minuend = any_to_decimal(split[1],radix)
    # 减数
    subtrahend = any_to_decimal(split[2],radix)

    diff = int(minuend)-int(subtrahend)
    # 输出正负
    sign = 0 if diff >=0 else 1
    # 计算绝对值
    value = abs(diff)

    print("%d %s"%(sign,f35(value,radix)))

def check(str):
    # 字符串长度大于1且以0开头时
    if len(str)>1 and str.startswith("0"):
        print(-1)
        return True
    # 出现其他异常
    return False

line = input().strip()
solve_method(line)