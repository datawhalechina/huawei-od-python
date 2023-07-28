# 输入获取
m, n = map(int, input().split())
matrix = [input().split() for i in range(m)]


# 算法入口
def getResult(matrix, m, n):
    checked = set()

    offsets = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def dfs(i, j, count, out):
        pos = f"{i}-{j}"

        if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] == "X" or pos in checked:
            return count

        checked.add(pos)

        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            out.append([i, j])

        count += 1

        for offsetX, offsetY in offsets:
            newI = i + offsetX
            newJ = j + offsetY
            count = dfs(newI, newJ, count, out)

        return count

    ans = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "O" and f"{i}-{j}" not in checked:
                out = []
                count = dfs(i, j, 0, out)
                if len(out) == 1:
                    tmp = out[0][:]
                    tmp.append(count)
                    ans.append(tmp)

    if len(ans) == 0:
        return "NULL"

    ans.sort(key=lambda x: -x[2])

    if len(ans) == 1 or ans[0][2] > ans[1][2]:
        return " ".join(map(str, ans[0]))
    else:
        return ans[0][2]


# 算法调用
print(getResult(matrix, m, n))