def solve_method(num):
    # 定义空集合存储因子
    factors=set()
    tmp = num
    # 初始因子为2
    f = 2
    while tmp != 1:
        # 判断tmp是否能被f整除
        if tmp % f != 0:
            # 不能则加1
            f+=1
        else:
            # 将可以整除的因子加入set中
            factors.add(f)
            # 求商
            tmp //f
    # 双重循环判断两个因子乘积是否为num
    for f1 in factors:
        for f2 in factors:
            if f1 * f2 == num:
                min_factor = min(f1,f2)
                max_factor = max(f1,f2)
                # 格式化输出
                print(f"{min_factor}{max_factor}")
                return
    print("-1 -1")

if __name__ == "__main__":
    num = int(input())
    solve_method(num)