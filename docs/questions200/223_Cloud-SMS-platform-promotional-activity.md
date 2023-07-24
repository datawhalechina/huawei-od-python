# 223 云短信平台优惠活动

## 题目描述
某云短信厂商，为庆祝国庆，推出充值优惠活动。
现在给出客户预算，和优惠售价序列，求最多可获得的短信总条数。

## 输入描述
第一行客户预算$M$，其中 $0 <= M <= 1000000$
第二行给出售价表，$P1,P2,...,Pn$，其中 $1 <= n <= 100$，$Pi$ 为充值i元获得的短信条数。
$1 <= Pi <= 1000$，$1 <= n <= 100$
## 输出描述
最多获得的短信条数
## 示例描述

### 示例一

**输入：**
```
6
10 20 30 40 60
```

**输出：**
```
70
```

**说明：**  
分两次充值最优，1元、5元各充一次。总条数 $10+60=70$

### 示例二

**输入：**
```
15
10 20 30 40 60 60 70 80 90 150
```

**输出：**
```
210
```

**说明：**  
分两次充值最优，10元、5元各充一次。总条数 $150+60=210$

## 解题思路
**一些知识点**
`0-1背包问题；动态规划`

**简单提示**
在消耗预算不超过给定的数 `M` 的前提下，获得最大总条数。
遍历所有可能性，计算总价`max_g`，并记录最大的总价`max_g`。

## 解题代码
``` python
max_g = 0

def solution(mesCount, n, lst, index):
    global max_g

    # 预算已耗光，计算当前总条数，并记录最大值
    if n == 0:
        count = sum(lst)
        max_g = max(max_g, count)
    else:
        for i in range(index, len(mesCount)):
            x = int(mesCount[i])
            lst.append(x)
            solution(mesCount, n - (i + 1), lst, i + 1) # 继续遍历所有可能性
            lst.pop()

if __name__ == '__main__':
    while(True):
        # 处理输入格式
        M = int(input())
        P = input().split()

        solution(P, M, [], 0)

        print(max_g)

        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break
```