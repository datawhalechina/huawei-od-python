def mergeArray(nums, n):
    ans = []
    flag = True
    times = 1
    while flag:
        flag = False
        for item in nums:
            if (times - 1) * n < len(item):
                ans.extend(item[(times - 1) * n:times * n])
                flag = True
        times += 1
    return ans


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    nums = []
    for _ in range(m):
        nums.append(list(map(int, input().strip().split(','))))

    res = mergeArray(nums, n)
    print(','.join([str(atom) for atom in res]))
