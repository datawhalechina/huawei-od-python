# 189 观看文艺汇演问题、最多能看几场演出

## 题目描述

为了庆祝成立100周年，某公园将举行多场文艺表演，很多演出都是同时进行，一个人只能同时观看一场演出，且不能迟到早退，由于演出分布在不同的演出场地，所以连续观看的演出最少有15分钟的时间间隔，小明是一个狂热的文艺迷，想观看尽可能多的演出。

现给出演出时间表，请帮小明计算他最多能观看几场演出。

## 输入描述

第一行是一个数`N`，表示演出场数，其中1 <= N <= 1000。

接下来`N`行，每行两个空格分隔的整数，第一个整数`T`表示演出的开始时间，第二个整数`L`表示演出的持续时间，`T`和`L`的单位为分钟，取值范围是0 <= T <= 1440、0 < L <= 100。

## 输出描述

最多能观看的演出场数。

## 示例描述

### 示例一

**输入：**

```text
2
720 120
840 120
```

**输出：**

```text
1
```

### 示例二

**输入：**

```text
2
0 60
90 60
```

**输出：**

```text
2
```

## 解题思路

1. 题解时基于时间段的排序和贪心策略。
2. 我们使用一个二维数组times来存储每个时间段的起始时间和结束时间。
3. 按照结束时间对时间段进行排序。
4. 初始化一个变量t为第一个时间段的结束时间，以及一个变量result为初始值1，表示最多能观看的一场。
5. 遍历排序后的时间段数组，对于每个时间段，获取其初始时间l和结束时间r。如果当前时间段的起始时间与前一个时间段的结束时间之差大于等于15分钟，则表示多增一场，将result值加一，并更新t为当前时间段的结束时间。

## 解题代码

```python
num_of_dice = int(input())
num_of_sides = int(input())
dice_strings = input().split()

rolls = [0] * num_of_dice
k = int(input())

for i in range(num_of_sides):
    rolls[int(dice_strings[i]) - 1] = 1

left = 0
right = 0
count = 0
result = 0

while right < num_of_dice:
    while right < num_of_dice and count <= k:
        if rolls[right] == 1:
            count += 1
        right += 1

        if count <= k:
            result = max(right - left, result)
    while left <= right and count > k:
        if rolls[left] == 1:
            count -=1
        left += 1

print(result)
```

