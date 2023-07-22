# 213 需要广播的服务器数量

## 题目描述

服务器连接方式包括直接相连和间接相连。`A`和`B`直接连接，`B`和`C`直接连接，则`A`和`C`间接连接。直接连接和间接连接都可以发送广播。

给出一个`N*N`数组，表示`N`个服务器，其中`matrix[i][j] == 1`表示`i`和`j`直接连接，不等于1，代表`i`和`j`不直接连接，`matrix[i][i] == 1`，表示自己和自己可以直接连接，并且`matrix[i][j] == matrix[j][i]`

计算初始需要给多少台服务器广播，才可以使每个服务器都收到广播。

## 输入描述

输入为`N`行，每行有`N`个数组，为0或为1，由空格分隔，构成`N*N`的数组，`N`的范围为`1 <= N <= 40`。

## 输出描述

输出一个数字，表示需要广播的服务器数量。

## 示例描述

### 示例一

**输入：**
```text
1 0 0
0 1 0
0 0 1
```

**输出：**
```text
3
```

**说明：**  
3台服务器互不相连，所以需要分别广播这3台服务器。

### 示例二

**输入：**
```text
1 1
1 1
```

**输出：**
```text
1
```

**说明：**  
2台服务器互相连接，所以只需要广播其中1台服务器。

## 解题思路

1. 初始化连接关系字典，`key`表示服务器编号，`value`表示与该服务器相连的服务器编号。
2. 遍历服务器：
   - 寻找是否与该服务器相连的服务器
        - 如果找到了，则返回相连的服务器编号
        - 如果没有找到，则初始化该服务器的相连关系列表
   - 继续寻找后续服务器是否与该服务器直接连接
        - 如果有直接连接的服务器，则放入该服务器的相连关系列表中
3. 返回需要广播的服务器数量，即为相连关系中的服务器个数。

## 解题代码

```python
from collections import defaultdict


def solve_method(arr):
    # 连接关系
    connect_map = defaultdict(list)
    for i in range(len(arr)):
        is_contain = False
        # 寻找是否与该服务器直接连接的服务器
        for k, v in connect_map.items():
            if i in v:
                is_contain = True
                map_key = k
        # 如果没有，则初始化连接关系
        if not is_contain:
            connect_map[i] = []
            map_key = i
        # 继续寻找后续服务器是否与该服务器直接连接
        for j in range(i, len(arr)):
            if i != j and arr[i][j] == 1:
                # 如果有直接连接的服务器，则放入对应的列表中
                connect_map[map_key].append(j)

    # 得到需要广播的服务器数量，即为相连关系中的服务器个数。
    return len(connect_map)


if __name__ == '__main__':
    arr = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
    assert solve_method(arr) == 3

    arr = [[1, 1],
           [1, 1]]
    assert solve_method(arr) == 1

    arr = [[1, 1, 0],
           [1, 1, 0],
           [0, 0, 1]]
    assert solve_method(arr) == 2
```