from collections import deque


def reconstruct_mars_grid(grid):
    rows = len(grid)
    if rows == 0:
        return -1
    cols = len(grid[0])

    # 统计初始宜居区和待改造区的数量
    inhabited_count = 0
    to_be_reconstructed_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "YES":
                inhabited_count += 1
            elif grid[i][j] == "NO":
                to_be_reconstructed_count += 1

    # 如果待改造区数量为0，则已经全部变成宜居区，返回0
    if to_be_reconstructed_count == 0:
        return 0

    # 初始化BFS队列和访问标记数组
    queue = deque()
    visited = [[False] * cols for _ in range(rows)]

    # 将初始宜居区加入队列，并标记为已访问
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "YES":
                queue.append((i, j))
                visited[i][j] = True

    # 定义四个方向的偏移量
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    days = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < rows and ny >= 0 and ny < cols and not visited[nx][ny]:
                    if grid[nx][ny] == "NO":
                        # 将待改造区改造成宜居区
                        grid[nx][ny] = "YES"
                        to_be_reconstructed_count -= 1
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        days += 1

        # 如果待改造区数量为0，则已经全部变成宜居区，返回天数
        if to_be_reconstructed_count == 0:
            return days

    # 如果无法将待改造区全部变成宜居区，返回-1
    return -1


# 读取输入
grid = []
while True:
    try:
        row = input().split()
        if not row:
            break
        grid.append(row)
    except EOFError:
        break

# 调用函数计算可改造区是否能全部变成宜居区，以及改造的太阳日天数
result = reconstruct_mars_grid(grid)

# 输出结果
print(result)
