#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter
def remove_minimum_characters(line):
    # 统计字符频率
    freq = Counter(line)
    # 求最小值
    min_freq = min(freq.values ())
    result = ''
    for c in line:
        if freq[c] != min_freq:
            result += c
    if result != '':
      return result
    else:
      return 'empty' 

if __name__ == '__main__':
    line = input()
    result = remove_minimum_characters(line)
    print(result)

