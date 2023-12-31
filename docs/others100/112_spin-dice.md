# 112 旋转骰子

## 题目描述

骰子是一个正方体，每个面有一个数字，初始为左1、右2、前3、后4、上5、下6，用`123456`表示这个状态，放置在平面上。

- 可以向左翻转（用`L`表示向左翻转1次）
- 可以向右翻转（用`R`表示向右翻转1次）
- 可以向前翻转（用`F`表示向前翻转1次）
- 可以向后翻转（用`B`表示向后翻转1次）
- 可以逆时针翻转（用`A`表示向逆时针翻转1次）
- 可以向顺时针翻转（用`C`表示向顺时针翻转1次）

现从`123456`这个初始状态开始，根据输入的动作序列，计算最终的状态。

## 输入描述

输入字符串，表示骰子旋转操作。字符取值范围是`L`、`R`、`F`、`B`、`A`、`C`。

## 输出描述

输出一行数字，表示骰子旋转之后的状态，依照顺序表示骰子左面、右面、前面、后面、上面、下面的数字。

## 示例描述

### 示例一

**输入：**

```text
LR
```

**输出：**

```text
123456
```

### 示例二

**输入：**

```text
FCR
```

**输出：**

```text
342156
```

## 解题思路

1. 建立一个`roll_switch`字典，记录不同操作应该交换数字序列的位置。
   - 当向左翻转，左右位置逆转，左右和上下的位置交换。
   - 当向右翻转，上下位置逆转，上下和左右的位置交换。
   - 当向前翻转，前后位置逆转，前后和上下的位置交换。
   - 当向后翻转，上下位置逆转，上下和前后的位置交换。
   - 当逆时针翻转，前后位置逆转，前后和左右的位置交换。
   - 当顺时针翻转，左右位置逆转，左右和前后的位置交换。
2. 遍历字母序列 ，交换`res`序列的位置。
3. 返回结果。

## 解题代码

```python
def solve_method(line):
    res = ['1', '2', '3', '4', '5', '6']

    roll_switch = {
        "L": lambda: roll(res, 0, 2, 4, 6),
        "R": lambda: roll(res, 4, 6, 0, 2),
        "F": lambda: roll(res, 2, 4, 4, 6),
        "B": lambda: roll(res, 4, 6, 2, 4),
        "A": lambda: roll(res, 2, 4, 0, 2),
        "C": lambda: roll(res, 0, 2, 2, 4)
    }
    for c in line:
        roll_switch[c]()

    return "".join(res)


def roll(res, s1, e1, s2, e2):
    res[s1:e1], res[s2:e2] = res[s2:e2], res[s1:e1][::-1]
    return res


if __name__ == "__main__":
    assert solve_method("LR") == "123456"
    assert solve_method("FCR") == "342156"
```
