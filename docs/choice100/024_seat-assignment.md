# 024 新员工座位安排系统

## 题目描述

工位由序列$F_1,F_2,\cdots,F_n$组成，$F_i$值为0、1、2，其中0代表空置，1代表有人，2代表障碍物。，座位安排有如下规则：
1. 某一空位的友好度为左右连续老员工工位数之和
2. 为方便新员工学习求助，优先安排友好度高的空位

给出工位序列，求所有空位中友好度的最大值。

## 输入描述

第一行表示工位序列：$F_1,F_2,\cdots,F_n$，其中1 <= n <= 100000，$F_i$值为0、1、2，其中0代表空置，1代表有人，2代表障碍物。

## 输出描述

所有空位中友好度的最大值，如果没有空位，返回0。

## 示例描述

### 示例一

**输入：**
```text
0 1 0
```

**输出：**
```text
1
```

### 示例二

**输入：**
```text
1 1 0 1 2 1 0
```

**输出：**
```text
3
```

## 解题思路

1. 初始化最大友好度、对应位置。
2. 遍历数组：
    - 当位于最左侧：友好度为后一个工位数。
    - 当位于最右侧：友好度为前一个工位数。
    - 当位于其他区域：友好度为前后两个工位数之和。
    - 比较友好度，获取最大友好度及对应位置。
3. 返回最大友好度对应的位置。

## 解题代码

```python
def solve_method(arr):
    max_value = 0
    max_pos = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            if i == 0:
                # 最左侧
                friend_value = arr[i + 1]
            elif i == len(arr) - 1:
                # 最右侧
                friend_value = arr[i - 1]
            else:
                # 其他区域
                friend_value = arr[i - 1] + arr[i + 1]
            # 比较友好度
            if friend_value > max_value:
                max_value = friend_value
                max_pos = i
    return max_pos + 1


if __name__ == '__main__':
    assert solve_method([0, 1, 0]) == 1
    assert solve_method([1, 1, 0, 1, 2, 1, 0]) == 3
```