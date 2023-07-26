# 017 人气最高的店铺

## 题目描述

某购物城有`m`个商铺，现决定举办一场活动选出人气最高店铺。活动共有`n`位市民参与，每位市民只能投一票，但1号店铺如果给该市民发放`q`元的购物补贴，该市民会改为投1号店铺。

请计算1号店铺需要最少发放多少元购物补贴才能成为人气最高店铺（即获得的票数要大于其他店铺），如果1号店铺本身就是票数最高店铺，返回0。

## 输入描述

第1行是`,`分隔的两个整数`n`、`m`，其中第一个整数`n`表示参与的市民总数，第二个整数`m`代表店铺总数，取值范围是1 <= n,m <= 3000。

第2到`n+1`行，每行是`,`分隔的两个整数`p`、`q`，表示市民的意向投票情况，其中每行的第一个整数`p`表示该市民意向投票给`p`号店铺，第二个整数`q`表示其改投1号店铺所需给予的`q`元购物补贴，取值范围是1 <= p <= m、1 <= q <= 10^9。

不考虑输入的格式问题。

## 输出描述

1号店铺需要最少发放购物补贴金额。

## 示例描述

### 示例一

**输入：**
```text
5,5
2,10
3,20
4,30
5,40
5,90
```

**输出：**
```text
50
```

**说明：**  
有5个人参与，共5个店铺。

- 如果选择发放10元+20元+30元=60元的补贴来抢2、3、4号店铺的票，总共发放了60元补贴（5号店铺有2票，1号店铺要3票才能胜出）。
- 如果选择发放10元+40元=50元的补贴来抢2、5号店铺的票，总共发放了50元补贴（抢了5号店铺的票后，现在1号店铺只要2票就能胜出）。

所以最少发放50元补贴。

### 示例二

**输入：**
```text
5,5
2,10
3,20
4,30
5,80
5,90
```

**输出：**
```text
60
```

**说明：**  
有5个人参与，共5个店铺。

- 如果选择发放10元+20元+30元=60元的补贴来抢2、3、4号店铺的票，总共发放了60元补贴（5号店铺有2票，1号店铺要3票才能胜出）。
- 如果选择发放10元+80元=90元的补贴来抢2、5号店铺的票，总共发放了90元补贴（抢了5号店铺的票后，现在1号店铺只要2票就能胜出）。

所以最少发放60元补贴。

## 解题思路

**基本思路：** 本题采用回溯法思想解题。
1. 初始化店铺票数字典`shop_ticket`，`key`为店铺号，`value`为店铺所得票数。
2. 使用回溯法：
    - 确定参数：每个店铺的补贴`tickets`、可用于发放的补贴方式`change_list`、遍历索引`index`。
    - 终止条件：检查1号店铺是否得票最多，如果是则获取最少的发放购物补贴金额，并返回。
    - 回溯：
       - 将该店铺添加到补贴方式中。
       - 遍历索引`index`加1，继续回溯。
       - 在补贴方式中，删除该店铺。
3. 检查1号店铺是否得票最多`check_shop1_max_ticket`：
    - 遍历补贴方式：1号店铺加票，其他店铺减票，并累加发放购物补贴金额。
    - 获取当前得票最多的店铺号。
    - 检查是否为1号店铺，或者1号店铺是否为得票最多的店铺
        - 如果是1号店铺，返回`True`。
        - 如果不是1号店铺，返回`False`。
4. 返回结果，即最少的发放购物补贴金额。

## 解题代码

```python
import math
from collections import defaultdict


def check_shop1_max_ticket(change_list):
    global money, shop_ticket
    temp_map = shop_ticket.copy()
    money = 0
    # 1号店铺加票，其他店铺减票，并累加发放购物补贴金额
    for shop_id, shop_money in change_list:
        money += shop_money
        temp_map[shop_id] -= 1
        temp_map[1] += 1

    sorted_shop = sorted(temp_map.items(), key=lambda x: -x[1])

    # 获取当前得票最多的店铺ID
    first_shop_id = sorted_shop[0][0]
    # 检查是否为1号店铺，或者1号店铺是否为得票最多的店铺
    if first_shop_id == 1 and (len(sorted_shop) == 1 or sorted_shop[0][1] > sorted_shop[1][1]):
        return True
    return False


def backstracking(tickets, change_list, index):
    global min_money, money
    # 如果是1号店铺得票最多，则获取最少的发放购物补贴金额
    if check_shop1_max_ticket(change_list) and min_money > money:
        min_money = money
        return

    for i in range(index, len(tickets)):
        change_list.append(tickets[i])
        backstracking(tickets, change_list, i + 1)
        change_list.pop()


def solve_method(tickets):
    global shop_ticket, min_money
    # 最少发放购物补贴金额
    min_money = math.inf
    # 店铺票数字典，key为店铺号，value为店铺所得票数
    shop_ticket = defaultdict(int)
    shop_ticket[1] = 0
    for ticket in tickets:
        shop_id = ticket[0]
        shop_ticket[shop_id] += 1

    # 使用回溯法
    backstracking(tickets, [], 0)

    return min_money


if __name__ == '__main__':
    tickets = [[2, 10], [3, 20], [4, 30], [5, 40], [5, 90]]
    assert solve_method(tickets) == 50

    tickets = [[2, 10], [3, 20], [4, 30], [5, 80], [5, 90]]
    assert solve_method(tickets) == 60
```

