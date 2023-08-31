# 015 垃圾信息拦截

## 题目描述

大众对垃圾短信深恶痛绝，希望影对垃圾短信发送者进行识别，为此，很多软件增加了垃圾短信识别机制。经分析，发现正常用户的短信通常具备交互性，而垃圾短信往往都是大量单向的短信，按照如下规则进行垃圾短信识别:

本题中，发送者`A`符合以下条件之一的，则认为`A`是垃圾短信发送者：
- `A`发短信的接收者中，没有发过短信给`A`的人数`L`大于5。
- `A`发送的短信数减去`A`接收的短信数`M`大于10。
- 如果存在`X`，`A`发送给`X`的短信数减去`A`接收到`X`的短信数`N`大于5。

## 输入描述

第一行是条目数目。

接下来几行是具体的条目，每个条目，是一对`ID`，第一个数字是发送者`ID`，后面的数字是接收者`ID`，中间空格隔开。所有的`ID`都为无符号整型，`ID`最大值为100。同一个条目中，两个`ID`不会相同（即不会自己给自己发消息）。

最后一行是指定的`ID`。

## 输出描述

输出该`ID`是否为垃圾短信发送者，并且按序列输出`L M`的值（由于`N`值不唯一，不需要输出）。输出均为字符串。

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

1. 遍历所有短信接发人员：统计目标用户`A`的发送短信的接收者`sent_to`、发给`A`的发送者`received_from`、接收者的短信数量`sent_to_count`、发送者的短信数量`received_from_count`，总发送短信数量`sent_mails_num`、总接收短信数量`received_mails_num`。
2. 计算`A`发送短信的接收者中，没有发送短信给`A`的人数`L`。
3. 计算`A`发送短信数减去`A`接收的短信数`M`。
4. 判断是否为垃圾邮件，并设置垃圾短信发送者标识`is_spam`：
    - 当`L`大于5，则设置为`True`，是垃圾短信发送者。
    - 当`M`大于10，则设置为`True`，是垃圾短信发送者。
    - 当`A`对单人发送的短信数减去接收的短信数大于5，则设置为`True`，是垃圾短信发送者。
5. 返回结果，即垃圾短信发送者标识`is_spam`、`L`和`M`。    

## 解题代码

```python
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
```