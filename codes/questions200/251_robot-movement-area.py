def solve_method(M, N, matrix):
    maxCount = 0
    # 遍历所有可能的起始位置
    for i in range(M):
        for j in range(N):
            maxCount = max(maxCount, dfs(M, N, matrix, i, j, [[0] * N for _ in range(M)]))
    return maxCount

def dfs(M, N, matrix, i, j, visited):
    count = 1
    visited[i][j] = 1
    for x, y in [[1,0], [-1,0], [0,1], [0,-1]]:
        if i+x >= 0 and i+x < M and j+y >= 0 and j+y < N:
            if not visited[i+x][j+y] and abs(matrix[i+x][j+y] - matrix[i][j]) <= 1:
                count += dfs(M, N, matrix, i+x, j+y, visited)
    return count

if __name__ == "__main__":
    # 4 4
    # 1 2 5 2
    # 2 4 4 5
    # 3 5 7 1
    # 4 6 2 4
    # M网格行数，N网格列数
    M, N = map(int, input().split())
    matrix = []
    for _ in range(M):
        matrix.append(list(map(int, input().split())))
    print(solve_method(M, N, matrix))

    assert solve_method(4, 4, [[1,2,5,2], [2,4,4,5], [3,5,7,1], [4,6,2,4]]) == 6
    assert solve_method(2, 3, [[1,3,5], [4,1,3]]) == 1