# 252 机房布局

## 题目描述

小明正在规划一个大型数据中心机房，为了使得机柜上的机器都能正常满负荷工作，需要确保在每个机柜边上至少要有一个电箱。

为了简化题目，假设这个机房是一整排，M表示机柜，I表示间隔。请你返回这整排机柜，至少需要多少个电箱。如果无解请返回-1。

## 输入描述

`cabinets="MIIM"`

其中M表示机柜，I表示间隔

## 输出描述
2

表示至少需要2个电箱备注

## 备注

`1<=strlen(cabinets)<=10000` 其中 `cabinets［i］＝'M'`或者`'I'`

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

**代码思路：**
1. 外层循环：遍历字符串，寻找机柜所在的位置
2. 对于每个机柜
    - 若其左右都没有空间放置电箱（左右均为边界、左右都有电箱），则返回-1
    - 否则在栈中存入：机柜可放电箱的区域
    - 判断下一机柜的电箱区域是否和其相邻，若是，则去除当前电箱区域
    - (注意引入变量fixed：若当前电箱兼顾了两个机柜，该电箱物尽其用 - 后续电箱都不能去除)
3. 栈中存储最终电箱需放置的区域，长度即为最少电箱数

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
                if stack[-1][1] == area[0]:
                    stack.pop()
                    fixed = True
                else:
                    fixed = False
            stack.append(area)
    return len(stack)

if __name__ == "__main__":
    # MIIM
    cabinets = input().strip()
    print(solve_method(cabinets))

    assert solve_method("MIIM") == 2
    assert solve_method("MIM") == 1
    assert solve_method("M") == -1
    assert solve_method("MMM") == -1
    assert solve_method("I") == 0
```