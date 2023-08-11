# encoding: utf-8
"""
@author: Yalin Feng
@file: 149_k-elements-sum.py
@time: 2023/8/11 17:00
@project: huawei-od-python
@desc: 149 求有多少种K个数的组合使和等于目标
"""
from typing import List


def solve_method(nums: List[int], K: int, T: int) -> int:
    # 1. 检查输入是否有效
    assert nums and (2 <= len(nums) <= 200) and (2 <= K <= 100) and (-10 ** 9 <= T <= 10 ** 9) \
           and (-10 ** 9 <= all(nums) <= 10 ** 9)

    # 2. 排序 nums,方便剪枝
    nums = sorted(nums)

    # 3. combination(array,k,t)= 在序列array中找k个数的组合等于t,返回组合的个数
    def combination(array: List[int], k: int, t: int) -> int:
        # 终止条件1: 不够 k个数; 序列最小的数都比 t大
        if len(array) < k or array[0] > t:
            return 0

        # 终止条件2: 只有一个要寻找的数
        if k == 1:
            return 1 if t in array else 0

        cnt = 0
        for i in range(len(array)):
            cnt += combination(array[i + 1:], k - 1, t - array[i])
        return cnt

    # 4. 因为数列里有相同的数字,为避免重复,不能直接调用 combination(nums,K,T)
    count = 0
    i = 0
    while i < len(nums):
        num = nums[i]
        count += combination(nums[i + 1:], K - 1, T - num)

        # 获取数字num能形成多少个组合后，让索引i指向下一个值不同的数字,这是避免重复的关键
        while i < len(nums) and num == nums[i]:
            i += 1

    return count


if __name__ == '__main__':
    res1 = solve_method([-1, 0, 1, 2, -1, -4], 3, 0)
    print(res1)
    assert res1 == 2

    res2 = solve_method([2, 7, 11, 15], 2, 9)
    print(res2)
    assert res2 == 1

    res3 = solve_method([10, 10, 10, 1, 1], 4, 31)
    print(res3)
    assert res3 == 1
