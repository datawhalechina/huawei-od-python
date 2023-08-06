def solve_method(string):
    string += "#"
    stack = []
    num, temp = 0, ""
    for c in string:
        if c.isdigit():
            num = num * 10 + int(c)
            continue
        if num != 0:  # 数字统计结束，进行计算 - 此时栈肯定非空，且栈顶元素为字母或}
            if stack[-1].isalpha():
                stack[-1] = stack[-1] * num
            elif stack[-1] == "}":
                stack.pop() # 弹出}
                while stack[-1] != "{":
                    temp = stack.pop() + temp
                stack[-1] = temp * num # 弹出{
            num, temp = 0, ""
        stack.append(c)
    return "".join(stack[:-1])

if __name__ == "__main__":
    # {A3B1{C}3}3
    string = input().strip()
    print(solve_method(string))

    assert solve_method("{A3B1{C}3}3") == "AAABCCCAAABCCCAAABCCC"
    assert solve_method("A3") == "AAA"
    assert solve_method("{AD11B1{CF}3}3") == "ADDDDDDDDDDDBCFCFCFADDDDDDDDDDDBCFCFCFADDDDDDDDDDDBCFCFCF"