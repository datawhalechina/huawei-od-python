# 241 探索地块建立

## 题目描述
给一块 $n * m$ 的地块，相当于 $n * m$ 的二维数组，每个元素的值表示这个小地块的发电量；
求在这块地上建立正方形的边长为 $c$ 的发电站，发电量满足目标电量 $k$ 地块数量。

## 输入描述
第一行为四个按空格分割的正整数，分别表示 $n, m, c, k$。后面 $n$ 行整数，表示每个地块的发电量。

## 输出描述
输出满足条件的地块的数量

## 示例描述

### 示例一

**输入：**
```
2 5 2 6
1 3 4 5 8
2 3 6 7 1
```

**输出：**
```
4
```

**说明：** 
满足条件的地块有以下几种
第一种：
```
1 3
2 3
```
第二种：
```
3 4
3 6
```
第三种：
```
4 5
6 7
```
第四种：
```
5 8
7 1
```

## 解题思路
**简单提示**
计算每个元素为起点的 `c * c` 个元素之和，分析这些和是否大于目标值 `k`

## 解题代码
``` python
def solution(mat, n, m, threshold, c):
    ans = 0
    # 遍历矩阵中的每个元素
    for i in range(n - c + 1):
        for j in range(m - c + 1):
            sum = 0

            # 计算以该元素为起点的c*c个元素之和
            for k in range(c):
                for l in range(c):
                    sum += int(mat[i + k][j + l])
            
            # 判断是否超预期
            if sum >= threshold:
                ans += 1

    return ans

if __name__ == '__main__':
    while(True):
        # 处理输入格式
        n, m, c, k = map(int, input().split())
        matrix = [list(input().split()) for _ in range(n)]
        
        print(solution(matrix, n, m, k, c))

        ifExit = input("Input exit or quit to quit.\n")
        if ifExit in ["exit", "quit"]:
            break
```