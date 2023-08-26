# 188 补种未成活胡杨树

## 题目描述

某沙漠新种植`N`颗胡杨（编号1\~N），一个月后，有`M`颗未能成活。现可补种`K`颗（只可补种，不可新种），请问怎样补种，可以得到最多的连续胡杨树？

## 输入描述

第一行是`N`，表示总种植数量，其中1 <= N < 1000。

第二行是`M`，表示未成活数量，其中1 <= M < N。

第三行是`M`个空格分隔的数，按编号从小到大排列。

第四行是`K`，表示最多可以补种的数量，其中O <= K <= M。

## 输出描述

输出补种胡杨树的位置下标，才能得到最多的连续胡杨树。

## 示例描述

### 示例一

**输入：**

```text
10
3
2 4 7
1
```

**输出：**

```text
6
```

**说明：**

补种第7颗，可得到5、6、7、8、9、10共5棵连续的胡杨树。

## 解题思路

1. 在 while 循环内部，有另一个 while 循环，直到 `count` 小于等于 `k`。 

   a. 如果 `rolls[right]` 的值为 1，则增加 `count` 的计数。 

   b. 增加 `right` 的值。 

   c. 如果 `count` 仍然小于等于 `k`，则将当前子数组的长度（`right - left`）与 `result` 的值进行比较，并将较大的值存储在 `result` 中。

2. 内部 while 循环结束后，有另一个 while 循环，直到 `left` 小于等于 `right` 且 `count` 大于 `k`。 a. 如果 `rolls[left]` 的值为 1，则减少 `count` 的计数。 b. 增加 `left` 的值。



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

