#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter

def mode_and_median(nums):
    count = Counter(nums) # 使用Counter计数

    max_count = max(count.values()) # 获取最大的频次
    modes = [num for num, freq in count.items() if freq == max_count] 

    sorted_nums = sorted(modes) # 将数组排序
    length = len(sorted_nums)

    if length % 2 == 1: # 如果数组长度为奇数，中位数为中间的那个元素
        median = sorted_nums[length // 2] 
    else: # 如果数组长度为偶数，中位数为中间两个元素的平均值
        median = (sorted_nums[length // 2 - 1] + sorted_nums[length // 2]) // 2 

    return median

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    result = mode_and_median(nums)
    print(result)

