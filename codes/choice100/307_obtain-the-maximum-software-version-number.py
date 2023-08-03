#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 307_obtain-the-maximum-software-version-number.py
@time: 2023/8/3 11:44
@project: huawei-od-python
@desc: 307 获取最大软件版本号
"""
import re


def solve_method(version1: str, version2: str) -> str:
    pattern = r"^(\d+)(?:\.(\d+))(?:\.(\d+))?(?:\-(.+))?$"

    major1, minor1, patch1, mile1 = re.findall(pattern, version1)[0]
    major2, minor2, patch2, mile2 = re.findall(pattern, version2)[0]

    # 比较主版本，按照数值比较
    if major1 != major2:
        return version1 if int(major1) > int(major2) else version2

    # 比较次版本，按照数值比较
    if int(minor1) != int(minor2):
        return version1 if int(minor1) > int(minor2) else version2

    # 比较增量版本，按照数值比较
    if patch1 != "" and patch2 != "":
        if int(patch1) > int(patch2):
            return version1
        elif int(patch1) < int(patch2):
            return version2
    elif patch1 != "" and patch2 == "":
        return version1
    elif patch1 == "" and patch2 != "":
        return version2

    # 比较里程碑，按照字典序比较
    if mile1 != "" and mile2 != "":
        if mile1 > mile2:
            return version1
        elif mile1 < mile2:
            return version2
    elif mile1 != "" and mile2 == "":
        return version1
    elif mile1 == "" and mile2 != "":
        return version2

    return version1


if __name__ == '__main__':
    assert solve_method("2.5.1-C", "1.4.2-D") == "2.5.1-C"
    assert solve_method("1.3.11-S2", "1.3.11-S13") == "1.3.11-S2"
    assert solve_method("1.05.1", "1.5.01") == "1.05.1"
    assert solve_method("1.5", "1.5.0") == "1.5.0"
    assert solve_method("1.5.1-A", "1.5.1-a") == "1.5.1-a"
