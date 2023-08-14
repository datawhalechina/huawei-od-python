def solve_method(str):
    total_A = str.count("A")
    res = total_A
    count_A = 0
    for i in range(len(str)):
        if str[i] == "A":
            count_A += 1
        res = min(res, i + 1 - count_A + total_A - count_A)
    return res

if __name__ == "__main__":
    # AABBA
    str = input().strip()
    print(solve_method(str))

    assert solve_method("AABBA") == 1
    assert solve_method("BAABBABBAB") == 3