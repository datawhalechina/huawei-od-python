def decodeString(s):
    prev, curr = '', ''
    stack = []
    num = 0
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == '[':
            stack.append(curr)
            stack.append(num)
            curr = ''
            num = 0
        elif s[i] == ']':
            curr_num = stack.pop()
            prev = stack.pop()
            curr = prev + curr_num * curr
        else:
            curr += s[i]

    return curr


if __name__ == '__main__':
    compressed_string = input().strip()
    res = decodeString(compressed_string)
    print(res)
