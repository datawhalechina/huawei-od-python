# 016 人数最多的站点

## 题目描述

公园园区提供小火车单向通行，从园区站点编号最小到最大，通行如1 -> 2 -> 3 -> 4 -> 1，并供员工在各个办公园区穿梭。

通过对公司`N`个员工调研，统计到每个员工的坐车区间，包含前后站点，请设计一个程序计算出小火车在哪个园区站点时人数最多。

## 输入描述

第1行是调研员工人数。

第2行开始是每个员工的开始上车站点和下车站点。

使用数字代替每个园区，用空格分隔，如`3 5`表示从第3个园区上车，在第5个园区下车。

## 输出描述

人数最多时的园区站点编号，最多人数相同时，返回编号最小的园区站点。

## 示例描述

### 示例一

**输入：**
```text
3
1 3
2 4
1 4
```

**输出：**
```text
2
```

**说明：**  
第1行，3代表调研员工总人数为3。

- 小火车在第1个园区时，车上有2个人。
- 到第2个园区时，有3个人。
- 到第3个园区，是3个人。
- 到第4个园区，是2个人。

返回数字最小的园区，所以输出2。

## 解题思路

1. 初始化站点人数字典`station_people`，`key`为站点号，`value`为人数。
2. 遍历每个员工的坐车区间：统计每个站点的小火车上的人数。
3. 对字典`station_people`按照人数来排序。
4. 返回字典中排在第一个元素的站点号。

## 解题代码

```python
from collections import defaultdict


def solve_method(people):
    station_people = defaultdict(int)
    for p in people:
        for station in range(p[0], p[1] + 1):
            station_people[station] += 1

    result = sorted(station_people.items(), key=lambda x: -x[1])
    return result[0][0]


if __name__ == '__main__':
    people = [(1, 3), (2, 4), (1, 4)]
    assert solve_method(people) == 2
```

