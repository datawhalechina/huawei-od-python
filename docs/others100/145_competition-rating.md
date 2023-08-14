# 145 比赛评分

## 题目描述

一个有`N`个选手参加的比赛，选手编号为从1到`N`（3 <= N <= 100），有`M`（3 <= M <= 10）个评委对选手进行打分。

打分规则为每个评委对选手打分，最高分10分，最低分1分。

请计算得分最多的3位选手的编号。如果得分相同，则得分高分值最多的选手排名靠前（10分数量相同，则比较9分的数量，以此类推，用例中不会出现多个选手得分完全相同的情况）。

## 输入描述

第一行是`,`分隔的两个正整数，第一个数字表示`M`个评委，第二个数字表示`N`个选手。

第2到`M+1`行是`,`分隔的整数序列，表示评委为每个选手的打分，0号下标数字表示1号选手分数，1号下标数字表示2号选手分数，依次类推。

## 输出描述

选手前3名的编号。

注：若输入为异常，输出-1，如`M`、`N`、打分不在范围内。

## 示例描述

### 示例一

**输入：**

```text
4,5
10,6,9,7,6
9,10,6,7,5
8,10,6,5,10
9,10,9,4,9
```

**输出：**

```text
2,1,5
```

**说明：**  

第一行代表有4个评委，5个选手参加比赛，矩阵代表是4*5，每个数字是选手的编号，每一行代表一个评委对选手的打分排序。

2号选手得分36分排第1，1号选手36分排第2，5号选手30分（2号10分值有3个，1号10分值只有1个，所以2号排第一）

### 示例二

**输入：**

```text
2,5
7,3,5,4,2
8,5,4,4,3
```

**输出：**

```text
-1
```

**说明：**  

只有2个评委，要求最少3个评委。

### 示例三

**输入：**

```text
4,2
8,5
5,6
10,4
8,9
```

**输出：**

```text
-1
```

**说明：**  

要求最少3个选手参加

### 示例四

**输入：**

```text
4,5
11,6,9,7,8
9,10,6,7,8
8,10,6,9,7
9,10,8,6,7
```

**输出：**

```text
-1
```

**说明：**  

第一个评委给选手打11分，无效分数

## 解题思路

**基本思路：** 

1. 检查`M`、`N`、选手得分是否满足输入要求，如果不满足，则返回-1。
2. 遍历所有选手得分，构造选手类的列表
3. 使用自定义的比较方法进行排序，继承`Counter`类，根据选手的总分排序，如果总分相同，再依次从10开始比较得分次数。
4. 返回前三名的id。

## 解题代码

```python
from collections import Counter
from typing import List


class Player(Counter):
    def __lt__(self, other):
        self_total = 0
        for k, v in self.items():
            self_total += k * v
        other_total = 0
        for k, v in self.items():
            other_total += k * v

        if self_total != other_total:
            return self_total > other_total
        else:
            for i in range(10, 0, -1):
                return self.get(i, 0) > other.get(i, 0)

        return False


def solve_method(M: int, N: int, ratings: List[List[int]]):
    """
    :param M: 评委个数
    :param N: 选手个数
    :param ratings: 选手得分
    :return:
    """
    # 检查输入参数是否满足要求(M,N,评分)
    if not (3 <= M <= 10) or not (3 <= N <= 100):
        return -1
    for row in ratings:
        if not all(1 <= num <= 10 for num in row):
            return -1

    players = []
    for i in range(N):
        scores = []
        for j in range(M):
            score = ratings[j][i]
            scores.append(score)
        # 构造选手类
        players.append([i + 1, Player(scores)])

    # 使用自定义的比较方法进行排序
    players.sort(key=lambda x: x[1])

    # 取出前3名选手
    return [x[0] for x in players[:3]]


if __name__ == '__main__':
    arr = [
        [10, 6, 9, 7, 6],
        [9, 10, 6, 7, 5],
        [8, 10, 6, 5, 10],
        [9, 10, 9, 4, 9],
    ]
    assert solve_method(4, 5, arr) == [2, 1, 5]

    arr = [
        [7, 3, 5, 4, 2],
        [8, 5, 4, 4, 3],
    ]
    assert solve_method(2, 5, arr) == -1

    arr = [
        [8, 5],
        [5, 6],
        [10, 4],
        [8, 9],
    ]
    assert solve_method(4, 2, arr) == -1

    arr = [
        [11, 6, 9, 7, 8],
        [9, 10, 6, 7, 8],
        [8, 10, 6, 9, 7],
        [9, 10, 8, 6, 7],
    ]
    assert solve_method(4, 5, arr) == -1
```