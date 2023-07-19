# 136 服务依赖、服务失效判断

## 题目描述

在某系统中有众多服务，每个服务用字符串（只包含字母和数字，长度 <= 10）作为唯一标识，服务间可能有依赖关系，如A依赖B，但当B故障时，导致A也故障。传递具有依赖性，如A依赖B，B依赖C，当C故障时导致B故障，也导致A故障。

给出所有依赖关系以及当前已知故障服务，要求输出所有正常的服务。

依赖关系：`服务1-服务2`表示服务1依赖服务2，不必考虑输入异常。

## 输入描述

第1行是依赖关系列表，用`,`分隔。

第2行是故障服务列表，用`,`分隔。

## 输出描述

依赖关系列表中提到的所有服务中可以正常工作的服务列表，用`,`分隔，按依赖关系列表中出现的顺序排序，如果没有正常节点，则输出一个`,`。

## 示例描述

### 示例一

**输入：**
```text
a1-a2,a5-a6,a2-a3
a5,a2
```

**输出：**
```text
a6,a3
```

**说明：**  
`a1`依赖`a2`，`a2`依赖`a3`，所以`a2`故障，导致`a1`不可用，但不影响`a3`，`a5`故障不影响`a6`，所以可用的是`a3`、`a6`，在依赖关系列表中`a6`先出现，所以输出`a6,a3`。

### 示例二

**输入：**
```text
a1-a2
a2
```

**输出：**
```text
,
```

**说明：**  
`a1`依赖`a2`，`a2`故障导致`a1`也故障，没有正常节点，输出`,`。

## 解题思路

**基本思路：** 使用深度优先搜索遍历服务依赖关系，得到所有故障服务。
1. 遍历依赖关系列表，得到所有服务`nodes`（已按照出现顺序排列）和服务依赖关系字典`server_dependencies`，其中`key`为依赖服务，`value`为被依赖服务。
2. 使用深度优先搜索遍历故障服务列表：
   - 确定参数：故障服务`node`、服务依赖关系字典`server_deps`、故障服务列表`paths`
   - 将故障服务添加故障服务列表`paths`中
   - 终止条件：如果没有依赖关系，停止递归
   - 通过服务依赖关系字典得到下一个故障的服务，继续递归
3. 从所有服务中按照顺序排除掉故障服务。
4. 返回正常工作的服务。

## 解题代码

```python
def dfs(node, server_deps, paths):
    # 添加到故障服务列表中
    if node not in paths:
        paths.append(node)

    if node not in server_deps:
        return

    # 得到依赖服务
    next_node = server_deps[node]
    dfs(next_node, server_deps, paths)


def solve_method(servers, errors):
    # 服务依赖服务
    servers = servers.split(",")
    # 故障服务
    errors = errors.split(",")
    # 所有服务
    nodes = []
    # 服务依赖关系
    server_dependencies = {}
    for server in servers:
        val, next = server.split("-")
        if val not in nodes:
            nodes.append(val)
        if next not in nodes:
            nodes.append(next)
        # 建立服务依赖关系
        server_dependencies[next] = val

    paths = []
    for error in errors:
        dfs(error, server_dependencies, paths)

    # 按照顺序排除掉故障服务
    good_nodes = [node for node in nodes if node not in paths]

    return ",".join(good_nodes) if len(good_nodes) != 0 else ","
```