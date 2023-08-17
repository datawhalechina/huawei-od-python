# 233 垃圾信息拦截

## 题目描述
大众对垃圾短信深恶痛绝，希望影对垃圾短信发送者进行识别，为此，很多软件增加了垃圾短信识别机制。经分析，发现正常用户的短信通常具备交互性，而垃圾短信往往都是大量单向的短信，按照如下规则进行垃圾短信识别:
本题中，发送者 `A` 符合以下条件之一的，则认为 `A` 是垃圾短信发送者:
- `A` 发短信的接收者中，没有发过短信给 `A` 的人数 `L > 5`
- `A` 发送的短信数 - `A` 接收的短信数 `M > 10`:
- 如果存在 `X`，`A` 发送给 `X` 的短信数 - `A` 接收到 `X` 的短信数 `N > 5`;

## 输入描述
第一行为条目数目，接下来几行是具体的条目;

每个条目，是一对 `ID`，第一个数字是发送者 ID，后面的数字是接收者 ID，中间空格隔开;

所有的 `ID` 都为无符号整型，`ID` 最大值为 `100`;

同一个条目中，两个 `ID` 不会相同 (即不会自己给自己发消息)

最后一行为指定的`ID`

## 输出描述
输出该 `ID` 是否为垃圾短信发送者，并且按序列输出 `L M` 的值 (由于 `N` 值不唯一，不需要输出);

输出均为字符串。

## 示例描述

### 示例一

**输入：**
```
15
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
1 11
1 12
1 13
1 14
14 1
1 15
1
```

**输出：**
```
true 13 13
```

### 示例二

**输入：**
```
15
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
1 11
1 12
1 13
1 14
14 1
1 15
2
```

**输出：**
```
false 0 -1
```

## 解题思路

**简单提示**
使用集合和字典，记录目标用户发邮件的信息和收邮件的信息，即 共多少次、另一个ID是哪些、分别多少次；

然后根据题目要求，计算 `L` 和 `M`，并判断是否为垃圾邮件。

## 解题代码
``` python
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
```