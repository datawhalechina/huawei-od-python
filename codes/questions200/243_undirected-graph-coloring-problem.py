def solve_method(n, m, edges):
    count = 0
    for num in range(1 << n):
        # 标记是否满足要求
        flag = True
        for edge in edges:
            if (num & (1 << edge[0])) and (num & (1 << edge[1])):
                flag = False
                break
        count += flag
    return count

if __name__ == "__main__":
    # 3 3
    # 0 1
    # 0 2
    # 1 2
    # n个节点，m条边
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(solve_method(n, m, edges))
    assert solve_method(3, 3, [[0,1], [0,2], [1,2]]) == 4
    assert solve_method(4, 3, [[0,1], [1,2], [2,3]]) == 8