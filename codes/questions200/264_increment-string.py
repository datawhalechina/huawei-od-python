def solve_method(str):
    count1 = 0
    A_last_index = str.rfind("A")
    for i in range(A_last_index):
        if str[i] == "B":
            count1 += 1

    count2 = 0
    B_first_index = str.find("B")
    for i in range(B_first_index, len(str)):
        if str[i] == "A":
            count2 += 1
    return min(count1, count2)

if __name__ == "__main__":
    # AABBA
    str = input().strip()
    print(solve_method(str))

    assert solve_method("AABBA") == 1