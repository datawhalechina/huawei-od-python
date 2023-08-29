#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 071_seat-adjustment
@time:  2023/8/24 10:31
@project:  huawei-od-python
@desc: 071 座位调整
"""


def solve_method(nums):
    if len(nums) < 3:
        return 0 if sum(nums) > 0 else 1

    if sum(nums) >= len(nums) // 2 + 1:
        return 0
    ans = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            continue
        elif i == 0 and nums[i + 1] == 0:
            # 如果第一个位置和第二个位置是空的，则第一个位置可坐人
            ans += 1
            nums[i] = 1
        elif i == n - 1 and nums[i - 1] == 0:
            # 如果最后一个位置和倒数第二个位置是空的，则最后一个位置可坐人
            ans += 1
            nums[i] = 1
        else:
            # 如果前一个和后一个均为0，则当前位置可坐人
            if nums[i - 1] == 0 and nums[i + 1] == 0:
                ans += 1
                nums[i] = 1
    return ans


if __name__ == '__main__':
    assert solve_method([1, 0, 0, 0, 1]) == 1
    assert solve_method([0, 0, 0, 0, 0]) == 3
    assert solve_method([1, 0, 0, 0, 0, 0]) == 2
