#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 008_code-editor.py
@time: 2023/9/1 14:36
@project: huawei-od-python
@desc: 008 代码编辑器
"""


def solve_method(code, ops):
    result = list(code)

    index = 0
    for op in ops:
        operation, value = op.split()
        if operation == "FORWARD":
            # 指针向前（右）移动X
            index = min(index + int(value), len(result))
        elif operation == "BACKWARD":
            # 指针向后（左）移动X
            index = max(index - int(value), 0)
        elif operation == "SEARCH-FORWARD":
            # 从指针当前位置向前查找word，并将指针移动到word的起始位置
            _index = code.rfind(value, 0, index)
            if _index != -1:
                index = _index
        elif operation == "SEARCH-BACKWARD":
            # 在文本中向后查找word，并将指针移动到word的起始位置
            _index = code.find(value, index)
            if _index != -1:
                index = _index
        elif operation == "INSERT":
            # 在指针当前位置前插入word，并将指针移动到word的结尾
            result.insert(index, value)
            index += len(value)
        elif operation == "REPLACE":
            # 在指针当前位置替换并插入字符
            result[index: index + len(value)] = value
        elif operation == "DELETE":
            del result[index: index + int(value)]

    return "".join(result)


if __name__ == '__main__':
    ops = ["INSERT h"]
    assert solve_method("ello", ops) == "hello"

    ops = ["FORWARD 1", "INSERT e"]
    assert solve_method("hllo", ops) == "hello"

    ops = ["FORWARD 1000", "INSERT o"]
    assert solve_method("hell", ops) == "hello"

    ops = ["REPLACE HELLO"]
    assert solve_method("hello", ops) == "HELLO"

    ops = ["REPLACE HELLO_WORLD"]
    assert solve_method("hello", ops) == "HELLO_WORLD"

    ops = ["FORWARD 10000", "REPLACE O"]
    assert solve_method("hell", ops) == "hellO"
