#!/usr/bin/env python
# encoding: utf-8
"""
@author: Yalin Feng
@file: 147_narcissistic-number2.py
@time: 2023/8/11 14:30
@project: huawei-od-python
@desc: 147 水仙花数2
"""
from typing import List


def solve_method(line: str) -> int:
    # 1. 确保输入有效
    assert len(line) <= 200

    # 2. 使用 lambda表达式定义一个匿名函数，用于计算字符串的ascii码之和
    ascii_sum = lambda string: sum(map(ord, string))

    # 3. 定义一个匿名函数，用于判断一个数是不是水仙花数,返回bool类型
    # is_narcissistic = lambda num: num in [153, 370, 371, 407] # 这里已经知道3位数的水仙花数只有4个，算是取巧的写法
    is_narcissistic = lambda num: num == (num % 10) ** 3 + (num // 10 % 10) ** 3 + (num // 100) ** 3

    # 4. 定义一个可以递归的方法,判断某个字符串能否成功分割
    # 返回结果格式为List[List(str)] 如: f3d5a8 -> [["f3","@d5a8"],["f3@d5","a8"]]
    def my_split(string: str) -> List[List[str]]:
        res = []
        # 注意range的左右端点; 用 [:len(string)]才能获取整个字符串
        for i in range(1, len(string) + 1):
            sub1 = string[:i]
            sub2 = string[i:]
            if is_narcissistic(ascii_sum(sub1)):
                # sub2为空串(整个字符串是一个水仙花数
                if sub2 == '':
                    return [[sub1, ]]

                # sub2不为空串,递归调用split去分割sub2
                else:
                    tmp = my_split(sub2)
                    # tmp是一个string的二维列表,我们在sub2的每种分割(每一行)前面插入sub1,表示一次完整分割
                    for row in tmp:
                        row.insert(0, sub1)
                        res.append(row)
        return res

    ret = my_split(line)

    # 5. 若分割成功且结果不唯一,返回-1;分割不成功则返回0; 否则返回分割后子串的数目(ret[0]的长度)
    if len(ret) > 1:
        return -1
    elif len(ret) == 0 or len(ret[0]) == 1:
        return 0
    else:
        return len(ret[0])


if __name__ == '__main__':
    res1 = solve_method("abc")
    print(res1)
    assert res1 == 0

    res2 = solve_method("f3@d5a8")
    print(res2)
    assert res2 == -1

    res3 = solve_method("AXdddF")
    print(res3)
    assert res3 == 2

    res4 = solve_method("f3")
    print(res4)
    assert res4 == 0
