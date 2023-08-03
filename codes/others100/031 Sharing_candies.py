#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve(x: int):
    if x > 1000000:
      return False
    # 当x=2时，返回1
    if x == 2:
        return 1  
    # 当x为偶数时
    if x % 2 == 0:
        return solve(x // 2) + 1  
    # 当x为奇数时
    else:
        return min(solve(x + 1) + 1, solve(x - 1) + 1)
 
 
if __name__ == "__main__":
    n = int(input()) 
    result = solve(n)
    print(result)

