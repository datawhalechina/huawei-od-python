#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_prime_factors(num):  
    # 判断是否是质数
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # 将num分解成两个数相乘
    for i in range(2, num):
        if num % i ==0:
            if is_prime(i) and is_prime(num // i):
                return (i, num // i)
    
    return "NO"

if __name__ == '__main__':
    num = int(input())
    result = find_prime_factors(num)
    print(result)

