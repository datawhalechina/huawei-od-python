# 019 找出通过车辆最多的颜色

## 题目描述

在一个狭小的入口，每秒只能通过一辆车，假如车辆的颜色只有3种，找出`N`秒内经过的最多颜色的车辆数量，三种颜色编号为0、1、2。

## 输入描述

第一行输入的是通过的车辆颜色信息，[0,1,1,2]代表4秒钟通过的车辆颜色分别是0、1、1、2。

第二行输入的是统计事件窗，数据类型为整型，单位为秒。

## 输出描述

输出指定时间窗内经过的最多颜色的车辆数量

## 示例描述

### 示例一

**输入：**
```text
0 1 2 1
3
```

**输出：**
```text
2
```

**说明：**  
在[1,2,1]这个3秒时间窗，1这个颜色出现2次，数量最多。

### 示例二

**输入：**
```text
0 1 2 1
2
```

**输出：**
```text
1
```

**说明：**  
在2秒时间窗内，每个颜色最多出现1次。

## 解题思路

1. 本题需要使用`Counter`构建哈希表，解决频数问题。
2. 读取窗口中的数据，使用`Counter`类构建哈希表。
3. 使用`most_common`方法，得到最多的频数（即最多颜色的次数）。
4. 返回最多颜色的次数。

## 解题代码

```python
import collections


def solve_method(cars: list, time_windows: int):
    max_color = 0
    for i, car in enumerate(cars):
        # 读取窗口中的数据
        if i + 1 >= time_windows:
            count_cars = cars[i + 1 - time_windows: i + 1]
        else:
            count_cars = cars[:i + 1]
        # 使用Counter类构建哈希表
        counter = collections.Counter(count_cars)
        # 得到最多的频数
        max_color = max(max_color, counter.most_common(1)[0][1])

    return max_color


if __name__ == '__main__':
    assert solve_method([0, 1, 2, 1], 3) == 2
    assert solve_method([0, 1, 2, 1], 2) == 1
```