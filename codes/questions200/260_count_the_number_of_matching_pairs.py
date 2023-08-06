def solve_method(A, B):
    dict_A = {}
    for a in A:
        dict_A[a] = dict_A.get(a, 0) + 1

    dict_B = {}
    for b in B:
        dict_B[b] = dict_B.get(b, 0) + 1

    summ = 0
    for key in dict_A:
        if key in dict_B:
            summ += dict_A[key] * dict_B[key]
    return summ

if __name__ == "__main__":
    # 5
    # 4
    # 1 2 3 4 5
    # 4 3 2 1
    M = int(input().strip())
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    print(solve_method(A, B))

    assert solve_method([1,2,3,4,5], [4,3,2,1]) == 4
    assert solve_method([1,2,4,4,2,1], [1,2,3]) == 4