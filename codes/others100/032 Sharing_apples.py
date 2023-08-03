#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve(num):
    if len(n) != nums:
        return False
    count = 0
    # 进行异或运算
    for i in n:
        count = count^i
    if count == 0:
        return sum(n) - min(n)
    else:
        return -1
if __name__ == '__main__':
    nums = int(input()) # 输入苹果数量
    n = [int(x) for x in input().split()] # 输入苹果重量
    result = solve(n)
    print(result)

