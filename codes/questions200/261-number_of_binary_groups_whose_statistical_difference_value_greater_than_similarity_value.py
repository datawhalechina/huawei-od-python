def solve_method(n, nums):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] ^ nums[j] > nums[i] & nums[j]:
                count += 1
    return count

if __name__ == "__main__":
    # 4
    # 4 3 5 2
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(solve_method(n, nums))

    assert solve_method(4, [4,3,5,2]) == 4
    assert solve_method(5, [3,5,2,8,4]) == 8