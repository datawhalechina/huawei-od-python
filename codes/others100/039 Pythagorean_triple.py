#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve(n, m):
    result = []
    
    # 判断是否是互质
    def is_coprime(a, b, c):
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x
        
        return gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) == 1
    
    # 求勾股数A、B、C
    for a in range(n, m+1):
        for b in range(a, m+1):
            # c^2 = a^2+b^2
            c_squared = a**2 + b**2
            c = int(c_squared ** 0.5)
            if c_squared == c**2 and c <= m and is_coprime(a, b, c):
                result.append((a, b, c))
    
    return result

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    res = solve(n,m)
    print(res)

