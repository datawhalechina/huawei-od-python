def solve_method(nums):
    dict = {}
    for num in nums:
        dict[num] = dict.get(num, 0) + 1

    stack = []
    for num in nums:
        if stack and dict[stack[-1]] > 2 and stack[-1] < num:
            dict[stack[-1]] -= 1
            stack.pop()
        stack.append(num)

    # 从后向前依次删除元素，确保每个元素最多出现两次
    res = []
    while stack:
        if dict[stack[-1]] > 2:
            dict[stack[-1]] -=1
            stack.pop()
        else:
            res.insert(0, stack.pop())
    return "".join(res)

if __name__ == "__main__":
    # 4533
    input_str = input().strip()
    nums = [c for c in input_str]
    print(solve_method(nums))

    assert solve_method("34533") == "4533"
    assert solve_method("5445795045") == "5479504"
    assert solve_method("5554") == "554"