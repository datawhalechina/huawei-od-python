# 225 优选核酸检测点

## 题目描述

张三要去外地出差，需要做核酸，需要在指定时间点前做完核酸，  
请帮他找到满足条件的核酸检测点。

1. 给出一组核酸检测点的距离和每个核酸检测点当前的人数
2. 给出张三要去做核酸的出发时间 出发时间是10分钟的倍数  

    同时给出张三做核酸的最晚结束时间
3. 题目中给出的距离是整数，单位是公里，时间1分钟为一基本单位

去找核酸点时，有如下的限制：

1. 去往核酸点的路上，每公里距离花费时间10分钟，费用是10元
2. 核酸点每检测一个人的时间花费是1分钟
3. 每个核酸点工作时间都是8点到20点中间不休息  

    核酸点准时工作，早到晚到都不检测
4. 核酸检测结果可立刻知道
5. 在张三去某个核酸点的路上花费的时间内，此核酸检测点的人数是动态变化的，变化规则是
    1. 在非核酸检测时间内，没有人排队
    2. 8点-10点每分钟增加3人
    3. 12点-14点每分钟增加10人

要求将所有满足条件的核酸检测点按照优选规则排序列出 ：  
优选规则：

1. 花费时间最少的核酸检测点排在前面。
2. 花费时间一样,花费费用最少的核酸检测点排在前面。
3. 时间和费用一样，则ID值最小的排在前面

## 输入描述
```
H1 M1
H2 M2
N
ID1 D1 C1
ID2 D2 C2
...
IDn Dn Cn
```

`H1`: 当前时间的小时数。
`M1`：当前时间的分钟数，
`H2`：指定完成核酸时间的小时数。
`M2`：指定完成核酸时间的分钟数。
`N`：所有核酸检测点个数。
`ID1`：核酸点的ID值。
`D1`：核酸检测点距离张三的距离。
`C1`：核酸检测点当前检测的人数。

## 输出描述
```
N
I2 T2 M2
I3 T3 M3
```

`N`：满足要求的核酸检测点个数
`I2`:选择后的核酸检测点ID
`T2`:做完核酸花费的总时间(分钟)
`M3`:去该核酸点花费的费用
  
## 示例描述

### 示例一

**输入：**
```
10 30
14 50
3
1 10 19
2 8 20
3 21 3
```

**输出：**
```
2
2 80 80
1 190 100
```

## 解题思路
**简单提示**

做完核酸花费的总时间 

= 到达核酸点的时间 + 到达核酸点时等待排在前的人做完核酸的时间

= 到达核酸点的时间 + 核酸点当前检测的人数

= 到达核酸点的时间 + 出发时核酸点当前检测的人数 + 检测人数的动态变化

检测人数的动态变化如下图所示：

![image](images/225-001-sample-analysis.png)


## 解题代码
``` python
import heapq

def solve_method(start_time, end_time, sites):
    (EIGHT_ACLOCK, TEN_ACLOCK, TWELVE_ACLOCK, FORTEEN_ACLOCK, TWENTY_ACLOCK) = \
    (8 * 60, 10 * 60, 12 * 60, 14 * 60, 20 * 60)
         
    # 模拟从出发到每个核酸点的时间变化过程
    selected = [] 

    for site in sites:
        id, distance, people = site
        time_cost = distance * 10 # 计算到达核酸点花费的时间 = 需要花费的费用
        arrive_time = start_time + time_cost    # 到达时间
        test_time = 0
        
        if arrive_time > end_time: # 到达核酸点后，若已超过结束时间，则不再模拟后续过程
            continue

        # 模拟到达核酸检测点后，前面还有多少人
        if  start_time < TEN_ACLOCK:
            # 计算 start_time - arrive_time 在 8:00 - 10:00 区间内的时长
            queue_time = min(TEN_ACLOCK, arrive_time) - max(EIGHT_ACLOCK, start_time)
            if queue_time > 0:  # 8:00 - 10:00 每分钟新增3人
                people += queue_time * (3 - 1)
        
        if start_time < TWELVE_ACLOCK: # 10:00 - 12:00 无新增
            people = max(people - (min(TWELVE_ACLOCK, arrive_time) - max(start_time, TEN_ACLOCK)), 0)

        if start_time < FORTEEN_ACLOCK:
            # 计算 start_time - arrive_time 在 12:00 - 14:00 区间内的时长
            quque_time = min(FORTEEN_ACLOCK, arrive_time) - max(TWELVE_ACLOCK, start_time)
            if quque_time > 0:  # 12:00 - 14:00 每分钟新增10人
                people += quque_time * (10 - 1)

        if start_time < TWENTY_ACLOCK and arrive_time > FORTEEN_ACLOCK: # 14:00 - 20:00 无新增
            people = max(people - (arrive_time - max(start_time, FORTEEN_ACLOCK)), 0)
        
        # 判断是否能在规定时间内完成核酸    
        if arrive_time + people <= end_time:
            selected.append((id, time_cost + people, time_cost))
            
    # 按题目要求排序        
    selected.sort(key=lambda x: (x[1], x[2], x[0])) 
    
    return len(selected), selected

# 打印输出
if __name__ == '__main__':
    while(True):
        start = 10 * 60 + 30
        end = 14 * 60 + 50
        sites = {(1, 10, 19), (2, 8, 20), (3, 21, 3)}

        assert solve_method(start, end, sites) == (2, [(2, 80, 80), (1, 190, 100)])
```