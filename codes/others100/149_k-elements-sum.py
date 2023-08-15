# encoding: utf-8
"""
@author: Yalin Feng
@file: 149_k-elements-sum.py
@time: 2023/8/11 17:00
@project: huawei-od-python
@desc: 149 求有多少种K个数的组合使和等于目标
"""


def solve_method(nums, k, target):
    if not (nums and (2 <= len(nums) <= 200)
            and (2 <= k <= 100)
            and (-10 ** 9 <= target <= 10 ** 9)
            and (-10 ** 9 <= all(nums) <= 10 ** 9)):
        return -1

    result = []
    current_combination = []

    def backtracking(start_index, current_sum):
        if len(current_combination) == k and current_sum == target:
            # 当和值等于目标值，并且正好有k个元素，则保存该组合
            result.append(list(current_combination))
            return

        if len(current_combination) > k or current_sum > target:
            # 如果该组合的和超过了目标值，或个数超过了k个，则返回
            return

        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                # 避免重复取值
                continue
            current_combination.append(nums[i])
            backtracking(i + 1, current_sum + nums[i])
            current_combination.pop()

    nums.sort()
    backtracking(0, 0)
    # 去重处理
    result = list(set(tuple(comb) for comb in result))
    result = [list(comb) for comb in result]
    return len(result)


if __name__ == '__main__':
    assert solve_method([-1, 0, 1, 2, -1, -4], 3, 0) == 2
    assert solve_method([2, 7, 11, 15], 2, 9) == 1
    assert solve_method([10, 10, 10, 1, 1], 4, 31) == 1
