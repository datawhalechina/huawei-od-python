# 084 找最小数

## 题目描述

给一个正整数`NUM1`，计算出新正整数`NUM2`，`NUM2`为`NUM1`中移除`N`位数字后的结果，需要使得`NUM2`的值最小。

## 输入描述

输入的第一行是一个字符串，字符串由`0-9`字符组成，记录正整数`NUM1`，`NUM1`长度小于32。

输入的第二行是需要移除的数字的个数，小于`NUM1`长度。

## 输出描述

输出一个数字字符串，记录最小值`NUM2`。

## 示例描述

### 示例一

**输入：**
```text
2615371
4
```

**输出：**
```text
131
```

**说明：**  

移除2、6、5、7这四个数字，剩下1、3、1按原有顺序排列组成131为最小值。

### 示例二

**输入：**
```text
123456
4
```

**输出：**
```text
12
```

## 解题思路

**基本思路：** 使用贪心算法解题。
1. 将数字转换为字符串列表`nums`。
2. 初始化栈`stack`，用于存储数字。
3. 初始化`removed`，表示需要移除的数字个数。 
4. 遍历字符串列表`nums`：
   - 如果栈顶的数字大于当前数字且还有剩余的移除次数，则弹出栈顶数字
   - 如果不满足上述条件，则将当前数字入栈。
5. 如果还有剩余的数字需要移除。    
6. 将栈`stack`的字符串转成数值，返回结果。

## 解题代码

```python
def solve_method(num, n):
    nums = list(str(num))
    # 使用栈来存储数字
    stack = []
    # 表示需要移除的数字个数
    removed = 0

    for digit in nums:
        # 如果栈顶的数字大于当前数字且还有剩余的移除次数，则弹出栈顶数字
        while stack and removed < n and stack[-1] > digit:
            stack.pop()
            removed += 1
        stack.append(digit)

    # 如果还有剩余的数字需要移除
    while removed < n:
        stack.pop()
        removed += 1

    # 构建最终的结果
    return int("".join(stack))


if __name__ == '__main__':
    assert solve_method(2615371, 4) == 131
    assert solve_method(123456, 4) == 12
```