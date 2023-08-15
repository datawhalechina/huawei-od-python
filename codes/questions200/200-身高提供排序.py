def solve_method(n, height, weight):
    arr1 = []
    for i in range(n):
        arr1.append(((height[i], weight[i]),i+1))

    arr2 = sorted(arr1, key=lambda x: x[0])
    return arr2


n = int(input())
height = list(map(int, input().split()))
weight = list(map(int, input().split()))
arr2 = solve_method(n, height, weight)
for i in arr2:
    print(i[1], end='')