# 286 整理扑克牌

## 题目描述

给定一组数字，表示扑克牌的牌面数字，忽略扑克牌的花色，请按照如下规则对这一组扑克牌进行整理。
- 步骤一：对扑克牌进行分组，规则如下：
    1. 当牌面数字相同，张数大于等于4时，组合牌为”炸弹“；
    2. 三张相同牌面数字+两张相同牌面数字，且三张牌与两张牌不相同时，组合牌为”葫芦“；
    3. 三张相同牌面数字，组合牌为”三张“；
    4. 两张相同牌面数字，组合牌为”对子“；
    5. 剩余没有相同的牌，则为”单张“。
- 步骤二：对上述组合牌进行由大到小排列，规则如下：
    1. 不同类型组合牌之间由大到小排列规则：炸弹>葫芦>三张>对子>单张。
    2. 相同类型组合牌之间，除葫芦外，按组合牌全部牌面数组加和，由大到小排列。
    3. 葫芦则先按三张相同牌面数字加和，由大到小排列，三张相同牌面数字加和相同时，再按另外两张牌面数字加和，由大到小排列。
    4. 由于葫芦大于三张，因此如果能形成更大的组合牌，也可以将三张拆分成两张或一张，其中的两张可以和其他三张重新组合成葫芦，剩下的一张为单张。
- 步骤三：
    1. 当存在多个可能组合方案时，按如下规则排序取最大的一个组合牌。
    2. 一次对组合方案中的组合牌进行大小比较，规则同上。
    3. 当组合方案A中的第N个组合牌>组合方案B中的第N个组合牌时，即组合方案A大于组合方案B。

## 输入描述

第一行为N个正整数（按空格分隔），每个整数取值范围为[1,13]，N的取值范围为[1, 1000]。

## 输出描述

经重新排序后的扑克牌数字列表，每个数字以空格分隔

## 示例描述

### 示例一

**输入：**
```text
1 3 3 3 2 1 5
```

**输出：**
```text
3 3 3 1 1 5 2
```

### 示例二

**输入：**
```text
4 4 2 1 2 1 3 3 3 4
```

**输出：**
```text
4 4 4 3 3 2 2 1 1 3
```

## 解题思路

1. 将扑克牌按照频数降序、按照牌面降序排列，用`sorted_pokers`表示。
2. 遍历初步整理好的扑克牌：
  - 如果为3张牌：由于已经排好序，如果当前牌有3张，前一个大一点的牌也有3张，拆分当前牌为两张或一张，存入拆牌列表`split_pokers`中，并将当前扑克牌数量重新赋值为2张。
  - 如果为单张牌：与拆牌列表`split_pokers`循环比较单张牌，把大牌放入结果列表中。
  - 如果不是上述两种情况，则直接添加到整理好的结果列表中。
3. 将拆牌列表`split_pokers`中的扑克牌添加到结果列表队尾。

## 解题代码

```python
import collections


def solve_method(poker_arr):
    counter = collections.Counter(poker_arr)
    # 按照频数降序、按照牌面降序排列
    sorted_pokers = sorted(counter.items(), key=lambda x: (-x[1], -x[0]))

    result = []
    # 拆牌队列
    split_pokers = []
    for i, (card_num, card_count) in enumerate(sorted_pokers):
        # 由于已经排好序，如果当前牌有3张，前一个大一点的牌也有3张，拆分当前牌为两张或一张
        if i > 0 and sorted_pokers[i - 1][1] == 3 and card_count == 3:
            # 添加到拆牌队列中
            split_pokers.append(card_num)
            card_count = 2
            # 将当前位置，重新赋值为2张
            sorted_pokers[i] = (card_num, 2)
        elif card_count == 1 and split_pokers:
            # 循环比较单张牌
            for k, split_num in enumerate(split_pokers):
                if split_num > card_num:
                    result.append(split_num)
                    split_pokers.pop(k)
                    break

        # 添加到整理好的结果列表中
        result.extend([card_num] * card_count)

    # 如果拆牌队列中还有牌，直接加入到结果列表队尾
    if split_pokers:
        result.extend(split_pokers)

    return result


if __name__ == '__main__':
    assert solve_method([1, 3, 3, 3, 2, 1, 5]) == [3, 3, 3, 1, 1, 5, 2]
    assert solve_method([4, 4, 2, 1, 2, 1, 3, 3, 3, 4]) == [4, 4, 4, 3, 3, 2, 2, 1, 1, 3]
```