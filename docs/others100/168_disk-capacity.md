# 168 磁盘容量

## 题目描述

磁盘的容量单位常用的有`M`、`G`、`T`，它们之间的换算关系为1T=1024G、1G=1024M。

现在给定`n`块磁盘的容量，请对它们按从小到大的顺序进行稳定排序。

例如：给定`5`块盘的容量：
```text
5
1T
20M
3G
10G6T
3M12G9M
```

排序后的结果为：
```text
20M
3G
3M12G9M
1T
10G6T
```

注意：单位可以重复出现，上述`3N12G9M`表示的容量即为`3M12G9M`和`12M12G`相等。

## 输入描述

输入第一行包含一个整数`n `，取值范围是2 <= n <= 100，表示磁盘的个数。

接下来的`n`行，每行一个字符串，2 < 字符串长度 < 30，表示磁盘的容量。由一个或多个格式为`MV`的子串组成，其中`M`表示容量大小，`V`表示容量单位。例如`20M`、`1T`。

磁盘容量的范围是`1～1024`的正整数，单位`M`、`G`、`T`。

## 输出描述

输出`n`行，表示`n`块磁盘容量排序后的结果。

## 示例描述

### 示例一

**输入：**

```text
3
1G
2G
1024M
```

**输出：**

```text
1G
1024M
2G
```

**说明：**

稳定排序要求相等值保留原来位置。

### 示例二

**输入：**

```text
3
2G4M
3M2G
1T
```

**输出：**

```text
3M2G
2G4M
1T
```

## 解题思路

1. 使用`sort`函数，对`key`关键字传入自定义的比较函数`cmp`，对磁盘容量进行排序。
2. 自定义的比较函数`cmp`：使用双指针，获取磁盘容量，并将其转换为以`M`为单位的容量值。
3. 返回排序结果。

## 解题代码

```python
def solve_method(n, disks):
    def cmp(x):
        res = 0
        left = right = 0
        while right < len(x):
            if x[right].isdigit():
                right += 1
            elif x[right] == 'M':
                res += int(x[left:right])
                right += 1
                left = right
            elif x[right] == 'G':
                res += int(x[left:right]) * 1024
                right += 1
                left = right
            elif x[right] == 'T':
                res += int(x[left:right]) * 1024 * 1024
                right += 1
                left = right
        return res

    # 按照cmp函数进行排序
    # 排序规则，将其全部转化为M最小单位来比较大小
    # 为了防止转换成M数值过大而溢出，也可以转成G或者T皆可
    disks.sort(key=cmp)
    return disks


if __name__ == '__main__':
    disks = ['1T', '20M', '3G', '10G6T', '3M12G9M']
    assert solve_method(5, disks) == ['20M', '3G', '3M12G9M', '1T', '10G6T']

    disks = ['1G', '2G', '1024M']
    assert solve_method(3, disks) == ['1G', '1024M', '2G']

    disks = ['2G4M', '3M2G', '1T']
    assert solve_method(3, disks) == ['3M2G', '2G4M', '1T']
```



