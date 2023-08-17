#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:058-monogram.py
@Date：2023/08/14 21:00
"""

# 定义数字到字母的映射
digits_mapping = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"],
    ["p", "q", "r"],
    ["s", "t"],
    ["u", "v"],
    ["w", "x"],
    ["y", "z"]
]

# 结果列表
res = []


# 主解决方法
def solve_method():
    num_str = input("请输入数字字符串：")
    no_contain = input("请输入不包含的字符：")
    method(0, num_str, no_contain, "")
    print(",".join(res))


def method(index, num_str, no_contain, temp):
    # 检查临时字符串的长度是否与数字字符串的长度相同
    if len(temp) == len(num_str):
        # 如果长度相同，则检查临时字符串是否不包含指定的字符
        if is_true(no_contain, temp):
            # 如果临时字符串通过检查，则将其添加到结果列表中
            res.append(temp)
    else:
        # 如果临时字符串的长度与数字字符串的长度不相同，则继续构建临时字符串

        # 从数字字符串中获取当前索引的数字，将其转换为digits_mapping列表的索引
        digits_index = int(num_str(index))

        # 使用上一行中计算的索引从digits_mapping列表中获取字符列表
        chars = digits_mapping[digits_index]

        # 对于字符列表中的每个字符，执行以下操作
        for i in range(len(chars)):
            # 递归调用method函数，增加索引并将当前字符添加到临时字符串中
            # 这将继续构建临时字符串，直到其长度与数字字符串的长度相同
            method(index + 1, num_str, no_contain, temp)


# 检查生成的字符串是否不包含指定的字符
def is_true(no_contain, s):
    for c in no_contain:
        if c not in s:
            return True
    return False


# 主程序入口
if __name__ == "__main__":
    solve_method()
