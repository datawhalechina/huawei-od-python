def solve_method(n, positions):
    # 区域数组positions的长度n范围为：1＜＝n＜＝10^5
    left, right = 0, 100000
    while left < right:
        mid = (left + right) >> 1
        if get_distance(mid, positions) < get_distance(mid+1, positions):
            right = mid
        else:
            left = mid + 1
    return get_distance(left, positions)

def get_distance(location, positions):
    distance = 0
    for position in positions:
        if position[0] > location:
            distance += position[0] - location
        elif position[1] < location:
            distance += location - position[1]
    return distance

if __name__ == "__main__":
    # 3
    # 1 2
    # 3 4
    # 10 20
    n = int(input())
    positions = []
    for _ in range(n):
        positions.append(list(map(int, input().split())))
    print(solve_method(n, positions))

    assert solve_method(3, [[1,2], [3,4], [10,20]]) == 8
    assert solve_method(2, [[1,4], [4,5]]) == 0
    assert solve_method(4, [[1,3], [2,6], [8,10], [15,18]]) == 14