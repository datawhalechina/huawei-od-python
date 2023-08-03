#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def realfare(n):
    real = 0
    count = 0
    for i in range(len(fakefare)-1, -1 ,-1):
        n = int(fakefare[i])
        # 大于4的情况
        if n>4:
            n = n-1
        real = real + n* 9**count
        count = count+1
    return real

if __name__ == '__main__':
    fakefare = input()
    result = realfare(fakefare)
    print(result)

