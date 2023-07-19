# 017_人数最多的站点oc

## 题目描述

公园园区提供小火车单向通行，从园区站点编号最小到最大，
通行如1 ~ 2 ~ 3 ~ 4 ~ 1 ，然后供员工在各个办公园区穿梭，
通过对公司N个员工调研统计到每个员工的坐车区间，包含前后站点，
请设计一个程序计算出小火车在哪个园区站点时人数最多。

## 输入描述

输入的第1个行，为调研员工人数
第2行开始，为每个员工的开始上车站点和下车站点。
使用数字代替每个园区用空格，分割如3 5表示从第3个园区上车，
在第5个园区下车

## 输出描述

人数最多时的园区站点编号，最多人数相同时返回编号最小的园区站点

## 示例描述

### 示例一

**输入：**
```text
3
1 3
2 4
1 4
```

**输出：**
```text
2
```

**说明：**  
第1行3代表调研员工总人数为3，
小火车在第1个园区时，车上有两个人
到第2个园区时，有三个人
到第3个园区，是三个人，
到第4个园区，是两个人
返回数字最小的园区，所以输出2

## 解题思路

统计一组数据中，哪一个数字出现最多的次数。

## 解题代码

```python
# coding:utf-8
import collections
def solve_method(ints):
    # 用来存储每个数字的频率
    map = collections.defaultdict(int)
    for pair in ints:
        for i in range(pair[0],pair[1] + 1):
            map[i] += 1
    # 创建一个由元组组成的列表，每个元组包含一个数字和它的频率
    list = [(k,v) for k,v in map.items()]
    # 根据数字的频率对列表进行降序排序
    list.sort(key=lambda x:x[1],reverse=True)
    print(list[0][0])

if __name__ =="__main__":
    n = int(input().strip())
    ints = [list(map(int,input().strip().split())) for _ in range(n)]
    solve_method(ints)
```

