def solve_method(n, ints, base):
    arr = sorted(filter(lambda x: x < base,ints))
    count = n - len(arr)
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] >= base:
            count += 1
            i += 1
            j -= 1
        else:
            i += 1
    print(count)


n = int(input().strip())#总人数
ints = list(map(int, input().split()))#每个人的能力
base = int(input().strip())#队伍最低能力值
solve_method(n, ints, base)