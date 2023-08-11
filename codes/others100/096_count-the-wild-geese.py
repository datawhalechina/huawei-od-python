#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 096_count-the-wild-geese.py
@time: 2023/8/11 20:18
@project: huawei-od-python
@desc: 096 数大雁
"""


def solve_method(chars):
    if len(chars) % 5 != 0:
        return -1

    quack_str = "quack"
    # 建立桶
    bucket = [0] * len(quack_str)
    # 大雁计数器
    count = 0

    for char in chars:
        if char == quack_str[0]:
            # 如果字符与`q`相等，则相应位置累加1
            bucket[0] += 1
        else:
            # 获取字符在`quack`中的索引
            index = quack_str.index(char)
            # 将前一个字符的计数减1，后一个字符的计数加1
            bucket[index - 1] -= 1
            bucket[index] += 1
            if char == quack_str[-1]:
                bucket[-1] -= 1

        if -1 in bucket:
            # 如果计数中存在-1，说明字符顺序不正确，返回-1
            return -1
        # 更新大雁计数器为当前计数的最大值，统计大雁的叫声重叠数
        count = max(count, sum(bucket))

    if sum(bucket) != 0:
        # 如果计数不为0，说明字符数量不匹配，返回-1
        return -1

    return count


if __name__ == '__main__':
    assert solve_method("quackquack") == 1
    assert solve_method("qaauucqcaa") == -1
    assert solve_method("quacqkuack") == 2
