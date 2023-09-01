# 009 五子棋迷

## 题目描述

张兵和王武是五子棋迷，工作之余经常切磋棋艺。走了一会儿，轮到张兵了，他对着一条线思考起来了，这条线上的棋子分布如下：

用数组表示：`-1 0 1 1 1 0 1 0 1 -1`。

棋子分布说明：
1. -1代表白子，0代表空位，1代表黑子。
2. 数组长度`L`，满足1 < L < 40，且`L`为奇数。

请帮他写一个程序，算出最有利的出子位置。

最有利的定义：

1. 找到一个空位（0），用棋子（1/-1）填充该位置，可以使得当前子的最大连续长度变大。
2. 如果存在多个位置，返回最靠近中间的较小的那个坐标。
3. 如果不存在可行位置，直接返回-1。
4. 连续长度不能超过5个（五子棋约束）。

## 输入描述

第一行是当前出子颜色。

第二行是当前的棋局状态。

## 输出描述

输出1个整数，表示出子位置的数组下标。

## 示例描述

### 示例一

**输入：**
```text
1
-1 0 1 1 1 0 1 0 1 -1 1
```

**输出：**
```text
5
```

**说明：**  

当前为黑子（1），放置在下标为5的位置，黑子的最大连续长度，可以由3到5。

### 示例二

**输入：**
```text
-1
-1 0 1 1 1 0 1 0 1 -1 1
```

**输出：**
```text
1
```

**说明：** 

当前为白子，唯一可以放置的位置下标为1，白子的最大长度，由1变为2。

### 示例三

**输入：**
```text
1
0 0 0 0 1 0 0 0 0 1 0
```

**输出：**
```text
5
```

**说明：** 

可行的位置很多，5最接近中间的位置坐标。

## 解题思路

1. 遍历每一个空闲的位置：
    - 计算左边连续是当前棋子颜色的个数`left_count`。
    - 计算右边连续是当前棋子颜色的个数`right_count`。
    - 如果总长度小于等于5，满足五子棋约束，则将当前棋子位置和总长度存入结果列表中。
2. 将结果列表按照长度从大到小，与中间的距离从小到大排序。
3. 返回结果值，即结果列表中第一个值的第一个元素（棋子位置）。   

## 解题代码

```python
def solve_method(curr_piece, pieces):
    result = []

    def get_left_count(index):
        left = index - 1
        count = 0
        while left > -1 and pieces[left] == curr_piece:
            count += 1
            left -= 1

        return count

    def get_right_count(index):
        right = index + 1
        count = 0
        while right < len(pieces) and pieces[right] == curr_piece:
            count += 1
            right += 1

        return count

    for i, piece in enumerate(pieces):
        if piece != 0:
            continue

        left_count = get_left_count(i)
        right_count = get_right_count(i)
        total_count = left_count + right_count
        if total_count <= 5:
            result.append([i, total_count])
    
    # 按照长度从大到小，与中间的距离从小到大排序
    result.sort(key=lambda x: (-x[1], abs(x[0] - len(pieces) // 2)))

    return result[0][0]


if __name__ == '__main__':
    pieces = [-1, 0, 1, 1, 1, 0, 1, 0, 1, -1, 1]
    assert solve_method(1, pieces) == 5

    pieces = [-1, 0, 1, 1, 1, 0, 1, 0, 1, -1, 1]
    assert solve_method(-1, pieces) == 1

    pieces = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    assert solve_method(1, pieces) == 5
```