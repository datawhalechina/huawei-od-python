# 040 端口合并

## 题目描述

有`M`（1 <= M <= 10）个端口组，每个端口组是长度为`N`（1 <= N <= 100）的整数数组，如果端口组间存在2个及以上不同端口相同，则认为这2个端口组互相关联，可以合并.

第一行输入端口组个数`M`，再输入`M`行，每行`,`分隔，代表端口组。输出合并后的端口组，用二维数组表示。

## 输入描述

第一行输入一个数字`M`。

第二行开始输入`M`行，每行是长度为`N`的整数数组，用`,`分隔。

## 输出描述

合并后的二维数组。

## 示例描述

### 示例一

**输入：**
```text
4
4
2,3,2
1,2
5
```

**输出：**
```text
[[4],[2,3],[1,2],[5]]
```

**说明：**  
仅有一个端口2相同，不可以合并

### 示例二

**输入：**
```text
3
2,3,1
4,3,2
5
```

**输出：**
```text
[[1,2,3,4],[5]]
```

### 示例三

**输入：**
```text
6
10
4,2,1
9
3,6,9,2
6,3,4
8
```

**输出：**
```shell
[[10],[1,2,3,4,6,9],[9],[8]]
```

## 解题思路

1. 对端口组进行合并，遍历所有端口组：
    - 比较两个端口组合并之后的长度和，是否小于等于合并之前长度和减2（表示有至少两个相同的端口）。
    - 如果有，则合并一个，删除另一个。
2. 重复合并操作，直至没有需要合并的端口组。    
2. 返回去重合并之后的端口组。

## 解题代码

```python
def merge(ports):
    for i in range(len(ports)):
        for j in range(i + 1, len(ports)):
            seti = set(ports[i])
            setj = set(ports[j])
            merge_set = seti.union(setj)
            if len(merge_set) <= len(seti) + len(setj) - 2:
                ports[i] = list(merge_set)
                ports.pop(j)
                return True
    return False


def solve_method(ports):
    while merge(ports):
        pass

    return [sorted(list(set(p))) for p in ports]


if __name__ == '__main__':
    ports = [[4], [2, 3, 2], [1, 2], [5]]
    assert solve_method(ports) == [[4], [2, 3], [1, 2], [5]]
    ports = [[2, 3, 1], [4, 3, 2], [5]]
    assert solve_method(ports) == [[1, 2, 3, 4], [5]]
    ports = [[10], [4, 2, 1], [9], [3, 6, 9, 2], [6, 3, 4], [8]]
    assert solve_method(ports) == [[10], [1, 2, 3, 4, 6, 9], [9], [8]]
```