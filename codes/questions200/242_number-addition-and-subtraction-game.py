def solve_method(s, t, a, b):
    diff = abs(s - t)
    min_count = 0
    while ((diff - min_count * a) % b != 0) and ((diff + min_count * a) % b != 0):
        min_count += 1
    return min_count

if __name__ == "__main__":
    s, t, a, b = map(int, input().split())
    print(solve_method(s, t, a, b))
    assert solve_method(1, 10, 5, 2) == 1
    assert solve_method(11, 33, 4, 10) == 2