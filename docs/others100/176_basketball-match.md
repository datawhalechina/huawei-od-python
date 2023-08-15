# 176 篮球比赛

## 题目描述

篮球(5v5)比赛中每个球员拥有一个战斗力，每个队伍的所有球员战斗力之和为该队伍的总体战斗力。现有十个球员准备分为两队进行训练赛，教练希望两个队伍的战斗力差能够尽可能的小，以达到最佳训练效果。

给出十个球员的战斗力，如果你是教练，你该如何分队，才能达到最佳训练效果?请输出该分队方案下的最小战斗力差值。



## 输入描述

十个篮球队员的战斗力(整数，范围`[1，10000]`)

战斗力之间用空格分隔，如: `10 9 8 7 6 5 4 3 2 1`

不需要考虑异常输入的场景

## 输出描述

最小战斗力差值，如:1



## 示例描述

### 示例一

**输入：**

```text
10 9 8 7 6 5 4 3 2 1
```



**输出：**

```text
1
```



**说明：**

`1 2 5 9 10` 分为一队，`3 4 6 7 8`分为一队，两队战斗力之差最小，输出差值`1`。



**备注：**

球员分队方案不唯一，但最小战斗力差值固定是1



## 解题思路

**基本思路：**

将该题使用贪心的思想（注意题目中明说分成5v5的队伍），先将运动员从大到小排序，哪个队伍能力值总和小进入哪个队伍。

当某个队伍满了五个人时，剩下的人只能都进入另一个队伍。

## 解题代码

```python
def solve_method(s):
    players = list(map(int, s.split()))
    total = sum(players)
    half = total // 2
    # 从大到小排序
    players.sort(reverse=True)
    team_a = []
    team_b = []
    # 从大遍历所有运动员，哪个队伍能力值总和小进入哪个队伍
    # 当某个队伍满了五个人时，剩下的人只能进入另一个队伍
    for player in players:
        # 所有队伍未满五人时
        if len(team_a)!=5 and len(team_b)!=5:
            if sum(team_a) <= sum(team_b):
                team_a.append(player)
            else:
                team_b.append(player)
        # 某个队伍满了五人时
        else:
            # a队伍满了，则进入b队伍
            if len(team_a)==5:
                team_b.append(player)
            # b队伍满了，则进入a队伍
            else:
                team_a.append(player)
    print(team_a, team_b)
    return abs(sum(team_a) - sum(team_b))


if __name__ == '__main__':
    assert solve_method("1 2 3 4 5 6 7 8 9 10") == 1
    assert solve_method("1 2 3 4 5 6 7 8 999 10") == 973
    assert solve_method("1 2 3 4 5 6 7 8 999 1000") == 1

```



