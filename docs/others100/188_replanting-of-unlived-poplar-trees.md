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

**基本思路：** 使用双指针求解。

1. 将需要补种的胡杨树位置设为1，已成活的位置设为0。
2. 使用双指针：
    - 得到连续补种`K`棵之后，并且不为1的位置`right`。
    - 如果已经找到K个，计算补种之后的连续胡杨树的个数，得到最大连续胡杨树的个数。
    - 找到在[left, right]中第一个为1的位置，然后加1，更新左指针`left`，并减去多加的个数。
3. 返回结果，即最多的连续胡杨树的个数。    

## 解题代码

```python
def solve_method(N, M, trees, K):
    rolls = [0] * N

    for tree in trees:
        rolls[tree - 1] = 1

    left = 0
    right = 0
    count = 0
    result = 0

    while right < N:
        while right < N and count <= K:
            if rolls[right] == 1:
                # 如果找到需要补种的胡杨树，则count累加1
                count += 1
            right += 1

            if count <= K:
                # 如果已经找到K个，计算补种之后的连续胡杨树的个数
                result = max(right - left, result)

        # 找到在[left, right]中第一个为1的位置，然后加1，更新左指针
        left = rolls.index(1, left, right) + 1
        # 减去多加的个数
        count -= 1
    return result


if __name__ == '__main__':
    assert solve_method(10, 3, [2, 4, 7], 1) == 6
    assert solve_method(10, 3, [2, 4, 7], 2) == 8
    assert solve_method(10, 3, [2, 4, 7], 3) == 10
```

