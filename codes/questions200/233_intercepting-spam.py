#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 233_intercepting-spam.py
@time: 2023/8/17
@project: huawei-od-python
@desc: 233 垃圾信息拦截 
"""
from collections import defaultdict


def solve_method(itemNum, items, target_id):
    # A发送短信的接收者集合
    sent_to = set()
    # 发给A的发送者集合
    received_from = set()
    # 接收者的短信数量字典，key为接收者ID，value为接收的短信数量
    sent_to_count = defaultdict(int)
    # 发送者的短信数量字典，key为发送者ID，value为发送者的短信数量
    received_from_count = defaultdict(int)
    # A发送的短信数
    sent_mails_num = 0
    # A接收的短信数
    received_mails_num = 0
    # 是否为垃圾短信发送者
    is_spam = False

    # 统计目标用户A的发送短信的接收者、发给A的发送者、接收者的短信数量、发送者的短信数量，总发送短信数量、总接收短信数量
    for item in items:
        if item[0] == target_id:
            sent_mails_num += 1
            sent_to.add(item[1])
            sent_to_count[item[1]] += 1
        elif item[1] == target_id:
            received_mails_num += 1
            received_from.add(item[0])
            received_from_count[item[0]] += 1

    sent_to.difference_update(received_from)
    # 计算A发送短信的接收者中，没有发送短信给A的人数
    L = len(sent_to)
    # 计算A发送短信数减去A接收的短信数
    M = sent_mails_num - received_mails_num

    # 判断是否为垃圾邮件
    if L > 5:
        is_spam = True
    elif M > 10:
        is_spam = True
    else:
        for receiver_id, sent_count in sent_to_count.items():
            if sent_count - received_from_count.get(receiver_id, 0) > 5:
                is_spam = True
                break

    return is_spam, L, M


if __name__ == '__main__':
    items = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
             [1, 7], [1, 8], [1, 9], [1, 10], [1, 11],
             [1, 12], [1, 13], [1, 14], [14, 1], [1, 15]]

    assert solve_method(15, items, 1) == (True, 13, 13)

    items = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
             [1, 7], [1, 8], [1, 9], [1, 10], [1, 11],
             [1, 12], [1, 13], [1, 14], [14, 1], [1, 15]]

    assert solve_method(15, items, 2) == (False, 0, -1)
