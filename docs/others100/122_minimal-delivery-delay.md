# 122 最小传递延时

## 题目描述

通讯网络中有`N`个网络节点，用1\~N进行标识。网络通过一个有向无环图进行表示，其中图的边的值，表示节点之间的消息传递延时。

现给定相连节点之间的延时列表`times[i]={u,v,w}`，其中`u`表示源节点，`v`表示目的节点，`w`表示`u`和`v`之间的消息传递延时。

请计算给定源节点到目的节点的最小传递延时，如果目的节点不可达，请返回-1。

注意：`N`的取值范围是1\~100，延时`times`列表长度不超过6000，且`1 <= u, v <= N, 0 <= w <= 100`。

## 输入描述

输入第1行是两个正整数，分别表示网络节点个数`N`以及延时列表长度`M`，用空格分隔。

接下来的`M`行表示两个节点间的延时列表`[u,v,w]`

输入的最后一行是两个正整数`u`和`v`，分别表示源节点和目的节点。

## 输出描述

输出一个整数，表示源节点到目的节点的最小延时。

## 示例描述

### 示例一

**输入：**
```text
3 3
1 2 11
2 3 13
1 3 50
1 3
```

**输出：**
```text
24
```

**说明：**  
1 \~ 3 的延时是50，1\~2\~3的延迟是11+13=24，所以1\~3的最小延时是24。

### 示例二

**输入：**
```text
5 7
1 2 11
2 3 13
1 3 50
3 4 55
4 5 35
2 4 15
3 5 40
1 5
```

**输出：**
```text
61
```

## 解题思路

**基本思路：** 本题采用回溯算法求解，回溯法三部曲如下：
1. 确定参数：包括延时列表`times`、开始节点`start`、结束节点`end`、路径`paths`、结果列表`result`。
2. 终止条件：当开始节点等于结束节点时
    - 当`paths`列表中仅有一个值（即直接找到了直达路径），直接取延时时间，存入结果列表中。
    - 当`paths`列表中大于一个值（即有多个节点），求延时累和，并存入结果列表中。
3. 回溯搜索遍历过程：
   - 循环访问所有节点，排除已经在路径的节点。
   - 如果还存在跳跃节点，添加当前节点到路径中，将继续递归。
   - 回溯，在路径中删除当前节点。 
4. 返回结果列表中最小值。

## 解题代码

```python
def backtracking(times, start, end, paths, result):
    if start == end:
        if len(paths) == 1:
            return result.append(paths[0][2])
        elif len(paths) > 1:
            length = 0
            for node in paths:
                length += node[2]
            return result.append(length)

    for node in times:
        if node not in paths:
            if node[0] == start:
                paths.append(node)
                backtracking(times, node[1], end, paths, result)
                paths.remove(node)


def solve_method(times, start, end):
    paths = []
    result = []
    backtracking(times, start, end, paths, result)

    return -1 if len(result) == 0 else min(result)
```