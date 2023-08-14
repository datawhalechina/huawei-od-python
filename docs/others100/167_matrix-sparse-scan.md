# 167 矩形稀疏扫描

## 题目描述

如果矩阵中的许多系数都为零，那么该矩阵就是稀疏的。对稀疏现象有兴趣是因为它的开发可以带来巨大的计算节省，并且在许多大的实践中都会出现矩阵稀疏的问题。
给定一个矩阵，现在需要逐行和逐列地扫描矩阵，如果某一行或者某一列内，存在连续出现的0的个数超过了行宽或者列宽的一半【W/2】(地板除)，则认为该行或者该列是稀疏的。
扫描给定的矩阵，输出稀疏的行数和列数。



## 输入描述

第一行输入为M和N，表示矩阵的大小 M*N，0<M<=100，0<N<=100.
接下来M行输入为矩阵的成员，每行N个成员，矩阵成员都是有符号整数，范围-32,768到32,767。



## 输出描述

输出两行，第一行表示稀疏行的个数，第二行表示稀疏列的个数。


## 示例描述
### 示例一

**输入：**

```text
3 3
1 0 0
0 1 0
0 0 1
```

**输出：**
```text
3
3
```

**说明：**

给定的3 x 3矩阵里，每一行和每一列内都存在2个0，行宽3，列宽3，【3/2】=1，因此稀疏行有3个，稀疏列有3个。

### 示例二

**输入：**

```text
5 3
-1 0 1
0 0 0
-1 0 0
0 -1 0
0 0 0
10
```

**输出：**

```text
5
3
```

**说明：**

给定的5 x 3矩阵，每行里面0的个数大于等于1表示稀疏行，每列里面0的个数大于等于2表示稀疏行，所以有5个稀疏行，3个稀疏列。



## 解题思路
**基本思路：**
按照题目模拟即可，寻找每行每列0的次数是否超过相应的列数和行数，分别进行计数。



## 解题代码

```python
# 做法一，模拟
def solve_method1(row, col, matrix):
    count_row = 0
    for i in range(row):
        cnt = matrix[i].count(0)
        if cnt>=col//2:
            count_row+=1
    count_col = 0
    for i in range(col):
        tmp = []
        for j in range(row):
            tmp.append(matrix[j][i])
        cnt = tmp.count(0)
        if cnt>=row//2:
            count_col+=1
    return count_row, count_col

# 做法二，使用numpy并行加速处理
import numpy as np
def solve_menhod2(row, col, matrix):
    

    new_matrix = np.array(matrix)
    cnt_row = cnt_col=0


    # np.count_nonzero(matrix==X)可以统计X数值的个数
    cnt_row = np.count_nonzero(new_matrix==0, axis=1)
    # np.count_nonzero(matrix>=X)可以统计大于等于X数值的个数
    res_row = np.count_nonzero(cnt_row>=col//2)

    cnt_col = np.count_nonzero(new_matrix==0, axis=0)
    res_col = np.count_nonzero(cnt_col>=row//2)

    return res_row, res_col

if __name__ == '__main__':
    assert solve_method1(3, 3, [[1,0,0],[0,1,0],[0,0,1]]) == (3,3)
    assert solve_method1(5,3, [[-1,0,1],[0,0,0],[-1,0,0],[0,-1,0],[0,0,0]]) == (5,3)
    assert solve_method2(3, 3, [[1,0,0],[0,1,0],[0,0,1]]) == (3,3)
    assert solve_method2(5,3, [[-1,0,1],[0,0,0],[-1,0,0],[0,-1,0],[0,0,0]]) == (5,3)
```



