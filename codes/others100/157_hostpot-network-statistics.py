#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 157_hostpot-network-statistics.py
@time: 2023/8/29 0:20
@project: huawei-od-python
@desc: 157 热点网络统计
"""
from collections import Counter


def solve_method(lines):
    result = []
    start_pos = 0
    counter = Counter()
    for i in range(len(lines)):
        if lines[i].isdigit():
            counter.update(lines[start_pos:i])
            top_urls = counter.most_common(int(lines[i]))
            result.append([x[0] for x in top_urls])
            start_pos = i + 1
    return result


if __name__ == '__main__':
    lines = ["news.qq.com", "news.sina.com.cn", "news.qq.com", "news.qq.com",
             "game.163.com", "game.163.com", "www.huawei.com", "www.cctv.com",
             "3", "www.huawei.com", "www.cctv.com", "www.huawei.com",
             "www.cctv.com", "www.huawei.com", "www.cctv.com", "www.huawei.com",
             "www.cctv.com", "www.huawei.com", "3"]
    assert solve_method(lines) == [["news.qq.com", "game.163.com", "news.sina.com.cn"],
                                   ["www.huawei.com", "www.cctv.com", "news.qq.com"]]

    lines = ["news.qq.com", "www.cctv.com", "1",
             "www.huawei.com", "www.huawei.com", "2",
             "3"]
    assert solve_method(lines) == [["news.qq.com"],
                                   ["www.huawei.com", "news.qq.com"],
                                   ["www.huawei.com", "news.qq.com", "www.cctv.com"]]
