def maxCardsNumber(nums):
    return ''.join(sorted(nums))


if __name__ == '__main__':
    nums = input().strip().split(',')
    res = maxCardsNumber(nums)
    print(res)
