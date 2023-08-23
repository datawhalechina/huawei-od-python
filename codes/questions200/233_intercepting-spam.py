#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 233_intercepting-spam.py
@time: 2023/8/17
@project: huawei-od-python
@desc: 233 垃圾信息拦截 
"""

def solve_method(itemNum, items, target_id):
    sent_to = set()
    received_from = set()
    sent_to_count = dict()
    received_from_count = dict()
    sent_mails_num = 0
    received_mails_num = 0
    is_spam = False

    # 统计目标用户 发邮件的信息 和 收邮件的信息 （共多少次， 谁，分别多少次）
    for item in items:
        if item[0] == target_id:
            sent_mails_num += 1
            sent_to.add(item[1])
            sent_to_count[item[1]] = sent_to_count.get(item[1], 0) + 1
        elif item[1] == target_id:
            received_mails_num += 1
            received_from.add(item[0])
            received_from_count[item[0]] = received_from_count.get(item[0], 0) + 1

    # 计算 L 和 M 值
    sent_to.difference_update(received_from)
    L = len(sent_to)
    M = sent_mails_num - received_mails_num

    # 判断是否为垃圾邮件
    if L > 5:
        is_spam = True
    elif M > 10:
        is_spam = True
    else:
        for receiver_id, sent_count in sent_to_count.items():
            if receiver_id in received_from_count:
                if sent_count - received_from_count[receiver_id] > 5:
                    is_spam = True
                    break

    return (is_spam, L, M)


if __name__ == '__main__':
    items = [[1,2], [1, 3], [1, 4], [1, 5], [1, 6], 
             [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], 
             [1, 12], [1, 13], [1, 14], [14, 1], [1, 15]]
    
    assert solve_method(15, items, 1) == (True, 13, 13)

    items = [[1,2], [1, 3], [1, 4], [1, 5], [1, 6], 
             [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], 
             [1, 12], [1, 13], [1, 14], [14, 1], [1, 15]]
    
    assert solve_method(15, items, 2) == (False, 0, -1)