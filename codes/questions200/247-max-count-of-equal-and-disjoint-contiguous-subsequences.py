def solve_method(N, nums):
    max_count = 0
    # sum_count_dict, sum_pos_dict
    sum_count_dict = {}
    sum_pos_dict = {}
    dp = nums[:]
    for i in range(N):  # 枚举子序列的长度
        for j in range(N-i):  # 枚举子序列的起始位置
            if i > 0:
                dp[j] += nums[j+i]
            summ = dp[j]
            # 判断该和是否记录过
            if summ not in sum_count_dict:
                sum_count_dict[summ] = 0
                sum_pos_dict[summ] = set()

            # 判断该索引是否被记录过
            exist = False
            pos = sum_pos_dict[summ]
            for k in range(j, j+i+1):
                if k in pos:
                    exist = True
                    break
            # 索引没有被记录过
            if not exist:
                sum_count_dict[summ] += 1
                max_count = max(max_count, sum_count_dict[summ])
                for k in range(j, j+i+1):
                    pos.add(k)
                sum_pos_dict[summ] = pos
    return max_count

if __name__ == "__main__":
    # 10
    # 8 8 9 1 9 6 3 9 1 0
    # -1 0 4 -3 6 5 -6 5 -7 -3
    N = int(input())
    nums = list(map(int, input().split()))
    print(solve_method(N, nums))

    assert solve_method(10, [8, 8, 9, 1, 9, 6, 3, 9, 1, 0]) == 4
    assert solve_method(10, [-1, 0, 4, -3, 6, 5, -6, 5, -7, -3]) == 3