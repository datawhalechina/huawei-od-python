# 020 拔河比赛

## 题目描述

公司最近准备进行拔河比赛，需要在全部员工中进行挑选。选拔的规则如下：

1. 按照身高优先、体重次优先的方式准备比赛阵容。
2. 规定参赛的队伍派出10名选手。
   
请实现一个选拔队员的小程序。

输入为一个数组，记录了部门人员的身高、体重信息，如`[身高，体重]`的方式放置，部门全部成员数量为大于10的一个数组。

要求输出一个`size`为10的二维数组。输入数据范围：

1. 成员身高、体重为整数类型。
2. 输入备选成员数量为`N`，取值范围是10 <= N <= 100。

## 输入描述

输入为`N`行员工信息，表示部门报名参加选拔的候选人信息，每行有两个数字，使用空格分隔，表示员工的身高、体重信息，如：
```text
181 70
182 70
```

表示两位候选员工，第一人身高181厘米，体重70公斤；第二人身高182厘米，体重70公斤。

输入数据范围：
1. 成员身高、体重为整数类型。
2. 输入备选成员数量为`N`，取值范围是10 <= N <= 100。

## 输出描述

要求输出一个10行的已经排序的参赛员工信息数据，每行有两个数字，使用空格分隔，表示员工的身高、体重信息，如：

```text
182 70
181 70
```

## 示例描述

### 示例一

**输入：**
```text
181 70
182 70
183 70
184 70
185 70
186 70
180 71
180 72
180 73
180 74
180 75
```

**输出：**
```text
186 70
185 70
184 70
183 70
182 70
181 70
180 75
180 74
180 73
180 72
```

## 解题思路

1. 将按照部门人员的身高从高到低、体重从大到小排序
2. 返回结果，即前10名选手。

## 解题代码

```python
def solve_method(arr):
    # 按照身高从高到低、体重从大到小排序
    arr.sort(key=lambda x: (-x[0], -x[1]))
    # 选出10名选手
    return arr[:10]


if __name__ == '__main__':
    arr = [[181, 70], [182, 70], [183, 70], [184, 70], [185, 70],
           [186, 70], [180, 71], [180, 72], [180, 73], [180, 74],
           [180, 75]]
    assert solve_method(arr) == [[186, 70], [185, 70], [184, 70], [183, 70], [182, 70],
                                 [181, 70], [180, 75], [180, 74], [180, 73], [180, 72]]
```