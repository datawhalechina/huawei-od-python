# encoding: utf-8
"""
@author: Yalin Feng
@file: 142_dictionary-reference.py
@time: 2023/8/8 2:00
@project: huawei-od-python
@desc: 142 查字典
"""

from typing import List


def solve_method(prefix: str, length: int, dict: List[str]) -> str:
    # 空列表results 存储与前缀相匹配的单词
    results = []

    for word in dict:
        # 判断字符串的前缀是否与给定的前缀相同,如果相同，将该字符串添加到results列表中
        if word[0:length] == prefix:
            results.append(word)

    # 如果results列表不为空，使用join()方法将所有的字符串连接成一个字符串，并用换行字符"\n“分隔不同单词，最后返回该字符串
    # 否则，返回一个字符串-1
    return ("\n".join(results)) if results else str(-1)

if __name__ == '__main__':
    print(solve_method("b", 3, ["a", "b", "c"]) == "b")
    print(solve_method("abc", 4, ["a", "ab", "abc", "abcd"]) == "abc\nabcd")
    print(solve_method("a", 3, ["b", "c", "d"]) == "-1")
