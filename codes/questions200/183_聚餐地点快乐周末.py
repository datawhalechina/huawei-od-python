from collections import deque

def bfs(row,col):
    queue = deque([(row,col)])
    visited = set([(row,col)])
    while queue:
        r,c=queue.popleft()

        if (r,c)==end_spot:
            return True
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if not (0 <= nr <m and 0 <= nc <n) or map_[nr][nc] == "1":
                continue
            if (nr,nc) not in visited:
                queue.append((nr,nc))
                visited.add((nr,nc))

    return False

n,m = map(int,input().split())
map_ = [input().split() for _ in range(m)]

start_spots = []
end_spots = []

for i in range(m):
    for j in range(n):
        if map_[i][j] == "2":
            start_spots.append((i,j))
        elif map_[i][j]== "3":
            end_spots.append((i,j))
count = 0

for end_spot in end_spots:
    if all(bfs(start_spot[0],start_spot[1]) for start_spot in start_spots):
        count +=1

print(count)


