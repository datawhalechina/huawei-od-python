def addNumber(nums, n):
    sorted_number = sorted(list(set(nums)))
    if len(sorted_number) < 2 * n:
        return -1
    return sum(sorted_number[:n]) + sum(sorted_number[-n:])


if __name__ == '__main__':
    m = int(input().strip())
    nums = list(map(int, input().strip().split(' ')))
    n = int(input().strip())
    res = addNumber(nums, n)
    print(res)
