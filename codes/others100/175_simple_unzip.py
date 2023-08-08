#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 175_simple_unzip.py
@time: 2023/8/8 21:27
@project: huawei-od-python
@desc: 175 简易压缩算法
"""


def solve_method(s):
    stack = []

    # 1.初筛
    # 先判断是否是数字和小写字母
    for i in s:
        if i.isdigit() or (i.isalpha() and i.islower()):
            continue
        else:
            return '!error'
    
    # 2.将数字和字母配对在一起
    stack = []
    for i in s:
        if stack:
            # 数字相邻则相连
            if i.isdigit():
                if stack[-1].isdigit():
                    stack[-1]+=i
                    continue
            # 字母前是数字则相连，字母前是相同的字母则相连
            else:
                if stack[-1].isdigit() or stack[-1][-1]==i:
                    stack[-1]+=i
                    continue
        # 其余情况直接append
        stack.append(i)
        
    # 将配对的数字和字母组合到一起，存在stack中
    # print(stack)

    # 3.遍历整个stack内的元素，同时判断元素是否合法
    res = ''
    for string in stack:
        num = ''
        alpha = ''
        for char in string:
            if char.isdigit():
                num+=char
            else:
                alpha+=char
        # 不合法的规则：既有数字，还有两个字母；或者字母数量大于2
        if (num and len(alpha)==2) or (len(alpha)>2):
            return '!error'
        else:
            if num:
                res+=alpha*int(num)
            else:
                res+=alpha
    return res

if __name__ == '__main__':
    assert solve_method("4dff2d") == 'ddddffdd'
    assert solve_method("24d2ff2d") == '!error'
    assert solve_method("24dfff2d") == '!error'
    assert solve_method("4#dff2dabcd") == '!error'
