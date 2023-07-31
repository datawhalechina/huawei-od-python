def solve_method(n, d, nums):
    nums.sort()
    # 前i个队伍中，最多可以匹配的队伍数量
    dp1 = [0] * (n + 1)
    # 前i个队伍中，最多匹配的队伍数量对应的实力差值总和
    dp2 = [0] * (n + 1)
    for i in range(2, n+1):
        # 考虑当前队伍i-1是否和前一个队伍匹配
        if nums[i-1] - nums[i-2] <= d: # 匹配
            # 判断dp1[i]的取值
            if dp1[i-2] + 1 > dp1[i-1]:
                dp1[i] = dp1[i-2] + 1
                dp2[i] = dp2[i-2] + nums[i-1] - nums[i-2]
            elif dp1[i-2] + 1 < dp1[i-1]:
                dp1[i] = dp1[i-1]
                dp2[i] = dp2[i-1]
            else:
                dp1[i] = dp1[i-1]
                dp2[i] = min(dp2[i-2] + nums[i-1] - nums[i-2], dp2[i-1])
    if dp1[n] == 0:
        return -1
    minDiffsum = dp2[n]
    for i in range(1, n+1):
        if dp1[i] == dp1[n]:
            minDiffsum = min(dp2[i], minDiffsum)
    return minDiffsum

if __name__ == "__main__":
    # 6 30
    # 81 87 47 59 81 18
    n, d = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve_method(n, d, nums))

    assert solve_method(6, 30, [81, 87, 47, 59, 81, 18]) == 57
    assert solve_method(6, 20, [81, 87, 47, 59, 81, 18]) == 12
    assert solve_method(4, 10, [40, 51, 62, 73]) == -1