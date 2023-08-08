# 034 删除指定目录

## 题目描述

某文件系统中有`N`个目录，每个目录都一个独一无二的ID。每个目录只有一个父目录，但每个目录下可以有零个或多个子目录，目录结构呈树状结构。

假设根目录的ID为0，且根目录没有父目录，ID用唯一的正整数表示，并统一编号。

现给定目录ID和其父目录ID的对应父子关系表：`[子目录ID,父目录ID]`，以及一个待删除的目录ID。

请计算并返回一个ID序列，表示因为删除指定目录后剩下的所有目录，返回的ID序列以递增序输出。

注意：
1. 被删除的目录或文件编号一定在输入的ID序列中。
2. 当一个目录删除时，它所有的子目录都会被删除。

## 输入描述

输入的第一行是父子关系表的长度`m`。

接下来的`m`行是`m`个父子关系对。

最后一行是待删除的ID，序列中的元素以空格分隔，参见样例。

## 输出描述

输出一个序列，表示因为删除指定目录后，剩余的目录ID。

## 示例描述

### 示例一

**输入：**

```text
5
8 6
10 8
6 0
20 8
2 6
8
```

**输出：**

```text
2 6
```

## 解题思路

**基本思路：**

1. 遍历节点，构建目录树，`key`为父目录ID，`value`为子目录ID列表。
2. 使用递归方式删除子目录：
    - 确定参数：目录树`tree`、待删除目录`node`。
    - 终止条件：待删除目录没有子目录，直接返回。
    - 递归处理：先删除子目录，然后递归删除父目录下的子目录
3. 使用`set`集合，存储剩余目录，并排序之后返回结果。    

## 解题代码

```Python
from collections import defaultdict


def build_tree(dirs, tree):
    for dir_ids in dirs:
        node, parent = dir_ids[0], dir_ids[1]
        tree[parent].append(node)


def rm_node(tree, node):
    # 删除子目录
    for k, v in tree.items():
        if node in v:
            v.remove(node)

    if node in tree.keys():
        # 删除父目录
        children = tree.pop(node)

        for sub_node in children:
            # 递归删除目录
            rm_node(tree, sub_node)


def solve_method(dirs, dir_id):
    tree = defaultdict(list)
    build_tree(dirs, tree)
    rm_node(tree, dir_id)

    result = set()
    for k, v in tree.items():
        if k != 0:
            result.add(k)
            for node in v:
                result.add(node)
    return list(sorted(result))


if __name__ == '__main__':
    dirs = [[8, 6],
            [10, 8],
            [6, 0],
            [20, 8],
            [2, 6]]
    assert solve_method(dirs, 8) == [2, 6]
```



