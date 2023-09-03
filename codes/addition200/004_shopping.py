#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 004_shopping.py
@time: 2023/9/3 23:18
@project: huawei-od-python
@desc: 004 购物
"""
import heapq

class Item:
    def __init__(self, cur_sum, next_idx, next_sum):
        self.cur_sum = cur_sum
        self.next_idx = next_idx
        self.next_sum = next_sum
    def __lt__(self, other):
        return self.next_sum < other.next_sum

def solve_method(n, k, nums):
    nums.sort()

    # 空组合当前的和为0，将要加入的下一个元素为nums[0]（即索引为0），将要产生的新组合的和为0+nums[0]
    pq = [Item(0, 0, nums[0])]
    res = []
    while k > 0 and pq:
        # 取出优先队列中最小组合（注意这里的最小，指的是"将要产生的新组合"最小）
        cur_item = heapq.heappop(pq)
        res.append(cur_item.next_sum)
        k -= 1
        # 如果当前组合模型还有可合入的下一个元素，则说明可以基于当前组合模型产生一个新组合
        if cur_item.next_idx + 1 < n:
            # 基于当前组合模型产生的新组合，也是本轮最小的组合
            heapq.heappush(pq, Item(cur_item.next_sum, cur_item.next_idx + 1, cur_item.next_sum + nums[cur_item.next_idx + 1]))
            # 当前组合需要更新`next_idx`后，重新加入优先队列
            cur_item.next_idx += 1
            cur_item.next_sum = cur_item.cur_sum + nums[cur_item.next_idx]
            heapq.heappush(pq, cur_item)
    return res

if __name__ == '__main__':
    # n, k = map(int, input().split())
    # nums = list(map(int, input().split()))
    # print(solve_method(n, k, nums))
    # print(solve_method(4, 15, [1, 2, 3, 4]))

    assert solve_method(5, 6, [1, 1, 2, 3, 3]) == [1, 1, 2, 2, 3, 3]
    assert solve_method(4, 15, [1, 2, 3, 4]) == [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 10]
    assert solve_method(3, 7, [1, 10, 100]) == [1, 10, 11, 100, 101, 110, 111]