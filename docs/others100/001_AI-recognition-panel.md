# 001 AI识别面板

## 题目描述

AI识别到面板上有N（1 <= N <= 100）个指示灯，灯大小一样，任意两个之间无重叠。由于AI识别误差，每次识别到的指示灯位置可能有差异，以4个坐标值描述AI识别的指示灯的大小和位置（左上角x1、y1，右下角x2、y2），请输出先行后列排序的指示灯的编号。

**排序规则：**

1. 每次在尚未排序的灯中挑选最高的灯作为基准灯。
2. 找出和基准灯属于同一行所有的灯进行排序。两个灯高低偏差不超过灯半径算同一行（即两个灯坐标的差小于灯高度的一半）。

## 输入描述

第一行为`N`，表示灯的个数。接下来`N`行，每行为1个灯的坐标信息，格式为：
```
编号x1 y1 x2 y2
```
1. 编号全局唯一
2. 1 < 编号 <= 100
3. 0 <= x1 < X2 <= 1000
4. 0 <= y1 < y2 <= 1000

## 输出描述

排序后的编号列表，编号之间以空格分隔。

## 示例描述

### 示例一

**输入：**

```text
5
1 0 0 2 2
2 6 1 8 3
3 3 2 5 4
5 5 4 7 6
4 0 4 2 6
```

**输出：**

```text
1 2 3 4 5
```

## 解题思路

1. 构建新的灯列表，记录灯的id、x坐标的平均值、y坐标的平均值、灯高半径，记为`lights_list`。
2. 通过y坐标的平均值，将灯按行粗排。
3. 设置每一行的起始索引`row_start_index`，遍历所有的灯，判断灯的高低偏差超过灯高度的一半：
    - 如果超过了灯高度的一半，把之前的灯按x坐标排序，并存入结果列表中，更新起始索引`row_start_index`，表示新的一行。
    - 如果没有超过，则继续遍历。
4. 把该行剩余的灯全部加入到结果列表中。
5. 返回结果列表。

## 解题代码

```python
def solve_method(lights):
    lights_list = []
    for light in lights:
        id = light[0]
        x1 = light[1]
        y1 = light[2]
        x2 = light[3]
        y2 = light[4]
        # id, x坐标的平均值, y坐标的平均值, 灯高半径
        lights_list.append([id, (x1 + x2) // 2, (y1 + y2) // 2, (y2 - y1) // 2])

    # 将灯按行粗排
    lights_list.sort(key=lambda x: x[2])

    result = []

    # 设置每一行的起始索引
    row_start_index = 0
    # 先使用第1行第1个作为基准灯
    for i in range(1, len(lights_list)):
        # 高低偏差超过灯高度的一半
        if lights_list[i][2] - lights_list[row_start_index][2] > lights_list[row_start_index][3]:
            # 把之前的灯按x坐标排序，并存入结果列表中
            lights_list[row_start_index:i] = sorted(lights_list[row_start_index:i], key=lambda x: x[1])
            result.extend([light[0] for light in lights_list[row_start_index:i]])
            # 记录新一行对应的灯位置
            row_start_index = i

    # 把该行剩余的灯全部加入到结果列表中
    lights_list[row_start_index:] = sorted(lights_list[row_start_index:], key=lambda x: x[1])
    result.extend([light[0] for light in lights_list[row_start_index:]])

    return result
```

