#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 047_rearrange-books.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 047 叠放书籍
"""


def rearrange_books(nums):
    def getMaxLIS(nums):
        dp = [nums[0]]
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                ans += 1
            else:
                l, r = 0, ans - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if dp[mid] == nums[i]:
                        l = mid
                        break
                    elif dp[mid] > nums[i]:
                        r = mid - 1
                    elif dp[mid] < nums[i]:
                        l = mid + 1
                dp[l] = nums[i]

        return ans

    nums = sorted(nums, key=lambda x: (x[0], -x[1]))
    widths = [x[1] for x in nums]

    return getMaxLIS(widths)


if __name__ == '__main__':
    nums = eval(input().strip())
    res = rearrange_books(nums)
    print(res)
