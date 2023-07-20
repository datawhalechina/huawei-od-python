# 014-事件推送

## 题目描述

同一个数轴X上有两个点的集合A={A1,A2,,Am}和B={B1,B2,...,Bn},
Ai和Bj均为正整数，A、B已经按照从小到大排好序，A、B均不为空，
给定一个距离R(正整数)，
列出同时满足如下条件的所有（Ai,Bj)数对：
1.Ai <=Bj
2.Ai,Bj之间的距离小于等于R
3.在满足1,2的情况下，每个Ai只需输出距离最近的Bj
4.输出结果按Ai从小到大的顺序排序

## 输入描述

第一行三个正整数m,n,R
第二行m个正整数，表示集合A
第三行n个正整数，表示集合B
输入限制：
1<=R<=100000,1<=n,m<=100000,1<=Ai,Bj<=1000000000                              

## 输出描述

每组数对输出一行Ai和Bj,，以空格隔开

## 示例描述

### 示例一

**输入：**
```
4 5 5
1 5 5 10
1 3 8 8 20 
```

**输出：**
```
1 1
5 8 
5 8
```

## 解题思路

本道题的解题思路是：从输入的数据中读取两个数组a和b,然后使用solve函数处理它们
该函数的目的是在数组中找出所有的数，并在b数组中找出与它们相邻的数。如果差值在R内，则将它们的组合加入结果数组。

## 解题代码

```python
def main():
    # 读取输入的 m、n 和 R
    m, n, R = map(int, input().split())
    # 读取输入的列表 a 和 b
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 调用 solve 函数进行计算，并将结果保存在 result 中
    result = solve(R, a, b)
    # 遍历结果列表并输出每一对数字
    for r in result:
        print(r[0], r[1])

def solve(R, a, b):
    index = 0
    result = []
    for j in a:
        ints = [0, 0]
        while index < len(b):
            if j <= b[index] and b[index] - j <= R:
                ints[0] = j
                ints[1] = b[index]
                result.append(ints)
                break
            index += 1
    return result

if __name__ == "__main__":
    main()
```