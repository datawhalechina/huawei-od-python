def main():
    # 读取输入的 m、n 和 R
    m, n, R = map(int, input().split())
    # 读取输入的列表 a 和 b
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 调用 solve 函数进行计算，并将结果保存在 result 中
    result = solve(R, a, b)
    # 遍历结果列表并输出每一对数字
    for r in result:
        print(r[0], r[1])

def solve(R, a, b):
    index = 0
    result = []
    for j in a:
        ints = [0, 0]
        while index < len(b):
            if j <= b[index] and b[index] - j <= R:
                ints[0] = j
                ints[1] = b[index]
                result.append(ints)
                break
            index += 1
    return result

if __name__ == "__main__":
    main()
