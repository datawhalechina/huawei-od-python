#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 276_find-key.py
@time: 2023/7/13 20:27
@project: huawei-od-python
@desc: 276 寻找密码
"""


def solve_method(line):
    codebook = line.split()
    # 保证字典序
    codebook.sort()
    # 用于去重判断
    code_set = set(codebook)
    # 逆向遍历密码本
    for i in range(len(codebook) - 1, -1, -1):
        code = codebook[i]
        tmp_code = code[:-1]
        # 是否存在的标识
        flag = True
        # 循环判断从末尾开始依次去掉一位的密码是否在密码本中
        while len(tmp_code) > 0:
            if tmp_code in code_set:
                tmp_code = tmp_code[:-1]
            else:
                flag = False
                break
        if flag:
            return code

    return ""


if __name__ == '__main__':
    assert solve_method("h he hel hell hello") == "hello"
    assert solve_method("b eredderd bw bww bwwl bwwln bwwlm") == "bwwln"
