# 196 跳格子（1）

## 题目描述

地上共有`N`个格子，你需要跳完地上所有的格子，但是格子间是有强依赖关系的，跳完前一个格子后，后续的格子才会被开启，格子间的依赖关系由多组`steps`数组给出，`steps[0]`表示前一个格子，`steps[1]`表示`steps[0]`可以开启的格子：

- 比如`[0,1]`表示从跳完第0个格子以后，第1个格子就开启了。
- 比如`[2,1]`、`[2,3]`表示跳完第2个格子后，第1个格子和第3个格子就被开启了。

请你计算是否能由给出的`steps`数组跳完所有的格子，如果可以输出`yes`，否则输出`no`。

**说明：**

1. 你可以从一个格子跳到任意一个开启的格子。
2. 没有前置依赖条件的格子默认就是开启的。
3. 如果总数是`N`，则所有的格子编号为`[0, 1, 2, 3, ..., N-1]`连续的数组。
4. 仅有一个格子与一个格子之间的依赖，不会存在需要开启两个格子，才能开启后续的格子的情况。

其中：
- 1 <= N < 500
- steps[i].length = 2
- 0 <= step[i][0], step[i][1] < N

## 输入描述

输入一个整数`N`，表示总共的格子数量。

接着输入多组二维数组`steps`，表示所有格子之间的依赖关系。

## 输出描述

如果能按照`steps`给定的依赖顺序跳完所有的格子，输出`yes`，否则输出`no`。

## 示例描述

### 示例一

**输入：**

```text
3
0 1
0 2
```

**输出：**

```text
yes
```

**说明：**

总共有3个格子`[0,1,2]`，跳完0个格子后第1个格子就开启了，跳到第0个格子后第2个格子也被开启了。

按照`0->1->2`或者`0->2->1`的顺序都可以跳完所有的格子，所以，输出`yes`。

### 示例二

**输入：**

```text
2
1 0
0 1
```

**输出：**

```text
no
```

**说明：**

总共有2个格子，第1个格子可以开启第0个格子，但是第1个格子又需要第0个格子才能开启，相互依赖，因此无法完成。

### 示例三

**输入：**

```text
6
0 1
0 2
0 3
0 4
0 5
```

**输出：**

```text
yes
```

**说明：**

总共有6个格子，第0个格子可以开启第1、2、3、4、5个格子，所以跳完第0个格子之后，其他格子都被开启了，之后按照任意顺序都可以跳完剩余的格子。

### 示例四

**输入：**

```text
5
4 3
0 4
2 1
3 2
```

**输出：**

```text
yes
```

**说明：**

跳完第0个格子可以开启格子4，跳完格子4可以开启格子3，跳完格子3可以开启格子2，跳完格子2可以开启格子1，按照`0->4->3->2->1`这样就能跳完所有的格子。

### 示例五

**输入：**

```text
4
1 2
1 0
```

**输出：**

```text
yes
```

**说明：**

总共4个格子`[0,1,2,3]`，格子1和格子3没有前置条件，所以默认开启，格子1可以开启格子0和格子2，所以跳到格子1之后就可以开启所有的格子，因此可以跳完所有格子。

## 解题思路

1. 初始化格子开启字典`step_map`，`key`为前一个格子，`value`为被开启格子的列表。
2. 得到没有前置条件的格子`visited`。
3. 访问所有需要依赖条件的格子：
    - 如果存在环，则返回`no`。
    - 如果无法开启对应的格子（即不存在起始格子），则返回`no`。
4. 如果所有的格子都访问过了，则返回`yes`。

## 解题代码

```python
from collections import defaultdict


def solve_method(n, steps):
    # 格子开启字典，key为前一个格子，value为被开启格子的列表
    step_map = defaultdict(list)
    # 得到没有前置条件的格子
    visited = set(range(n))
    for start, node in steps:
        step_map[start].append(node)
        visited.discard(node)

    while len(step_map) != 0:
        # 如果还有剩余的格子没有开启
        visited_update = set()
        for node in visited:
            nodes = step_map.get(node, [])
            if nodes:
                if not set(nodes).difference(visited):
                    # 如果存在环，则返回no
                    return "no"
                else:
                    # 开启对应的格子
                    visited_update = visited_update.union(set(nodes))
                    step_map.pop(node)
        if visited_update:
            visited = visited.union(visited_update)
        else:
            # 如果无法开启对应的格子，则返回no
            return "no"

    if len(visited) == n:
        return "yes"


if __name__ == '__main__':
    steps = [[0, 1], [0, 2]]
    assert solve_method(3, steps) == "yes"

    steps = [[1, 0], [0, 1]]
    assert solve_method(2, steps) == "no"

    steps = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    assert solve_method(6, steps) == "yes"

    steps = [[4, 3], [0, 4], [2, 1], [3, 2]]
    assert solve_method(5, steps) == "yes"

    steps = [[1, 2], [1, 0]]
    assert solve_method(4, steps) == "yes"

    steps = [[1, 2], [2, 3], [3, 1]]
    assert solve_method(4, steps) == "no"
```

