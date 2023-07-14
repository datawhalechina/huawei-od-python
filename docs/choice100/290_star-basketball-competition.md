# 290 星际篮球争霸赛

## 题目描述

在星际争霸篮球赛对抗赛中，最大的宇宙战队希望每个人都能拿到MVP，MVP的条件是单场最高分得分获得者。可以并列。所以宇宙战队决定在比赛中，尽可能让更多队员上场，并且让所有得分的选手得分都相同，然而比赛过程中的每1分钟的得分都只能某一个人包揽。

## 输入描述

第一行为一个数字`t`，表示有得分的分钟数（1 <= t <= 50）

第二行为`t`个数字，表示每一分钟的得分`p`

## 输出描述

输出有得分的队员都是MVP时，最少的MVP得分。

## 示例描述

### 示例一

**输入：**
```
9
5 2 1 5 2 1 5 2 1
```

**输出：**
```
6
```

**说明：**  
一共4个人得分，分别都是6分：5+1、5+1、5+1、2+2+2

## 解题思路

1. 计算得分记录的总和`sum_score`
2. 遍历得分记录（最大可能由`num`个球员进球，逐步递减，计算最多能被多少个球员平分得分）：
    - 判断当前人数是否能平分得分：再次遍历得分记录，去掉当前得分，继续判断是否还能平分得分
    - 如果可以，返回`sum_score // i`

## 解题代码

```python
def split_score(arr, num, original_num):
    if len(arr) == 0 and num == original_num:
        return True

    flag = False
    for i in range(len(arr)):
        # 去掉当前得分，继续判断是否还能平分得分
        sub_arr = arr[:i] + arr[i + 1:]
        if arr[i] == num:
            # 示例中等于2的情况
            flag = flag or split_score(sub_arr, original_num, original_num)
        elif arr[i] < num:
            # 示例中等于5的情况
            flag = flag or split_score(sub_arr, num - arr[i], original_num)

    return flag


def solve_method(arr):
    sum_score = sum(arr)
    num = len(arr)
    # 最大可能由num个球员进球，逐步递减，计算最多能被多少个球员平分得分
    for i in range(num, 0, -1):
        if sum_score % i == 0:
            # 判断是否能平分成功
            if split_score(arr, sum_score // i, sum_score // i):
                return sum_score // i

    return sum_score
```