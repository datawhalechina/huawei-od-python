#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-26 16:13:15
# @Author  : catcooc 
# @Link    : https://github.com/catcooc
# @Desc    : 109 斗地主（1）

graph = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# 给牌按顺序标记 以便于后面找连续的牌
graph_num = {}
for i in range(len(graph)):
    graph_num[graph[i]] = i


def solve_method(my_cards, over_cards):
    cards = {}
    for card in graph:
        cards[card] = 4
    for card in (my_cards + "-" + over_cards).split("-"):
        if card in cards:
            cards[card] -= 1
            if cards[card] == 0:
                del cards[card]
    # 对手可能有的牌
    rest_cards = list(cards.keys())

    result = []
    pre_card = None
    straight = []
    for card in rest_cards:
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
        result.sort(key=lambda x: (len(x), x[0]), reverse=True)
        return "-".join(result[0])
    else:
        return "NO-CHAIN"


if __name__ == "__main__":
    my_cards, over_cards = "3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8-8"
    assert solve_method(my_cards, over_cards) == "9-10-J-Q-K-A"
    my_cards, over_cards = "3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8-8"
    assert solve_method(my_cards, over_cards) == "9-10-J-Q-K-A"
    my_cards, over_cards = "3-3-3-3-8-8-8-8", "K-K-K-K"
    assert solve_method(my_cards, over_cards) == "NO-CHAIN"
    my_cards, over_cards = "3-8", "K-K"
    assert solve_method(my_cards, over_cards) == "3-4-5-6-7-8-9-10-J-Q-K-A"
