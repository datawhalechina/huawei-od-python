# 144 比赛的冠亚军

## 题目描述

有`N`（3 <= N < 10000）个运动员，他们的id为0到`N-1`，他们的实力由一组整数表示。他们之间进行比赛，需要决出冠亚军。比赛的规则是0号和1号比赛、2号和3号比赛，以此类推，每一轮，相邻的运动员进行比赛，获胜的进入下一轮，实力值大的获胜，实力值相等的情况，id小的情况下获胜，轮空的直接进入下一轮。

默认季军为输给冠军的选手，如果半决赛不足四人，冠军直接战胜亚军，那么季军为输给亚军的选手。

## 输入描述

输入一行`N`个数字代表`N`的运动员的实力值（0 <= 实力值 <= 10000000000）。

## 输出描述

输出冠、亚、季的id，用空格隔开。

## 示例描述

### 示例一

**输入：**

```text
2 3 4 5
```

**输出：**

```text
3 1 2
```

**说明：**  

第一轮比赛，id为0实力值为2的运动员和id为1 实力值为3的运动员比赛，1号胜出进入下一轮争夺冠亚军；id为2的运动员和id为3的运动员比赛，3号胜出进入下一轮争夺冠亚军；

冠亚军比赛，3号胜1号；2号运动员是在冠亚军之前输给冠军3号的，所以季军是2号。

冠、亚、季军id分别为3、1、2。

## 解题思路

1. 计算需要比赛的轮次：
$$
epoch=\lceil log_2(players) \rceil=\lfloor log_2(players-1) \rfloor +1
$$  
2. 遍历每一轮：
    - 如果还需比赛的选手不足 4人(半决赛)，为了便于输出季军，保存此时他们的对阵情况。
    - 遍历所有的参赛选手：运动员`rank[i]`需要和身边的运动员`rank[i+1]`比拼；如果`rank[i]`身旁没人（也就是轮空），则直接算作这一轮的胜利者。
    - 记录每一轮的胜利者`win`。    
3. 循环终止时，`rank`里只包含冠军的id，`lose`的倒数第一位是亚军。
4. 返回结果，即冠亚季军的编号。

## 解题代码

```python
import math
from typing import List


def solve_method(strengh: List[int]):
    nums = len(strengh)
    rank = list(range(0, nums))  # 初始顺序, 代表还要比赛的选手
    win = []  # 每一轮的胜者
    lose = []  # 和已经产生的失败者
    semi_final = {}  # 半决赛 对阵情况(便于输出季军)
    # 需要比较的轮次：n= log2(nums)的向上取整=log2(nums-1)向下取整+1
    n = int(math.log2(nums - 1)) + 1

    # 模拟法；模拟运动员两两比赛的过程，需要比赛n轮
    for epoch in range(0, n):
        # 如果还需比赛的选手不足 4人(半决赛)，为了便于输出季军，保存此时他们的对阵情况
        if 3 <= len(rank) <= 4:
            semi_final = {rank[0]: rank[1], rank[1]: rank[0]}
            if len(rank) == 4:
                semi_final.update({rank[2]: rank[3], rank[3]: rank[2]})

        # while 循环模拟每一轮比赛
        win.clear()
        i = 0
        while i < len(rank):
            player_id = rank[i]

            # 轮空的直接进入下一轮
            if i == len(rank) - 1:
                win.append(player_id)
                i += 1

            # 和相邻的比较
            else:
                neighbor_player = rank[i + 1]
                if strengh[player_id] >= strengh[neighbor_player]:
                    win.append(player_id)
                    lose.append(neighbor_player)
                else:
                    win.append(neighbor_player)
                    lose.append(player_id)
                # 同时处理了2个运动员;
                i += 2

        # 本轮胜出的选手参加下一轮比赛
        rank = win[:]

    # 循环终止时，rank里只包含冠军的id，lose的倒数第一位是亚军
    # 季军可以用之前的 semi_final 字典找到
    champion = rank[0]
    second_player = lose[-1]
    third_player = semi_final.get(champion, semi_final.get(second_player))
    ret = [champion, second_player, third_player]
    return ret


if __name__ == '__main__':
    assert solve_method([2, 3, 4, 5]) == [3, 1, 2]
    assert solve_method([7, 6, 5, 4, 3, 2, 1, 0]) == [0, 4, 2]
```