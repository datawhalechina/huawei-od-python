#  110 斗地主（2）、斗地主之顺子

## 题目描述

在斗地主扑克牌游戏中，扑克牌由小到大的顺序为`3 4 5 6 7 8 9 10 J Q K A 2`，玩家可以出的扑克牌阵型有：单张、对子、顺子、飞机、炸弹等。其中顺子的出牌规则是由至少5张由小到大连续递增的扑克牌组成且不能包含2。

例如: `{3,4,5,6,7}`、`{3,4,5,6,7,8,9,10,J,Q,K,A}`都是有效的顺子，而`{J,Q,K,A,2}`、`{2,3,4,5,6}`、`{3,4,5,6}`、`{3,4,5,6,8}`等都不是顺子。

给定一个包含13张牌的数组，如果有满足出牌规则的顺子，请输出顺子。如果存在多个顺子，请每行输出一个顺子，且需要按照顺子的第一张牌的大小（必须从小到大）依次输出。如果没有满足出牌规则的顺子，请输出`No`。

## 输入描述

13张任意顺序的扑克牌，每张扑克牌数字用空格隔开，每张扑克牌的数字都是合法的，并且不包括大小王。

例如：`2 9 J 3 4 K A 7 9 A 5 6`

不需要考虑输入为异常字符的情况。

## 输出描述

输出组成的顺子，每张扑克牌数字用空格隔开。

例如：`3 4 5 6 7`

## 示例描述

### 示例一

**输入：**

```text
2 9 J 2 3 4 K A 7 9 A 5 6
```

**输出：**

```text
3 4 5 6 7
```

**说明：**  

13张牌中可以组成的顺子只有一组：`3 4 5 6 7`。

### 示例二

**输入：**

```text
2 9 J 10 3 4 K A 7 Q A 5 6
```

**输出：**

```text
3 4 5 6 7
9 10 J Q K A
```

**说明：**  

13张牌中可以组成两组顺子，从小到大分别为：`3 4 5 6 7`、`9 10 J Q K A`。

### 示例三

**输入：**

```text
2 9 9 9 3 4 K A 10 Q A 5 6
```

**输出：**

```text
No
```

**说明：**  

13张牌中无法组成顺子。

## 解题思路

1. 创建一个`graph_num`字典，给牌按顺序标记 以便于后面找连续的牌。
2. 将牌面转成序号，过滤掉2，再重新排序，将序号转换成牌面。
3. 遍历手上所有的牌：
   - 初始化顺子列表`straight`。
   - 如果满足条件，将牌加入到顺子列表中。
   - 如果不满足条件，把当前5张以上的顺子列表加入到结果列表中。
4. 对最后一次遍历之后，判断顺子列表是否有5张以上，如果满足，加入到结果列表中。
5. 判断结果列表是否为空：
   - 如果不为空，按照顺子的第一张牌从小到大进行排序，返回结果。
   - 如果为空，返回`No`。 

## 解题代码

```python
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
```

