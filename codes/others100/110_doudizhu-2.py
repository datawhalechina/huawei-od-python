#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-26 22:50:13
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Desc    : 110 斗地主（2）

graph = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# 给牌按顺序标记 以便于后面找连续的牌
graph_num = {}
for i in range(len(graph)):
    graph_num[graph[i]] = i


def solve_method(line):
    cards = line.split(" ")
    # 将牌面转成序号
    card_num = []
    for card in cards:
        if card in graph_num:
            card_num.append(graph_num[card])
    # 排序之后，再将序号转成牌面
    card_num.sort()
    cards = [graph[x] for x in card_num]

    result = []
    pre_card = None
    straight = []
    for card in cards:
        # 初始化顺子列表
        if not straight:
            pre_card = card
            straight.append(card)

        if graph_num[card] - graph_num[pre_card] == 1:
            # 满足条件，将牌加入到顺子列表中
            pre_card = card
            straight.append(card)
        elif graph_num[card] - graph_num[pre_card] > 1:
            # 如果不满足条件，把当前5张以上的顺子列表加入到结果列表中
            pre_card = card
            if len(straight) >= 5:
                result.append(straight)
            straight = [card]

    # 最后一次判断顺子列表是否有5张以上
    if len(straight) >= 5:
        result.append(straight)

    if result:
        result.sort(key=lambda x: x[0])
        return [" ".join(x) for x in result]
    else:
        return "No"


if __name__ == "__main__":
    assert solve_method("2 9 J 10 3 4 K A 7 Q A 5 6") == ["3 4 5 6 7", "9 10 J Q K A"]
    assert solve_method("2 9 J 2 3 4 K A 7 9 A 5 6") == ["3 4 5 6 7"]
    assert solve_method("2 9 9 9 3 4 K A 10 Q A 5 6") == "No"
