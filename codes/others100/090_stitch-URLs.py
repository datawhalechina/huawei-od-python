#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 090_stitch-URLs.py
@time: 2023/8/10 17:28
@project: huawei-od-python
@desc: 090 拼接URL
"""


def solve_method(urls):
    urls = urls.split(",")
    if len(urls) == 0:
        return "/"

    urls = "/".join([x.strip("/") for x in urls])
    result = urls if urls == "/" else "/" + urls
    return result


if __name__ == '__main__':
    assert solve_method("/acm,/bb") == "/acm/bb"
    assert solve_method("/abc/,/bcd") == "/abc/bcd"
    assert solve_method("/acd,bef") == "/acd/bef"
    assert solve_method(",") == "/"
