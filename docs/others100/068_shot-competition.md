# 068 射击比赛

## 题目描述

给定一个射击比赛成绩单，包含多个选手若干次射击的成绩分数，请对每个选手按其最高三个分数之和进行降序排名，输出降序排名后的选手`ID`序列。

条件如下：
1. 一个选手可以有多个射击成绩的分数且次序不固定。
2. 如果一个选手成绩小于三个，则认为选手的所有成绩无效，排名忽略该选手。
3. 如果选手的成绩之和相等，则成绩相等的选手按照其`ID`降序排列。

## 输入描述

输入第一行是一个整数`N`，表示该场比赛总共进行了`N`次射击，产生`N`个成绩分数，取值范围是2 <= N <= 100。

输入第二行是一个长度为`N`的整数序列，表示参与本次射击的选手`ID`，取值范围是0 <= ID <= 99。

输入第三行是长度为`N`的整数序列，表示参与每次射击的选手对应的成绩，成绩的取值范围是0 <= 成绩 <= 100。

## 输出描述

符合题设条件的降序排名后的选手`ID`序列。

## 示例描述

### 示例一

**输入：**
```text
13
3,3,7,4,4,4,4,7,7,3,5,5,5
53,80,68,24,39,76,66,16,100,55,53,80,55
```

**输出：**
```text
5,3,7,4
```

**说明：**

该场射击比赛进行了13次，参赛选手ID为3、4、5、7。

- 3号选手的成绩为53、80、55，最高三个成绩的和为188。
- 4号选手的成绩为24、39、76、66，最高三个和为181。
- 5号选手的成绩为53、80、55，最高三个和为188。
- 7号选手成绩为68、16、100，最高三个和184。
  
比较各个选手最高三个成绩的和，3 = 5 > 7 > 4，由于3号选手和5号选手成绩相等且5>3，所以输出为`5,3,7,4`。

## 解题思路
用字典记录每位选手的分数，如果分数小于三个，剔除选手，然后对每位选手分数取最大三个求和，
根据求和结果与选手id进行降序排列，取出排列结果的id
   

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 068_shot-competition
@time:  23/8/2023 下午 5:24
@project:  huawei-od-python 
"""


def solve_method(id_lst, score_lst):
    id2score = dict()
    for id_, score in zip(id_lst, score_lst):
        if id_ not in id2score:
            id2score[id_] = [score]
        else:
            id2score[id_].append(score)
    items = filter(lambda x: len(x[1]) > 2, list(id2score.items()))
    items = [[id_, sum(sorted(scores)[:3])] for id_, scores in items]
    items = sorted(items, key=lambda x: (x[1], x[0]), reverse=True)
    return ','.join([str(item[0]) for item in items])


if __name__ == '__main__':
    n = int(input().strip())
    id_lst = list(map(int, input().strip().split(',')))
    score_lst = list(map(int, input().strip().split(',')))
    res = solve_method(id_lst,score_lst)
    print(res)


```

