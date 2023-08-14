#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 179_meet-rules-combination.py
@time: 2023/8/8 23:44
@project: huawei-od-python
@desc: 179 满足规则的组合
"""

from collections import Counter
def solve_method(n, nums):
    s = Counter(nums)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            s[nums[i]]-=1
            s[nums[j]]-=1
            k = (nums[i]-nums[j])
            if k%2==0 and k//2 in s and s[k//2]>0:
                return '{} {} {}'.format(nums[i],nums[j],(k//2))
            s[nums[i]]+=1
            s[nums[j]]+=1
    return 0


if __name__ == '__main__':
    assert solve_method(4, [2,7,3,0]) == '7 3 2'
    assert solve_method(3, [1,1,1]) == 0
