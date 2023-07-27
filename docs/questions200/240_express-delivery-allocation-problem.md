# 240 快递投放问题

## 题目描述

有`N`个快递站点用字符串标识，某些站点之间有道路连接。每个站点有一些包裹要运输，每个站点间的包裹不重复，路上有检查站会导致部分货物无法通行，计算哪些货物无法正常投递。

## 输入描述
```text
4 2
package1 A C
package2 A C
package3 B C
package4 A C
A B package1
A C package2 package4
```
第一行输入`M`和`N`，`M`表示包裹数量，`N`表示道路个数. 取值范围是0 <= M,N <= 100，检查站禁止通行的包裹如果有多个以空格分隔。

## 输出描述

输出不能送达的包裹`package2 package4`，如果所有包裹都可以送达，则输出`none`，输出结果按照升序排列。

## 示例描述

### 示例一

**输入：**
```text
4 2
package1 A C
package2 A C
package3 B C
package4 A C
A B package1
A C package2
```

**输出：**
```text
package2
```

## 解题思路

**简单提示：**  

把相关的信息记录起来，模拟每一个包裹具体的路径情况，如果不允许通行，则记录该包裹名。

## 解题代码

```python
from collections import defaultdict


def solve_method(want, cant):
    # 初始化包裹道路信息的 字典 和 无法通行的道路字典
    want_map = defaultdict(set)
    cant_map = defaultdict(set)

    # 将 want 中 包裹道路信息，按照 [key = package] = "起点-终点"的格式记录在want_map字典里
    for arr in want:
        pkg, path1, path2 = arr
        path = path1 + "-" + path2
        want_map[path].add(pkg)

    # 将 cant 中 不可通行信息，按照 [key = "起点-终点"] = 包裹1，包裹2，... 的格式记录在cant_map字典里
    for arr in cant:
        path1, path2, *pkgs = arr
        path = path1 + "-" + path2
        cant_map[path].update(pkgs)

    res = []
    for path, want_pkg in want_map.items():
        # 遍历包裹道路信息，在不可通行信息中找 key = 道路
        cant_pkg = cant_map.get(path)

        if cant_pkg is None:
            continue

        # 将两个集合求交集，即不可通行信息中对应的包裹，记录到结果列表中
        cant_pkgs = cant_pkg.intersection(want_pkg)
        res.extend(list(cant_pkgs))

    if not res:
        return "none"

    # 按照包裹序列进行排序
    res.sort(key=lambda s: int(s[7:]))

    return res


if __name__ == '__main__':
    packages = [["package1", "A", "C"],
                ["package2", "A", "C"],
                ["package3", "B", "C"],
                ["package4", "A", "C"]]
    barries = [["A", "B", "package1"],
               ["A", "C", "package2"]]
    assert solve_method(packages, barries) == ["package2"]
```