# 011 乘坐保密电梯

## 题目描述

有一座保密大楼，你从0楼到达指定楼层`m`，必须这样的规则乘坐电梯：

给定一个数字序列，每次根据序列中的数字`n`上升`n`层或者下降`n`层，前后两次操作的方向必须相反，规定首次的方向向上，自行组织序列的顺序按规定操作到达指定楼层。

求解到达楼层的序列组合，如果不能到达楼层，给出小于该楼层的最近序列组合。

**说明：**

- 操作电梯时，不限定楼层范围。
- 必须对序列中的每个项进行操作，不能只使用一部分。

## 输入描述

第一行是期望的楼层，取值范围是`[1,50]`；序列总个数，取值范围是`[1,23]`。

第二行是序列，每个值取值范围是`[1,50]`。

## 输出描述

能够达到楼层或者小于该楼层最近的序列。

## 示例描述

### 示例一

**输入：**
```text
5 3
1 2 6
```

**输出：**
```text
6 2 1
```

**说明：**  

`1 2 6`、`6 2 1`均为可行解，按先处理大值的原则结果为`6 2 1`。

## 解题思路

**基本思路：** 使用回溯法求解。

1. 使用回溯法：
    - 确定参数：当前到达的楼层`curr_floor`、当前方向`curr_direction`、当前已操作的序列`curr_sequence`、当前剩余要操作的序列`sequence`。
    - 终止条件：
      - 当所有序列都已经操作完毕，并且当到达的楼层小于等于目标楼层，将操作序列和到达的楼层加入结果列表中。
      - 当所有序列都已经操作完毕，直接返回。
    - 递归遍历：
      - 将当前操作的数字加入到`curr_sequence`。
      - 计算下一个到达的楼层`next_floor`。
      - 剩余要操作的序列`sequence`删除当前操作的数字。
      - 继续递归。
      - 回溯：将当前操作的数字加入到剩余要操作的序列`sequence`中，当前已操作的序列`curr_sequence`删除当前操作数字。
2. 将结果列表按照楼层从大到小、操作数字从大到小排序。
3. 返回结果列表中的第一个元素的操作序列。

## 解题代码

```python
def solve_method(m, steps):
    result = []

    def backtracking(curr_floor, curr_direction, curr_sequence, sequence):
        seq = sequence.copy()

        if len(seq) == 0:
            # 当所有序列都已经操作完毕
            if curr_floor <= m:
                # 当到达的楼层小于等于目标楼层
                result.append((curr_sequence.copy(), curr_floor))
            return

        for i in range(len(seq)):
            curr_sequence.append(seq[i])
            next_floor = curr_floor + seq[i] if curr_direction else curr_floor - seq[i]
            # 操作方向相反
            next_direction = not curr_direction
            num = seq.pop(i)
            backtracking(next_floor, next_direction, curr_sequence, seq)
            # 回溯
            seq.insert(i, num)
            curr_sequence.remove(seq[i])

    backtracking(0, True, [], steps)
    
    # 按照楼层从大到小、操作数字从大到小排序
    result.sort(key=lambda x: (-x[1], -x[0][0]))
    return result[0][0]


if __name__ == '__main__':
    assert solve_method(5, [1, 2, 6]) == [6, 2, 1]
```