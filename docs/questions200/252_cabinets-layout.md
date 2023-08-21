# 252 机房布局

## 题目描述

小明正在规划一个大型数据中心机房，为了使得机柜上的机器都能正常满负荷工作，需要确保在每个机柜边上至少要有一个电箱。

为了简化题目，假设这个机房是一整排，`M`表示机柜，`I`表示间隔。请你返回这整排机柜，至少需要多少个电箱。如果无解请返回-1。

## 输入描述

输入一行字符串`cabinets`，只能包含`M`和`I`，其中`M`表示机柜，`I`表示间隔，字符串长度范围是1 <= cabinets.length <= 10000

## 输出描述

返回至少需要多少个电箱，才能确保在每个机柜边上至少要有一个电箱。

## 示例描述

### 示例一

**输入：**
```text
MIIM
```

**输出：**
```text
2
```

### 示例二

**输入：**
```text
MIM
```

**输出：**
```text
1
```

### 示例三

**输入：**
```text
M
```

**输出：**
```text
-1
```

### 示例四

**输入：**
```text
MMM
```

**输出：**
```text
-1
```

### 示例五

**输入：**
```text
I
```

**输出：**
```text
0
```

## 解题思路

**基本思路：**
- 若某个机柜的左右两侧都有机柜，则无法摆放电箱，返回-1
- 去除机柜间共用重复电箱的情况：若机柜间放电箱的区域刚好相邻，可去除前一个电箱

1. 初始化电箱区域列表`stack`。
2. 初始化标识`fixed`，`False`表示与上一个电箱没有共享，`True`表示上一个电箱被共享了。
3. 遍历字符串，即遍历所有机柜和间隔：
    - 如果是机柜：
        - 如果左右都没有空间放置电箱（左右均为边界、左右都有电箱），则返回-1。
        - 初始化机柜可放电箱的区域`area`。
        - 判断当前电箱是否能和上一个电箱共享，若是，则去除当前电箱区域  
        - 将当前区域存入电箱区域列表中。
4. 返回电箱区域列表的长度，即最终需要电箱的最少个数。

## 解题代码
```python
def solve_method(cabinets):
    stack = []
    # 去除重复的电箱时 - 需考虑若当前电箱是其他机柜所依赖的电箱，此时不能去除
    fixed = False
    for i in range(len(cabinets)):
        if cabinets[i] == 'M':
            is_left_invalid = i - 1 < 0 or cabinets[i-1] == 'M'
            is_right_invalid = i + 1 == len(cabinets) or cabinets[i+1] == 'M'
            # 若左右都没有空间放置电箱，则返回-1
            if is_left_invalid and is_right_invalid:
                return -1
            area = [max(0, i-1), min(len(cabinets)-1, i+1)]
            # 去除重复放置的电箱
            if stack and not fixed:
                # 合并能共享电箱的区域，只取最后一个
                if stack[-1][1] == area[0]:
                    stack.pop()
                    fixed = True
            else:
                fixed = False
            stack.append(area)
    return len(stack)

if __name__ == "__main__":
    # MIIM
    # cabinets = input().strip()
    # print(solve_method(cabinets))

    assert solve_method("MIIM") == 2
    assert solve_method("MIM") == 1
    assert solve_method("M") == -1
    assert solve_method("MMM") == -1
    assert solve_method("I") == 0
    assert solve_method("MIMIMIM") == 2
```