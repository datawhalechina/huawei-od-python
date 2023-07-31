def solve_method(n, points):
    # line_dict存储整数点和出现的次数
    line_dict = {}
    for point in points:
        for i in range(point[0], point[1]+1):
            line_dict[i] = line_dict.get(i, 0) + 1
    # del_count记录可删除的线段数：若线段上每个点出现次数均大于1，表明可删除
    del_count = 0
    for point in points:
        deletable = True
        for i in range(point[0], point[1]+1):
            if line_dict[i] <= 1:
                deletable = False
                break
        if deletable:
            for i in range(point[0], point[1]+1):
                line_dict[i] -= 1
            del_count += 1
    return n - del_count

if __name__ == "__main__":
    # 3
    # 1,4
    # 2,5
    # 3,6
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split(','))
        points.append((x, y))
    print(solve_method(n, points))

    assert solve_method(3, [[1,4], [2,5], [3,6]]) == 2