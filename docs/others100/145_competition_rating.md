# 145 比赛评分

## 题目描述

一个有N个选手参加的比赛，选手编号为从1到N（3＜＝N＜＝100），有M（3＜＝M＜＝10）个评委对选手进行打分。

打分规则为每个评委对选手打分，最高分10分，最低分1分。

请计算得分最多的3位选手的编号。

如果得分相同，则得分高分值最多的选手排名靠前（10分数量相同，则比较9分的数量，以此类推，用例中不会出现多个选手得分完全相同的情况）。



## 输入描述

第一行为半角逗号分割的两个正整数，第一个数字表示M个评委，第二个数字表示N个选手。
第2到M＋1行是半角逗号分割的整数序列，表示评委为每个选手的打分，0号下标数字表示1号选手分数，1号下标数字表示2号选手分数，依次类推。

注意：

- 评委数 M 需要满足：3＜＝M＜＝10
- 选手数 N 需要满足：3＜＝N＜＝100
- 每个评分需要满足 r： 1 <= r <= 10
- 输入可能有不合理的评委、选手数或者无效的打分。



## 输出描述

选手前3名的编号。

注：若输入为异常，输出—1，如M、N、打分不在范围内。



## 示例描述

### 示例一

**输入：**

```text
4,5
10,6,9,7,6
9,10,6,7,5
8,10,6,5,10
9,10,9,4,9
```

**输出：**

```bash
2,1,5
```



**说明：**  

第一行代表有4个评委，5个选手参加比赛
矩阵代表是4＊5，每个数字是选手的编号，每一行代表一个评委对选手的打分排序，
2号选手得分36分排第1，1号选手36分排第2，5号选手30分（2号10分值有3个，1号10分值只有1个，所以2号排第一）




### 示例二

**输入：**

```text
2,5
7,3,5,4,2
8,5,4,4,3
```

**输出：**

```text
-1
```

**说明：**  

要求最少3个评委






### 示例三

**输入：**

```text
4,2
8,5
5,6
10,4
8,9
```

**输出：**

```text
-1
```

**说明：**  

要求最少3个选手参加






### 示例四

**输入：**

```text
4,5
11,6,9,7,8
9,10,6,7,8
8,10,6,9,7
9,10,8,6,7
```

**输出：**

```text
-1
```

**说明：**  

第一个评委给选手打11分，无效分数




## 解题思路

**基本思路：** 

1. 根据输入输出示例二、三、四，先写输入检查，确定M、N、评分满足输入要求，否则返回“-1”
2. 这道题本质上是一道多键值排序题，我们需要根据运动员的总分、每个得分的次数，进行排序，所以我们在处理输入的`ratings`时，可以保存相关信息（总分、得1分得次数、得2分得次数...）
   - 这里我使用 得分频数矩阵 `scores` 记录选手得分情况，用`scores\[i][j]` 表示`运动员 i `得到分数 j 的次数, `scores\[i][0] `表示`运动员 i `得到的总分
3. 接下来可以循环处理输入的评分数据，并在`scores`里记录
4. 之后，我们只需要自定义一个排序方法，然后就可以利用python预定义的`sorted()`方法快速排序
5. 最后，将前三名的id取出，包装成字符串类型返回

## 解题代码

```python
from typing import List
from functools import cmp_to_key

def solve_method(M: int, N: int, ratings: List[List[int]]) -> str:
    # 1. 检查输入参数是否满足要求(M,N,评分)
    if not (3 <= M <= 10) or not (3 <= N <= 100):
        return "-1"
    for row in ratings:
        if not all(1 <= num <= 10 for num in row):
            return "-1"

    # 2.用 *得分频数矩阵* scores 记录选手得分情况
    # scores[i][j] 表示运动员 i 得到分数 j 的次数, scores[i][0] 表示运动员 i 得到的总分
    scores = [[0] * 11 for _ in range(101)]

    # 3.遍历评分,记录分数
    for i in range(M):
        for j in range(N):
            score = ratings[i][j]

            # 运动员编号从 1 到 N
            player_id = j + 1
            scores[player_id][0] += score  # 运动员总分增加
            scores[player_id][score] += 1  # 运动员的某个分数频数+1

    # 4. 自定义排序规则
    def compare_function(id1: int, id2: int) -> int:
        player1 = scores[id1]  # 通过运动员编号id,让player保存每个运动员的得分情况
        player2 = scores[id2]
        if player1[0] != player2[0]:  # player1[0]是1号运动员的总分
            return -1 * (player1[0] - player2[0])  # -1 是逆序; 让总分高的排前边

        # 接下来比较得分高分值的频数
        for score in range(10, -1, -1):
            if player1[score] != player2[score]:
                return -1 * (player1[score] - player2[score])  # -1 是逆序; 让得分高分值最多的选手排名靠前

        return 0

    # 5.根据记录的分数 scores 和我们定义的排序规则排序(第一名，第二名，...)
    rank = sorted(range(1, N + 1), key=cmp_to_key(compare_function))

    # 6.将前三名的id转化为string后返回
    return ",".join([str(rank[0]), str(rank[1]), str(rank[2])])
```