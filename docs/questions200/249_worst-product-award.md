# 249 最差产品奖

## 题目描述

A公司准备对他下面的 N 个产品评选最差奖，评选的方式是首先对每个产品进行评分，然后根据评分区间计算相邻几个产品中最差的产品。

评选的标准是依次找到从当前产品开始前 M 个产品中最差的产品，请给出最差产品的评分序列。

## 输入描述

第一行，数字 M，表示评分区间的长度，取值范围是 0<M<10000

第二行，产品的评分序列，比如[12,3,8,6,5]，产品数量 N 范围是 −10000<N<10000

## 输出描述

评分区间内最差产品的评分序列

## 示例描述

### 示例一

**输入：**
```text
3
12,3,8,6,5
```

**输出：**
```text
3,3,5
```

**说明：**
```
12,3,8 最差的是3
3,8,6 中最差的是3
8,6,5 中最差的是5
```

## 解题思路

**基本思路：**

..

**代码思路：**
1. 外层循环：遍历数组scores的每个元素
2. 内层循环：计算长度为M的滑动窗口内元素的最小值
3. 列表元素转为字符串，并以逗号分隔转成字符串返回

## 解题代码
```python
def solve_method(M, scores):
    min_scores = []
    for i in range(len(scores)-M+1):
        min_score = scores[i]
        for j in range(1, M):
            min_score = min(min_score, scores[i+j])
        min_scores.append(min_score)
    return ','.join(map(str, min_scores))

if __name__ == "__main__":
    # 3
    # 12,3,8,6,5
    M = int(input())
    scores = list(map(int, input().split(',')))
    print(solve_method(M, scores))

    assert solve_method(3, [12,3,8,6,5]) == "3,3,5"
```