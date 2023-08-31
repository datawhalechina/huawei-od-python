# 041 统一限载货物数最小值

## 题目描述

火车站附近的货物中转站负责将到站货物运往仓库，小明在中转站负责调度`2K`辆中转车（`K`辆干货中转车，`K`辆湿货中转车）。货物由不同供货商从各地发来，各地的货物是依次进站，然后小明按照卸货顺序依次装货到中转车上，一个供货商的货只能装到一辆车上，不能拆装，但是一辆车可以装多家供货商的货；中转车的限载货物量由小明统一制定，在完成货物中转的前提下，请问中转车的统一限载货物数最小值为多少。

## 输入描述

第一行输入`length`，表示供货商数量，取值范围是1 <= length <= 10^4。

第二行输入`goods`，表示供货数数组，取值范围是1 <= goods[i] <= 10^4。

第三行输入`types`，表示对应货物类型，`types[i]`等于0或者1，0代表干货，1代表湿货。

第四行输入`k`，表示单类中转车数量，取值范围是1 <= k <= goods.length。

## 输出描述

输出一个整数，表示中转车统一限载货物数。其中，中转车最多跑一趟仓库。

## 示例描述

### 示例一

**输入：**
```text
4
3 2 6 3
0 1 1 0
2
```

**输出：**
```text
6
```

**说明：**

- 货物1和货物4为干货，由2辆干货中转车中转，每辆车运输一个货物，限载为3。
- 货物2和货物3为湿货，由2辆湿货中转车中转，每辆车运输一个货物，限载为6。

这样中转车统一限载货物数可以设置为6（干货车和湿货车限载最大值），是最小的取值。

### 示例二

**输入：**
```text
4
3 2 6 8
0 1 1 1
1
```

**输出：**
```text
16
```

**说明：**

- 货物1为干货，由1辆干货中转车中转，限载为3。
- 货物2、货物3和货物4为湿货，由1辆湿货中转车中转，限载为16。

这样中转车统一限载货物数可以设置为16（干货车和湿货车限载最大值），是最小的取值。

## 解题思路

**基本思路：**

> **说明**： 题中"小明按照卸货顺序依次装货到中转车上"，但是没有说明**顺序依次**的含义（可能的含义如下），且示例解释没有考虑卸货顺序，所以以下解法不考虑卸货顺序。若考虑卸货顺序，`check`函数按贪心算法更改即可
> - 中转站只允许同时存在一辆车（即，如果货物1为湿货，货物2为干货，则放置货物2时湿货车必须先开走）
> - 中转站只允许存在最多一辆湿货车和一辆干货车
> - 中转站运行同时存在所有的车（即，此时顺序依次不起作用）

假设`2k`辆车能完成所有中转的最小限载货物数为`x`，那么以`x`为分割点的数轴具有二段性：
- 最小限载货物数小于`x`时，必然不可能通过`2k`辆车完成所有中转。
- 最小限载货物数大于等于`x`时，必然能通过`2k`辆车完成所有中转。

所以可采用二分算法：
- 限载货物数的最小值：考虑到一个供货商的货只能装到一辆车上，不能拆装，所以为`goods`数组的最大值。
- 限载货物数的最大值：`goods`数组货物量之和。
- 判决条件：递归和回溯所有可能

**代码思路：**
1. 将货物分为湿货和干货，分别存入两个数组`drys`和`wets`中。
2. 分别获取湿货数组和干货数组的限载货物数最小值（使用二分算法和深度优先搜索）
    - check函数的终止条件：所有货物都装完了。
    - check函数的递归处理：遍历所有的货物车，判断是否满足条件。
3. 将干湿货车的限载货物数进行比较，返回最大值，即为结果。

## 解题代码
```python
def solve_method(length, goods, types, k):
    drys, wets = [], []
    for i in range(length):
        if types[i] == 0:
            drys.append(goods[i])
        else:
            wets.append(goods[i])
    min_weight_drys = get_min_weight(drys, k)
    min_weight_wets = get_min_weight(wets, k)
    return max(min_weight_drys, min_weight_wets)


def get_min_weight(goods, k):
    min_weight = max(goods)
    max_weight = sum(goods)
    while min_weight < max_weight:
        mid = (min_weight + max_weight) // 2
        if check(goods, mid, [0] * k, 0):
            max_weight = mid
        else:
            min_weight = mid + 1
    return min_weight


def check(goods, weight, vans, index):
    # 判断所有货物是否都装完了
    if index == len(goods):
        return True
    for i in range(len(vans)):
        if vans[i] + goods[index] <= weight:
            vans[i] += goods[index]
            if check(goods, weight, vans, index + 1):
                return True
            vans[i] -= goods[index]
    return False


if __name__ == "__main__":
    # 4
    # 3 2 6 3
    # 0 1 1 0
    # 2
    # length = int(input().strip())
    # goods = list(map(int, input().strip().split()))
    # types = list(map(int, input().strip().split()))
    # k = int(input().strip())
    # print(solve_method(length, goods, types, k))

    assert solve_method(4, [3, 2, 6, 3], [0, 1, 1, 0], 2) == 6
    assert solve_method(4, [3, 2, 6, 8], [0, 1, 1, 1], 1) == 16
```