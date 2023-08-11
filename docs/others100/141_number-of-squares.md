# 141-构成的正方形数量

## 题目描述

输入N个互不相同的二维整数坐标（即N个点）, 求这N个坐标可以构成的正方形数量。



## 输入描述

* 第一行输入为`N`, 代表坐标数量（即点数）, `N`为正整数, 且`N<=100`
* 之后的`N`行输入为`x y`, `x` 和`y`为整数, 且以空格分隔, 均满足：`-10 <= x,y <=10`



## 输出描述

输出N个点可以构成的正方形数量



## 示例描述

### 示例一

**输入：**

```
3
1 3
2 4
3 1
```

**输出：**

```
0
```

**说明：**

3个点无法构成正方形



### 示例二

**输入：**

```
4
0 0
1 2
3 1
2 -1
```

**输出：**

```
1
```

**说明：**

这四个点可以构成一个正方形。四条边相等且互相垂直。



## 解题思路

### 直接方法：每次选4个点判断

1.   我们得到`N`个点的坐标以后, 无非**循环执行两个步骤**
   - 从`N`个点里**不重复地选出4个点的组合**
   - 判断**4个点能否形成正方形**
   - 当不能再选出新的点的组合时, 循环结束, 返回正方形个数。
2.   那么怎么从`N`个点里依次选出4个点来呢？

最简单的想法就是一个用四重循环：

```python
...
points=[]
...
for i in range(n-3):
    for j in range(i+1,n-2):
        for k in range(j+1,n-1):
            for p in range(k+1,n):
                if(is_square(points[i],points[j],points[k],points[p])):
                    # 4个点构成正方形则计数+1
                    count += 1
```

不过上面那种写法看起来感觉很冗长，最好使用python内置库`itertools模块`进行组合：

```python
# 使用 itertools.combinations 生成4个点索引的不重复组合;
points_combination = itertools.combinations(range(len(points)), 4)
count = 0
for combination in points_combination:
    four_points = [ points[index] for index in combination ]
```





3. 选出了4个点，怎么判断它们可否构成正方形呢？
   - 我们有4个点的坐标, 每两个点之间可以形成一条边, 就有6条边。
   - 正方形的四个顶点之间正好有**四条边**，**两条对角线**，同时正方形对角线长度是边的根号二倍。
   - 所以我们可以**计算得到6条边的长度**, 如果这6条边里的**4条短边之间长度相等**, 证明这个四边形是菱形。而**两条长边之间也长度相等**，进一步推得它是正方形。



- 该方法的时间复杂度：

这个时间复杂度很大。幸好我们已知 `N 不超过 100`, 在时间要求不紧张的情况下, 使用这种办法是可以的
$$
四重循环： C_N^4=(_4^N)=\frac{N(N-1)(N-2)(N-3)}{4*3*2*1}=\frac{N^4+...}{24}\le 10^7
\\
算法的时间复杂度大概是O(N^4)
$$



#### 解题代码

```python
import itertools
from typing import List

def solve_method(points: List[List[int]]) -> int:
    # 1. 定义 is_square([points1,...,points4]= 点1,点2,点3,点4能否构成正方形
    def is_square(points: List[List[int]]) -> bool:
        assert len(points) == 4
        # 计算每个点两两之间的边长
        distances = []
        for i in range(3):
            for j in range(i + 1, 4):
                x, y = points[i][0] - points[j][0], points[i][1] - points[j][1]
                distances.append(x * x + y * y)

        distances.sort()
        # 条件1：四条边长度相等（保证是菱形）
        # 条件2：两条对角线长度相等（菱形的两条对角线相等,那么就是正方形）
        return (distances[0] == distances[1]) and (distances[1] == distances[2]) and (
                distances[2] == distances[3]) and (distances[4] == distances[5])

    # 2. 使用  itertools.combinations 生成4个点索引的不重复组合; 调用 is_square 判断点的组合能否构成正方形
    points_combination = itertools.combinations(range(len(points)), 4)
    count = 0
    for combination in points_combination:
        count += 1 if is_square([points[index] for index in combination]) else 0
    return count
```





### 其他方法

该题跟数学关系很大，关键在于两点，第一是怎么**从N个点里挑选出点的组合**，第二**判断点的组合能不能构成正方形**。

除了每次4个点选取组合，我们也可以每次少选取点的组合，引入更多的分析。



比如：

#### 每个组合选三个点

- 假如给定4个点可以组成正方形：`[(0,0),(0,1),(1,0),(1,1)]`

我们先选出3个点`(0,0),(0,1),(1,0)`, 计算得到3条边 00到01, 00到10, 01到10, 长度分别为1, 1, 根号二。

我们发现有两条边相等, 长边的长度是短边的根号2倍, 说明这三个点是可能构成正方形的。我们再加上一个合适的点就可以构成正方形。

实际上, 如果确定了这三个点, 最后一个点的位置是唯一的。

- 这种办法的时间效率也不是最高的, 我们可以每个组合只选两个点。



#### 每个组合选两个点

我们设两个点为(x1,y1),(x2,y2)。

同样用高中数学的向量运算, 我们可以用这四个变量x1, x2, y1, y2来表示其他两个顶点。

> - Case 1
>
> x3=x1+(y1-y2); y3=y1-(x1-x2);
>
> x4=x2+(y1-y2); y4=y2-(x1-x2);
>
> 
>
> - Case 2
>
> x3=x1-(y1-y2); y3=y1+(x1-x2);
>
> x4=x2-(y1-y2); y4=y2+(x1-x2);



- 接下来，我们每次用一个二重循环遍历两个点的组合, 然后计算可能的(x3,y3)和(x4,y4), 并检查两个点是否在输入的点集里, 如果在, 计数就+1。

* 按这种方法, 一个正方形**ABCD**会被重复计算4次，所以真实次数还要除以4。



#### 解题代码

```python
def solve_method2(points: List[List[int]]) -> int:
    count = 0
    points_combination = itertools.combinations(range(len(points)), 2)
    for combination in points_combination:
        index1, index2 = combination[0], combination[1]
        x1, y1 = points[index1][0], points[index1][1]
        x2, y2 = points[index2][0], points[index2][1]

        x3, y3, x4, y4 = x1 + (y1 - y2), y1 - (x1 - x2), x2 + (y1 - y2), y2 - (x1 - x2)
        count += 1 if [x3, y3] in points and [x4, y4] in points else 0

        x3, y3, x4, y4 = x1 - (y1 - y2), y1 + (x1 - x2), x2 - (y1 - y2), y2 + (x1 - x2)

        count += 1 if [x3, y3] in points and [x4, y4] in points else 0

    # 一个正方形ABCD会被重复计算4次,所以真实次数还要除以4. 如: ABCD,AB+1,BC+1,CD+1,AD+1
    count //= 4
    return count
```


