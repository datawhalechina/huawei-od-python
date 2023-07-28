# 109 斗地主（1）

## 题目描述

斗地主起源于湖北十堰房县，据传是一位叫吴修全的年轻人根据当地流行的扑克玩法“跑得快”改编的，如今已风靡整个中国，并流行于互联网上。

牌型：
- 单顺，又称顺子，最少5张牌，最多12张牌（3\~A），不能有2，也不能有大小王，不计花色。
例如：`3-4-5-7-8`、`7-8-9-10-J-Q`、`3-4-5-6-7-8-9-10-J-Q-K-A`。
可用的牌`3<4<5<6<7<8<9<10<J<Q<K<A<2<B(小王)<C(大王)`，每种牌除大小王外有4种花色（共有`13x4+2`张牌）。
  
## 输入描述

输入的第一行是当前手中的牌。

输入的第二行是已经出过的牌（包括对手出的和自己出的牌）

## 输出描述

对手可能构成的最长的顺子（如果有相同长度的顺子，输出牌面最大的那一个），如果无法构成顺子，则输出`NO-CHAIN`。

## 示例描述

### 示例一

**输入：**

```text
3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A
4-5-6-7-8-8-8
```

**输出：**

```text
9-10-J-Q-K-A
```

### 示例二

**输入：**

```text
3-3-3-3-8-8-8-8
K-K-K-K
```

**输出：**

```text
NO-CHAIN
```

## 解题思路

1. 创建一个`graph_num`字典，给牌按顺序标记 以便于后面找连续的牌。
2. 初始化一个`cards`字典，包含游戏开始每张牌的数目。
3. 删去自己的牌和已经打掉的牌，构建一个`rest_card`数组记录对手可能有的牌。
4. 遍历对手可能有的牌：
   - 初始化顺子列表`straight`。
   - 如果满足条件，将牌加入到顺子列表中。
   - 如果不满足条件，把当前5张以上的顺子列表加入到结果列表中。
5. 对最后一次遍历之后，判断顺子列表是否有5张以上，如果满足，加入到结果列表中。
6. 判断结果列表是否为空：
   - 如果不为空，按照顺子长度和起始牌面从大到小排序，返回最长且牌面最大的顺子。
   - 如果为空，返回`NO-CHAIN`。 

## 解题代码

```python
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
```