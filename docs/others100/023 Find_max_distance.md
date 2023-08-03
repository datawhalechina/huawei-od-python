# 023 停车场最大的距离

## 题目描述

停车场有一横排车位`0`代表没有停车,`1`代表有车
至少停了一辆车在车位上,也至少有一个空位没有停车
为防止刮蹭,需为停车人找到一个车位
使得停车人的车最近的车辆的距离是最大的
返回此时的最大距离

## 输入描述

1. 一个用半角逗号分割的停车标识字符串,停车标识为 `0` 或 `1` 
`0` 为空位,`1`为已停车

2. 停车位最多有 100 个

## 输出描述

输出一个整数记录最大距离

## 示例描述

### 示例一

**输入：**

```Plain Text
 1,0,0,0,0,1,0,0,1,0,1
```

**输出：**

```Plain Text
2
```

**说明：**
当车停在第三个位置上时,离其最近的车距离为 2(1~3)
当车停在第四个位置上时,离其最近的车距离为 2(4~6)
其他位置距离为 1因此最大距离为 2

## 解题思路

**基本思路：** 

1. 找到最近的已停车车辆（表示为1）：遍历车位状态列表，对于每个已停车车辆（表示为1）计算其与当前空车位的距离（使用索引差的绝对值）。

2. 找到所有距离中的最小值，即为该空车位与最近的已停车车辆之间的距离。

3. 如果该距离大于之前找到的最大距离，则更新最大距离的值。

4. 返回最大距离。

## 解题代码

```Python
def find_max_distance(parking):
    max_distance = 0  # 初始化最大距离为0
    empty = None  # 初始化空车位索引为空
    parking = [int(n) for n in parking.split(",")]

    for i, n in enumerate(parking):
        if n == 0:  
            # 计算该空车位与最近的已停车车辆之间的距离
            distance = min([abs(i - j) for j, x in enumerate(parking) if x == 1])
            if distance > max_distance:  # 如果该距离大于之前找到的最大距离
                max_distance = distance  # 更新最大距离的值
                empty_slot = i  # 更新空车位索引

    return max_distance


if __name__ == "__main__":
    parking = input() #请输入车位状态，以逗号分隔（1代表有车停，0代表空车位）：

    max_distance = find_max_distance(parking)
    print(max_distance)
```

