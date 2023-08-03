#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve_method(line):
    strings = line.split(" ")
    nums = []
    for string in strings:
        nums.append(int(string))
    is_change = True
    while len(nums) != 1 and is_change:
        for i in range(1, len(nums)):
            n = i
            num = nums[i]
            is_end = False
            count = 0
            while not is_end:
                n -= 1
                count += nums[n]
                if count == num:
                    if i >= n:
                        del nums[n:i + 1]
                    nums.insert(n, 2 * num)
                    is_change = True
                    break
                if count > num or n == 0:
                    is_end = True
                    is_change = False
            if is_change:
                break

    res = ""
    for i in range(len(nums) - 1, -1, -1):
        res += str(nums[i])
        if i != 0:
            res += " "

    print(res)


if __name__ == '__main__':
    line = input("请输入一组数字，以空格分隔: ").strip()
    solve_method(line)
    

