# coding: utf-8
import sys

def solve_method(nums_str):
    # 将输入的数字字符串转换为整数列表
    nums = list(map(int, nums_str.split()))
    # 去除重复的数字
    nums = list(set(nums))
    # 初始化最小和为系统最大值
    min_sum = sys.maxsize
    # 初始化结果集合
    res_set = set()
    # 遍历数字列表
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            a, b = nums[i], nums[j]
            if a != b:
                # 计算当前两个数字的绝对值和
                cur_sum = abs(a + b)
                if cur_sum < min_sum:
                    # 如果当前和小于最小和，则更新最小和和结果集合
                    min_sum = cur_sum
                    res_set = set([a, b])
    # 如果结果集合不为空，则输出结果集合中的数字和最小和
    if len(res_set) != 0:
        print(*res_set, min_sum)

if __name__ == "__main__":
    # 输入数字字符串，调用 solve_method 函数进行处理
    nums_str = input()
    solve_method(nums_str)