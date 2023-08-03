#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve(n, num1, num2):
    count = 0
    for i in range(n):
        # 比较两个二进制数的相应位
        if num1[i] != num2[i]:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input()) # 输入n，表示二进制数的位数
    num1 = input() # 输入长度为n的二进制数
    num2 = input() # 输入长度为n的二进制数

    result = solve(n, num1, num2)
    print(result)

