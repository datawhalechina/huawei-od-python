def solve_method(N, nums, visited):
    count = 0
    for k in range(2, N):
        c = nums[k]
        # 排除遍历过的数字
        if visited[k] == 1:
            continue

        i = 0; j = k - 1;
        while i < j:
            # 排除遍历过的数字
            while i < j and visited[i] == 1:
                i += 1
            while i < j and visited[j] == 1:
                j -= 1
            if i == j:
                break

            if nums[i] ** 2 + nums[j] ** 2 < c ** 2:
                i += 1
            elif nums[i] ** 2 + nums[j] ** 2 > c ** 2:
                j -= 1
            else:
                visited[i] = visited[j] = visited[k] = 1
                count = 1 + solve_method(N, nums, visited)
                visited[i] = visited[j] = visited[k] = 0
                break
    return count

if __name__ == "__main__":
    # 1
    # 7 3 4 5 6 5 12 13
    # 7 3 4 5 6 6 12 13
    T = int(input())
    for _ in range(T):
        line = list(map(int, input().split()))
        N = line[0]
        print(solve_method(N, sorted(line[1:]), [0] * N))

    assert solve_method(7, [3, 4, 5, 6, 5, 12, 13], [0] * 7) == 2
    assert solve_method(7, [3, 4, 5, 6, 6, 12, 13], [0] * 7) == 1