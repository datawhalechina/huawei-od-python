# 163 - 病菌感染

## 题目

在一个地图中(地图有`N*N`个区域组成)有部分区域被感染病菌，感染区域每天都会把周围上下左右的四个区域感染，请根据给定的地图计算多少天以后全部区域都会被感染如果初始地图上所有区域都被感染或者没有被感染区域返回-1

备注：
`1 <= N< 200`



## 输入

一行`N*N`个数字只包含 `0 1`，不会有其他数字表示一个地图
数字间用,分割

`0`表示未感染区域，`1`表示感染区域

每`N`个数字表示地图中—行

输入数据共表示`N`行`N`列的区域地图

例如输入:
`1,0,1,0,0,0,1,0,1`

表示地图:

`1,0,1`

`0,0,0`

`1,0,1`

## 输出描述

—个整数表示经过多少天以后全部区域都会被感染



## 示例一

### 输入

```python
1,0,1,0,0,0,1,0,1
```

### 输出

```
2
```

### 说明

1天以后地图中仅剩中心点未被感染

2天以后全部被感染



## 示例二

### 输入

```python
0,0,0,0
```

### 输出

```
-1
```

### 说明

无感染区域



## 示例三

### 输入

```python
1,1,1,1,1,1,1,1,1
```

### 输出

```
-1
```

### 说明

全部感染



## 解题思路

思路很简单：

1.先将给定的数组等行等列切分

2.搜寻初始化的病菌位置

3.广度优先搜索对病菌进行扩散，同时计算天数

4.扩散停止，输出天数



要注意输出结果：当天数为0时，要么初始时全部被感染，要么初始时没一个病菌，那么应该返回-1



## 解题代码

```python
def solve_method(s):
    s = s.split(',')
    n = len(s)
    # 因为行列相等，直接开方
    row = col = int(n**0.5)

    # 一维数组切分成二维数组，方便遍历
    places = []
    for i in range(0, n, row):
        places.append(s[i:i+row])
        
    # 先将病毒的初始位置记录下来
    virus = []
    for i in range(row):
        for j in range(col):
            if places[i][j]=='1':
                virus.append((i,j))
    # 记录天数，每次广度优先搜索一次，天数+1
    days = 0
    # 从病毒的初始位置开始，广度优先搜索
    while virus:
        tmp = []
        while virus:
            i, j = virus.pop()
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0<=x<row and 0<=y<col and places[x][y]=='0':
                    tmp.append((x, y))
                    places[x][y]='1'
        virus = tmp
        if not virus:
            break
        else:
            days+=1
    return days if days else -1


if __name__ == '__main__':
    assert solve_method("1,0,1,0,0,0,1,0,1") == 2
    assert solve_method("0,0,0,0") == -1
    assert solve_method("1,1,1,1,1,1,1,1,1") == -1
    assert solve_method("1") == -1
    assert solve_method("0,1,1,0") == 1

```



