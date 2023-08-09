# 168 - 磁盘容量

## 题目

磁盘的容量单位常用的有`M`、`G`、`T`
他们之间的换算关系为`1T =1024G` , `1G=1024M`
现在给定n块磁盘的容量，请对他们按从小到大的顺序进行稳定排序

例如：给定`5`块盘的容量：

`5`

`1T`

`20M`

`3G`

`10G6T`

`3M12G9M`

排序后的结果为：

`20M`

`3G`

`3M12G9M`

`1T`

`10G6T`

注意：单位可以重复出现
上述`3N12G9M`表示的容量即为`3M12G9M`和`12M12G`相等



## 输入

输入第一行包含一个整数`n `， `2 <= n<= 100`，表示磁盘的个数。
接下来的n行，每行一个字符串，`2<长度< 30`，表示磁盘的容量，
由一个或多个格式为`M V`的子串组成，其中`M`表示容量大小，`V`表示容量单位，

例如`20M`、`1T`。
磁盘容量的范围`1～1024`的正整数，单位`M`、`G`、`T`。

## 输出描述

输出`n`行

表示`n`块磁盘容量排序后的结果



## 示例一

### 输入

```
3
1G
2G
1024M
```

### 输出

```
1G
1024M
2G
```

### 说明

稳定排序要求相等值保留原来位置



## 示例二

### 输入

```
3
2G4M
3M2G
1T
```

### 输出

```
3M2G
2G4M
1T
```



## 解题思路

将所有不同单位转化为同一个单位来进行比较即可，转换成M,G,T任一都可以。



## 解题代码

```python
def solve_method(n, capacity):
    def cmp(x):
        res = 0
        n = len(x)
        left = right = 0
        while right<n:
            if x[right].isdigit():
                right+=1
            elif x[right]=='M':
                res+=int(x[left:right])
                right+=1
                left = right
            elif x[right]=='G':
                res+=int(x[left:right])*1024
                right+=1
                left = right
            elif x[right]=='T':
                res+=int(x[left:right])*1024*1024
                right+=1
                left = right
        return res
    # 按照cmp函数进行排序
    # 排序规则，将其全部转化为M最小单位来比较大小
    # 为了防止转换成M数值过大而溢出，也可以转成G或者T皆可
    capacity.sort(key=cmp)
    return capacity


if __name__ == '__main__':
    assert solve_method(5, ['1T', '20M', '3G', '10G6T','3M12G9M']) == ['20M', '3G', '3M12G9M', '1T', '10G6T']
    assert solve_method(3, ['1G', '2G', '1024M']) == ['1G', '1024M', '2G']
    assert solve_method(3, ['2G4M', '3M2G', '1T']) == ['3M2G', '2G4M', '1T']
```



