#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve(str1, str2):
    length = len(str1)
    temp = []
    for i in range(len(str2) - length + 1):
        temp = list(str2[i:i+length])
        j = 0
        while j < length:
            if str1[j] in temp:
                temp.remove(str1[j])
            j += 1
        if temp == []:
            return i
    return -1

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    result = solve(str1, str2)
    print(result) 

