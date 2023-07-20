# 201 运动会

## 题目描述

某学校举行运动会，学生们按编号（1,2,3,...,n）进行标识，现需要按照身高由低到高排列，对身高相同的人，按体重由轻到重排列，对于身高体重都相同的人，维持原有的编号顺序关系。请输出排列后的学生编号。

## 输入描述

两个序列，每个序列由`N`个正整数组成（0 < n <= 100）。第一个序列中的数值代表身高，第二个序列中的数值代表体重。

## 输出描述

排列结果，每个数据都是原始序列中的学生编号，编号从`1`开始。

## 示例描述

### 示例一

**输入：**
```text
4    
100 100 120 130
40 30 60 50
```

**输出：**
```text
2 1 3 4
```

### 示例二

**输入：**
```text
3
90 110 90 
45 60 45
```

**输出：**

```text
1 3 2
```

## 解题思路

1. 遍历编号：使用三元组`(学生编号,身高,体重)`存储学生信息，并存入结果列表`result`中。
2. 使用`sort`方法，按身高升序、体重升序排列。
3. 遍历结果列表，取出学生编号列表。

```python
def solve_method(n, heights, weights):
    result = []
    for i in range(n):
        # 使用元组存储数据
        result.append((i + 1, heights[i], weights[i]))
    result.sort(key=lambda x: (x[1], x[2]))

    return [x[0] for x in result]


if __name__ == "__main__":
    heights = [100, 100, 120, 130]
    weights = [40, 30, 60, 50]
    assert solve_method(4, heights, weights) == [2, 1, 3, 4]

    heights = [90, 110, 90]
    weights = [45, 60, 45]
    assert solve_method(3, heights, weights) == [1, 3, 2]
```

