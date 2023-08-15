#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 168_disk-capacity.py
@time: 2023/8/8 22:30
@project: huawei-od-python
@desc: 168 磁盘容量
"""


def solve_method(n, disks):
    def cmp(x):
        res = 0
        left = right = 0
        while right < len(x):
            if x[right].isdigit():
                right += 1
            elif x[right] == 'M':
                res += int(x[left:right])
                right += 1
                left = right
            elif x[right] == 'G':
                res += int(x[left:right]) * 1024
                right += 1
                left = right
            elif x[right] == 'T':
                res += int(x[left:right]) * 1024 * 1024
                right += 1
                left = right
        return res

    # 按照cmp函数进行排序
    # 排序规则，将其全部转化为M最小单位来比较大小
    # 为了防止转换成M数值过大而溢出，也可以转成G或者T皆可
    disks.sort(key=cmp)
    return disks


if __name__ == '__main__':
    disks = ['1T', '20M', '3G', '10G6T', '3M12G9M']
    assert solve_method(5, disks) == ['20M', '3G', '3M12G9M', '1T', '10G6T']

    disks = ['1G', '2G', '1024M']
    assert solve_method(3, disks) == ['1G', '1024M', '2G']

    disks = ['2G4M', '3M2G', '1T']
    assert solve_method(3, disks) == ['3M2G', '2G4M', '1T']
